# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
"""
This module contains the configuration class
"""
import logging
import json

# from meliora.enums import RunMode, State, Exchange, Fiat
# from meliora.config import constants

logger = logging.getLogger(__name__)


class Configuration:
    """
    Class to read and init the bot configuration
    Reuse this class for the bot, backtesting and every script that required configuration
    """
