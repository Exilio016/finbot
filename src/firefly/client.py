from typing import Optional
from langchain_core.tools import tool
from openapi_client.api.accounts_api import AccountsApi
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.models.account_array import AccountArray
from openapi_client.models.account_type_filter import AccountTypeFilter
from openapi_client.models.budget_array import BudgetArray
from openapi_client.models.transaction_array import TransactionArray
from openapi_client.api.transactions_api import TransactionsApi
from openapi_client.models.transaction_type_filter import TransactionTypeFilter
from openapi_client.models.transaction_single import TransactionSingle
from openapi_client.models.transaction_store import TransactionStore
from openapi_client.api.budgets_api import BudgetsApi
from datetime import date
import os

config = Configuration(access_token=os.getenv("FIREFLY_TOKEN"), host=os.getenv("FIREFLY_URL"))

@tool
def list_accounts(type: AccountTypeFilter | None) -> AccountArray:
    """
    List all accounts.

    This endpoint returns a list of all the accounts owned by the authenticated user.
    
    :param type: Optional filter on the account type(s) returned  
    :type type: AccountTypeFilter  
    """
    with ApiClient(config) as client:
        accounts = AccountsApi(client)
        return accounts.list_account(type=type)

@tool
def list_transactions(type: TransactionTypeFilter | None, start_date: date | None, end_date: date | None) -> TransactionArray:
    """
    List all the user's transactions.
    
    :param start_date:This is the start date of the selected range (inclusive).  
    :type start_date: date  
    :param end_date: This is the end date of the selected range (inclusive).  
    :type end_date: date  
    :param type: Optional filter on the transaction type(s) returned.  
    :type type: TransactionTypeFilter  
    """
    with ApiClient(config) as client:
        transactions = TransactionsApi(client)
        return transactions.list_transaction(type=type, start=start_date, end=end_date)

@tool
def create_transaction(transaction: TransactionStore) -> TransactionSingle:
    """
    Store a new transaction
    Creates a new transaction. The data required can be submitted as a JSON body or as a list of parameters.

    :param transaction: JSON array or key=value pairs with the necessary transaction information. See the model for the exact specifications. (required)  
    :type transaction: TransactionStore  
    """
    with ApiClient(config) as client:
        api = TransactionsApi(client)
        return api.store_transaction(transaction)

@tool
def list_budgets(start: Optional[date], end: Optional[date]) -> BudgetArray:
    """
    List all budgets.
    List all the budgets the user has made. If the start date and end date are submitted as well, the "spent" array will be updated accordingly.
    :param start: A date formatted YYYY-MM-DD, to get info on how much the user has spent. You must submit both start and end.  
    :type start: date  
    :param end: A date formatted YYYY-MM-DD, to get info on how much the user has spent. You must submit both start and end.  
    :type end: date  
    """
    with ApiClient(config) as client:
        api = BudgetsApi(client)
        return api.list_budget(start=start, end=end)
