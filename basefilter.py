from pathlib import Path
import os
from utils import write_classification_to_file
import abc
from random import choice

class BasicFilter(abc.ABC):

    # def train(self, path_to_mails: str):
    #     pass

    # @abc.abstractmethod
    def decide_class():
        pass

    def universal_test(self, path_to_mails: str):
        path_to_mails = Path(path_to_mails)

        email_classes = dict()

        # for every file in a directory
        for a_file in os.listdir(path_to_mails):
            # if it isn't a special file
            if (a_file.find('!') == 0):
                pass
            # categorize email as write_class
            else:
                email_classes[a_file] = self.decide_class
        
        # write that down to a !prediction.txt file
        write_classification_to_file(path_to_mails / "!prediction.txt", email_classes)

    # @abc.abstractmethod
    def test(self, path_to_mails):
        pass

