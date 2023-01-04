import os
from utils import (write_classification_to_file)


def create_prediction(path_to_mails: str, spam_words: list):
    
    email_types = dict()

    for a_file in os.listdir(path_to_mails):
            # if it isn't a special file
            if (a_file.find('!') == 0):
                pass

            # categorize email as ham / spam
            else:
                with open((path_to_mails / a_file), 'r', encoding='utf-8') as cur_mail:
                    msg = cur_mail.read()
                    msg = msg.lower()

                    for word in spam_words:
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