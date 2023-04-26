from os import environ as env

from hypercorn import Config as HypercornConfig


class Config(HypercornConfig):
    """
    Summary
    -------
    the config class for the server

    Attributes
    ----------
    openai_api_key (str) : the openai api key
    """
    _bind = [f"0.0.0.0:{env['UNSTRUCTURED_PORT']}"]
    access_log_format = '%(s)s "%(R)s" %(h)s "%(a)s"'
    accesslog = '-'
    use_reloader = True
