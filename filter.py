import email
from email.message import EmailMessage
import os
from pathlib import Path
from basefilter import BasicFilter

class MyFilter(BasicFilter):

    def __init__(self):
        self.spamwords = ["Adult", "Prince", "Money", "Cash", "Girl", "Women", "Mom", "Xxx", "Lonely", "Porn", "Treasure", "Lottery", "Special Offer", "Karma", "Prediction", "Savings", "Cheating", "Order Now", "Weight Loss", "Hot"]

    def train(self, path_to_mails):
        path_to_mails = Path(path_to_mails)
        pass

    def test(self, path_to_mails):
        # creates !prediction.txt in path_to_mails
        # implement as last fce
        # will run through the mails, and search for key-words that train() has found
        path_to_mails = Path(path_to_mails)

        for a_file in os.listdir(path_to_mails):
            # if it isn't a special file
            if (a_file.find('!') == 0):
                pass
            # categorize email as write_class
            else:
                msg = email.message_from_file(a_file)
                body = msg.get_body()

                for word in self.spamwords:
                    if body.find(word.lower) !=-1 or body.find(word.upper) !=-1 or body.find(word) !=-1:
                        def decide_class():
                            return "SPAM"
                    else:
                        def decide_class():
                            return "OK"

        self.universal_test(path_to_mails)


        # return super().test(path_to_mails)