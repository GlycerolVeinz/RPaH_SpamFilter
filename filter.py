import os
from pathlib import Path
from utils import write_classification_to_file

class MyFilter():

    def __init__(self):
        self.spamwords = ["adult", "prince", "money", "cash", "girl", "women", "mom", "xxx", "lonely", "porn", "treasure", "lottery", "special offer", "karma", "prediction", "savings", "cheating", "order now", "weight loss", "hot"]

    def train(self, path_to_mails):
        pass

    def test(self, path_to_mails):
        # creates !prediction.txt in path_to_mails
        # implement as last fce
        # will run through the mails, and search for key-words that train() has found
        path_to_mails = Path(path_to_mails)
        email_classes = dict()

        for a_file in os.listdir(path_to_mails):
            # if it isn't a special file
            if (a_file.find('!') == 0):
                pass
            # categorize email as write_class
            else:
                with open(os.path.join(path_to_mails, a_file), 'r', encoding='utf-8') as fp:
                    msg = fp.read()
                    msg = msg.lower()

                    for word in self.spamwords:
                        if msg.find(word) !=-1:
                            def decide_class():
                                return "SPAM"
                            break
                        else:
                            def decide_class():
                                return "OK"
                    email_classes[a_file] = decide_class()

                    write_classification_to_file(os.path.join(path_to_mails, "!prediction.txt"), email_classes)
