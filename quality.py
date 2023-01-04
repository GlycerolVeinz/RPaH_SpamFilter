from utils import read_classification_from_file
from confmat import BinaryConfusionMatrix
from pathlib import Path

def quality_score(tp: int, tn: int, fp: int, fn: int):
    '''computes quality based on equation'''
    return (tp + tn) / (tp + tn + 10*fp + fn)

def compute_quality_for_corpus(corpus_dir):
    '''computes quality for corpus of emails'''
    # set path
    corpus_dir = Path(corpus_dir)
    
    # create hashes for truth and prediction
    truth_hash = read_classification_from_file(corpus_dir / "!truth.txt")
    prediction_hash = read_classification_from_file(corpus_dir / "!prediction.txt")

    # compute BinConMat
    current_corpus = BinaryConfusionMatrix()
    current_corpus.compute_from_dicts(truth_hash, prediction_hash)

    # ret quality of corpus
    return quality_score(current_corpus.tp, current_corpus.tn, current_corpus.fp, current_corpus.fn)
    
