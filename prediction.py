import os
from pathlib import Path
from utils import (write_classification_to_file)

spam_tag = "SPAM"
ham_tag = "OK"

def create_prediction(mails_path: str, spam_words: list):
    # make os universal paths
    mails_path = Path(mails_path)
    prediction_path = (mails_path / "!prediction.txt")

    # pre-gen lists and dicts
    email_types = dict()
    emails_list = os.listdir(mails_path)

    # for every email in path to mails
    for cur_mail in email_types:
        cur_mail_path = (mails_path / cur_mail)

        # if it isn special file, skip it
        if (cur_mail.find('!') == 0):
            continue

        # categorize email as ham / spam
        with open(cur_mail_path, 'r', encoding='utf-8') as opened_mail:
            msg = opened_mail.read()
            msg = msg.lower()

            for word in spam_words:
                if msg.find(word) != -1:
                    decide_type = spam_tag

                else:
                    decide_type = ham_tag

            email_types[cur_mail] = decide_type

            write_classification_to_file(prediction_path, email_types) 