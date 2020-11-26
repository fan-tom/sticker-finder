"""Config values for stickerfinder."""
import os
import sys
import toml
import logging

default_config = {
    "telegram": {
        "api_key": "your_telegram_api_key",
        "worker_count": 20,
        "admin": "your user name",
        "bot_name": "your bot name",
    },
    "database": {
        "sql_uri": "postgres://localhost/stickerfinder",
        "connection_count": 20,
        "overflow_count": 10,
    },
    "logging": {
        "sentry_enabled": False,
        "sentry_token": "",
        "log_level": logging.INFO,
        "debug": False,
    },
    "webhook": {
        "enabled": False,
        "domain": "https://localhost",
        "token": "stickerfinder",
        "cert_path": "/path/to/cert.pem",
        "port": 7000,
    },
    "job": {
        "user_check_count": 200,
        "report_count": 5,
    },
    "mode": {
        "leecher": False,
        "authorized_only": False,
        "auto_accept_set": False,
        "private_inline_query": False,
        "inline_cache_size": 500,
    },
}

# config_path = os.path.expanduser("~/.config/stickerfinder.toml")
config_path = "stickerfinder.toml"

if not os.path.exists(config_path):
    with open(config_path, "w") as file_descriptor:
        toml.dump(default_config, file_descriptor)
    print("Please adjust the configuration file at '~/.config/stickerfinder.toml'")
    sys.exit(1)
else:
    config = toml.load(config_path)

    # Set default values for any missing keys in the loaded config
    for key, category in default_config.items():
        for option, value in category.items():
            if option not in config[key]:
                config[key][option] = value

    # Handle heroku
    port = int(os.environ.get('PORT', -1))
    if port >= 0:
        config["webhook"]["port"] = port

    db_url = os.environ.get('DATABASE_URL')

    if db_url is not None:
        config["database"]["sql_url"] = db_url

    webhooktoken = os.environ.get('WEBHOOK_TOKEN')
    if webhooktoken is not None:
        config["webhook"]["token"] = webhooktoken

    bot_token = os.environ.get('BOT_TOKEN')
    if bot_token is not None:
        config["telegram"]["api_key"] = bot_token
