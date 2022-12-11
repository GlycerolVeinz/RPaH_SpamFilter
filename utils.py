

def read_classification_from_file(class_file):
    '''reads classification of mail from a file'''
    email_types = dict()
    
    with open (class_file, mode ='r', encoding = 'utf-8') as a_file:

        #infinite loop until EOF (here its "")
        while True:
            current_line = a_file.readline()
            if (current_line == ''):
                break

            #  if not EOF split email and c=its classification
            tmp_string_split = current_line.split(" ")
            # del \n on the ends of lines
            tmp_string_split[1] = tmp_string_split[1].replace('\n', '')
            # put everything in to hash
            email_types[tmp_string_split[0]] = tmp_string_split[1]
            tmp_string_split = list()

    return email_types


def write_classification_to_file(class_file: str, email_types: dict):

    with open(class_file, mode='w', encoding= 'utf-8') as a_file:

        for i in email_types.keys():
            a_file.write(f"{i} {email_types[i]}\n")



if __name__ == "__main__":
    
    a = {"email100" : "OK", "email101" : "SPAM"}
    write_classification_to_file("lol.txt", a)
    print(read_classification_from_file("lol.txt"))
    