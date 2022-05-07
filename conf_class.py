import os


class Config:

    def __init__(self):
        self.option_one = None
        self.option_two = None
        self.option_three = None

    def get_options(self):
        self.option_one = os.environ.get('ONE', 1)
        self.option_two = os.environ.get('TWO', 2)
        self.option_three = os.environ.get('THREE', 3)


########################################################################################################################

# In another file:
"""
from ... import Config

class LocalMockConfig(Config):

    def get_options(self):
        self.option_one = 777
        self.option_two = 888
        self.option_three = 999


conf_obj = LocalMockConfig()  
"""
