from pathlib import Path
from simplefilters import BasicFilter

class MyFilter(BasicFilter):

    def train(self, path_to_mails: str):
        # path to mails need to have !truth.txt
        # need to check if key-words appear in mails (like porn, african prince etc.)
        # should create workflow for test()

        return super().train(path_to_mails)


    def test(self, path_to_mails):
        # creates !prediction.txt in path_to_mails
        # implement as last fce
        # will run through the mails, and search for key-words that train() has found
        return super().test(path_to_mails)
