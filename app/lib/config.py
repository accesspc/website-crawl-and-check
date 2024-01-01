import yaml


class Config():

    def __init__(self):
        cfg = 'config/config.yml'

        with open(cfg, 'r') as cf:
            config = yaml.safe_load(cf)
            self.email = config['email']
            self.websites = config['websites']
