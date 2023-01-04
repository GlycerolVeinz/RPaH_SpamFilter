
def read_spamwords():

    with open("./spamwords.txt", "r", encoding="utf-8") as sp_file:
        sp_words = sp_file.read()
        sp_words = sp_words.split("\n")
    return sp_words
    
def read_classification_from_file(fpath):
    ndict = dict()
    with open(fpath, 'r', encoding='utf-8') as f:
        for line in f:
            s = line.split()
            ndict[s[0]] = s[1]

    return ndict

def write_classification_to_file(class_file: str, email_types: dict):

    with open(class_file, mode='w', encoding='utf-8') as a_file:

        for i in email_types.keys():
            a_file.write(f"{i} {email_types[i]}\n")
