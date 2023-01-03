import os

class Corpus:
    def __init__(self, fpath):
        self.path=fpath

    def emails(self):
        for file_name in os.listdir(self.path):
            if file_name[0]!='!':
                with open(os.path.join(self.path, file_name),'r',encoding='utf-8') as f:
                    text=f.read()
                yield file_name, text