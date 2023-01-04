from utils import read_spamwords
from prediction import create_prediction
from shutil import rmtree
from pathlib import Path

class MyFilter:
    '''spam-filter that searches for spam-words, to decide email type'''
    def __init__(self):
        self.spamwords = read_spamwords()

    def train(self, path_to_mails):
        #  our spfilter doesn't learn or tarin itself
        pass

    def test(self, path_to_mails: str):
        '''creates !prediction.txt in path_to_mails'''
        create_prediction(path_to_mails, self.spamwords)


if __name__ == "__main__":

    from quality import compute_quality_for_corpus
    import simplefilters
    CORPUS_DIR = "./spam-data-12-s75-h25(1)/1/"
    CORPUS_DIR = Path(CORPUS_DIR)

    def qute_fltr(fltr):
        fltr.test(CORPUS_DIR)
        print(compute_quality_for_corpus(CORPUS_DIR))
        rmtree((CORPUS_DIR / "!prediction.txt"), ignore_errors=True)

    filtr = MyFilter()
    qute_fltr(filtr)

    filtr = simplefilters.NaiveFilter()
    qute_fltr(filtr)

    filtr = simplefilters.ParanoidFilter()
    qute_fltr(filtr)

    filtr = simplefilters.RandomFilter()
    qute_fltr(filtr)

    


    