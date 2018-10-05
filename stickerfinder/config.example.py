"""Config values for stickerfinder."""
from datetime import timedelta


class Config:
    """Config class for convenient configuration."""

    # Get your telegram api-key from @botfather
    TELEGRAM_API_KEY = None
    SQL_URI = 'sqlite:///stickerfinder.db'
    SENTRY_TOKEN = None
    # Username of the admin
    ADMIN = 'Nukesor'
    # Run maintenance jobs. This is important if you want to run multiple instances of the bot
    RUN_JOBS = True

    # Job parameter
    USER_CHECK_INTERVAL = timedelta(days=1)
    USER_CHECK_RECHECK_INTERVAL = timedelta(days=2)
    USER_CHECK_COUNT = 200
    VOTE_BAN_COUNT = 1


config = Config()
