from datetime import date
from typing import Optional
from langchain.chat_models import init_chat_model
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from src.firefly import create_transaction, list_accounts, list_transactions, list_budgets
from telegram import Update, User
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from langchain_community.document_loaders import PyPDFLoader
import os

@tool
def current_date() -> date:
    """
    It return today's date.
    """
    return date.today()

class Agent:
    def __init__(self) -> None:
        model = init_chat_model("gpt-4o-mini", model_provider="OpenAI")
        memory = MemorySaver()
        tools = [list_accounts, list_transactions, create_transaction, list_budgets, current_date]
        self.agent = create_react_agent(model, tools, checkpointer=memory)

    def prompt(self, question: str, chat_id: str):
        config = RunnableConfig(configurable = {"thread_id": chat_id})
        return self.agent.invoke({"messages":[("user", question)]}, config=config, debug=True)

agent = Agent()
users = os.getenv("ACCEPTED_USERS")

def validate_user(user: Optional[User]):
    if not users:
        return True
    if not user:
        return False
    ids = users.split(",")
    return user.id in ids

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Receive message...")
    user = update.effective_user
    message = update.effective_message
    if  message and validate_user(user):
        question = str(message.text)
        chat_id = str(message.chat_id)
        res = agent.prompt(question, chat_id)
        ai_message = res['messages'][-1].content
        await context.bot.send_message(chat_id, ai_message)

async def handle_attachment_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Receive attachment message...")
    user = update.effective_user
    message = update.effective_message
    if message and validate_user(user):
        additional_data = str(message.text)
        doc = message.document
        chat_id = str(message.chat_id)
        if doc:
            await context.bot.send_message(chat_id, "I will process this file and create the transaction...")
            file = await doc.get_file()
            loader = PyPDFLoader(str(file.file_path))
            docs = loader.load()
            question = f"Using the following document create a new transaction.\nAdditional data: ${additional_data}\nDocument:${docs}"
            res = agent.prompt(question, chat_id)
            ai_message = res['messages'][-1].content
            await context.bot.send_message(chat_id, ai_message)

def main():
    bot = ApplicationBuilder().token(str(os.getenv('BOT_TOKEN'))).build()
    handler = MessageHandler(filters.TEXT, handle_message)
    attachement_handler = MessageHandler(filters.ATTACHMENT, handle_attachment_message)
    bot.add_handler(handler)
    bot.add_handler(attachement_handler)
    bot.run_polling()

if __name__ == "__main__":
    main()
