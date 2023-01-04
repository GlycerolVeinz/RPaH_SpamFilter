import os
from pathlib import Path


class Corpus:

    def __init__(self, emails_path: str):
        self.emails_path = Path(emails_path)

    def emails(self):
        '''generator of files in a directory'''
        # for every file in a directory
        for a_file in os.listdir(self.emails_path):
            # if it isn't a special file
            if (a_file.find('!') == 0):
                pass
            else:
                email_name = str()
                email_body = str()
                current_line = str(" ")

                path_to_read = self.emails_path / a_file
                # reads a file line by line
                with open(path_to_read, mode='r', encoding='utf-8') as o_file:
                    while (current_line != ''):
                        current_line = o_file.readline()
                        email_body += current_line

                email_name = a_file
                yield (email_name, email_body)