import yaml
import datetime
from logging_err import *


class Config:
    __instance = None

    @staticmethod
    def inst():
        if Config.__instance == None:
            Config.__instance = Config()
        return Config.__instance

    def __init__(self):
        print('config')
        import sys, os
        if getattr(sys, 'frozen', False):
            self.BASE_DIR = os.getcwd()
        else:
            self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.filename_config = os.path.join(self.BASE_DIR, 'yaml', 'setting.yaml')
        try:

            with open(self.filename_config, 'r', encoding='utf-8') as yaml_config_file:
                self.config = yaml.load(yaml_config_file)
        except Exception as e:
            self.config = {}

    @property
    def version(self):
        return self.config

    @version.setter
    def version(self, value):
        self.config[datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")] = value
        with open(self.filename_config, "w", encoding='utf-8') as f:
            yaml.dump(self.config, f, default_flow_style=False)
