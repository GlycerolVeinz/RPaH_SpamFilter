from pathlib import Path
import os
from utils import write_classification_to_file
import abc

class BasicFilter(abc.ABC):

    def train(self, path_to_mails: str):
        pass

    def universal_test(self, path_to_mails: str, write_class: str):
        path_to_mails = Path(path_to_mails)

        email_classes = dict()

        # for every file in a directory
        for a_file in os.listdir(path_to_mails):
            # if it isn't a special file
            if (a_file.find('!') == 0):
                pass
            # naivly categorize email as "OK"
            else:
                email_classes[a_file] = "OK"
        
        # write that down to a !prediction.txt file
        write_classification_to_file(path_to_mails / "!prediction.txt", email_classes)

    @abc.abstractmethod
    def test(self, path_to_mails):
        pass

class NaiveFilter(BasicFilter):
    
    def test(self, path_to_mails):
        self.universal_test(path_to_mails, "OK")
