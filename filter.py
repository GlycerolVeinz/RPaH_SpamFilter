import os
from pathlib import Path
from utils import (write_classification_to_file, read_spamwords)
from prediction import create_prediction


class MyFilter:

    def __init__(self):
        self.spamwords = read_spamwords()

    def train(self, path_to_mails):
        #  our spfilter doesn't lear or tarin itself
        pass

    def test(self, path_to_mails:str):
        '''creates !prediction.txt in path_to_mails'''
        create_prediction(path_to_mails, self.spamwords)
