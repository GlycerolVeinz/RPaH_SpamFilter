import os
from utils import read_classification_from_file
from confmat import BinaryConfusionMatrix
def quality_score(tp, tn, fp, fn):
    q=(tp+tn)/(tp+tn +10*fp +fn)
    return q
def compute_quality_for_corpus(corpus_dir):
    for file_name in os.listdir(corpus_dir):
        if file_name=='!truth.txt':
            truth_dict=read_classification_from_file(os.path.join(corpus_dir, file_name))
        if file_name=='!prediction.txt':
            pred_dict=read_classification_from_file(os.path.join(corpus_dir, file_name))
    pchel=BinaryConfusionMatrix("SPAM","OK")
    pchel.compute_from_dicts(truth_dict, pred_dict)
    matrix=pchel.as_dict()
    res=quality_score(matrix['tp'], matrix['tn'], matrix['fp'], matrix['fn'])
    return res
        