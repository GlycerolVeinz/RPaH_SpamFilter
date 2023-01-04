
def read_spamwords():
    '''create list of spamwords from a spamwords.txt file'''
    with open("./spamwords.txt", "r", encoding="utf-8") as sp_file:
        # read whole file, then split on "new line"
        sp_words = sp_file.read()
        sp_words = sp_words.split("\n")
    return sp_words
    
def read_classification_from_file(fpath):
    '''read types of emails from a file'''
    ndict = dict()
    with open(fpath, 'r', encoding='utf-8') as f:
        for line in f:
            s = line.split()
            ndict[s[0]] = s[1]

    return ndict

def write_classification_to_file(types_file: str, email_types: dict):
    '''writes down email types to a file'''
    with open(types_file, mode='w', encoding='utf-8') as a_file:

        for i in email_types.keys():
            a_file.write(f"{i} {email_types[i]}\n")
