class BinaryConfusionMatrix:

    def __init__(self, pos_tag="SPAM", neg_tag="OK"):
        # BinConMat
        self.tp = 0
        self.tn = 0
        self.fp = 0
        self.fn = 0

        # modifieble tags
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag

    def as_dict(self):
        '''ret dict of BinConMat'''
        return {"tp": self.tp, "tn": self.tn, "fp": self.fp, "fn": self.fn}

    def update(self, truth, prediction):
        '''update BinConMat'''
        # only error that COULD occur (that python hasnt acount for)
        def wrong_tag():
            raise ValueError("Truth or prediction don't corespond with your class tags.")

        # check what state we are in
        # if tags != outcomes raise error
        if prediction == self.pos_tag:
            if (prediction == truth):
                self.tp += 1
            elif (prediction != truth) and (truth == self.neg_tag):
                self.fp += 1
            else:
                wrong_tag()
        elif prediction == self.neg_tag:
            if (prediction == truth):
                self.tn += 1
            elif (prediction != truth) and (truth == self.pos_tag):
                self.fn += 1
            else:
                wrong_tag()
        else:
            wrong_tag()

    
    def compute_from_dicts(self, truth_dict: dict, pred_dict: dict):
        '''calls update on multiple outcomes from hashes'''
        truth_keys = truth_dict.keys()
        pred_keys = truth_dict.keys()

        for i in pred_keys:
            self.update(truth_dict[i], pred_dict[i])