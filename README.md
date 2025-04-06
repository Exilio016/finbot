# FINBOT
A telegram bot that uses AI to interface with a [Firefly III](https://github.com/firefly-iii/firefly-iii) server.

## Geting started
To get started, first you need to setup the following environment variables:
- FIREFLY_URL: The base URL for the firefly api calls. Example: `https://demo.firefly-iii.org/api`
- FIREFLY_TOKEN: The firefly personal access token. Can be generated on Profile page on firefly.
- OPENAI_API_KEY: The OpenAI API Key.
- BOT_TOKEN: The telegram bot token created by the `@BotFather`.
- ACCEPTED_USERS: The telegram user id.

If you are using nixos you can just run:
```bash
nix develop .#impure
uv run -m src
```

Otherwise you need to have installed `python` and `uv`, and run:
```bash
uv run -m src
```

