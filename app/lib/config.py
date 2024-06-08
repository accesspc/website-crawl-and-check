import logging
import sys
import yaml

log = logging.getLogger('config')

class Config():

    # Init - read config file
    def __init__(self) -> None:
        cfg = 'config/config.yml'

        try:
            with open(cfg, 'r') as cf:
                config = yaml.safe_load(cf)
                self._cron = config['cron']
                self._email = config['email']
                self._websites = config['websites']
        except IOError as e:
            log.error(f'IOError: {e}')
            sys.exit(1)
        except Exception as e:
            log.error(f'Exception: {e}')
            sys.exit(1)

    # Attributes
    ## Cron
    @property
    def cron(self):
        return self._cron

    @cron.setter
    def cron(self, value):
        self._cron = value

    ## Email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    ## Websites
    @property
    def websites(self):
        return self._websites

    @websites.setter
    def websites(self, value):
        self._websites = value
