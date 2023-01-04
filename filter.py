import os
from pathlib import Path
from utils import (write_classification_to_file, read_spamwords)


class MyFilter:

    def __init__(self):
        self.spamwords = read_spamwords()

    def train(self, path_to_mails):
        pass

    def test(self, path_to_mails):
        # creates !prediction.txt in path_to_mails
        # implement as last fce
        path_to_mails = Path(path_to_mails)
        email_types = dict()

        for a_file in os.listdir(path_to_mails):
            # if it isn't a special file
            if (a_file.find('!') == 0):
                pass
            # categorize email as ham / spam
            else:
                with open((path_to_mails / a_file), 'r',
                          encoding='utf-8') as fp:
                    msg = fp.read()
                    msg = msg.lower()

                    for word in self.spamwords:
                        if msg.find(word) != -1:

                            def decide_class():
                                return "SPAM"

                            break
                        else:

                            def decide_class():
                                return "OK"

                    email_types[a_file] = decide_class()

                    write_classification_to_file(
                        (path_to_mails / "!prediction.txt"), email_types)
