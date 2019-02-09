import os
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
            # If the application is run as a bundle, the pyInstaller bootloader
            # extends the sys module by a flag frozen=True and sets the app
            # path into variable _MEIPASS'.
            self.BASE_DIR =os.getcwd()
        else:
            self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.filename_config = os.path.join(self.BASE_DIR, 'yaml','setting.yaml')
        try:
            if not os.path.exists(self.filename_config):
                with open(self.filename_config, 'w', encoding='utf-8') as yaml_config_file:
                    pass
            with open(self.filename_config, 'r', encoding='utf-8') as yaml_config_file:
                self.config = yaml.load(yaml_config_file)
                self.config = {} if self.config is None else self.config
        except Exception as e:
            exeption_print(e)

    @property
    def version(self):
        return self.config

    @version.setter
    def version(self, value):
        # self.config['version'] = value
        self.config[datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]=value
        with open(self.filename_config, "w", encoding='utf-8') as f:
            yaml.dump(self.config, f,default_flow_style=False)



