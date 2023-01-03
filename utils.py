def read_classification_from_file(fpath):
    dict={}
    with open(fpath,'r',encoding='utf-8') as f:
        for line in f:
            s = line.split()
            dict[s[0]]=s[1]
    return dict

# def write_classification_to_file(class_file: str, email_types: dict):
    
#     with open(class_file, mode='w', encoding= 'utf-8') as a_file:

#         for i in email_types.keys():
#             new_line = '{} {}\n'.format(i, email_types[i])
#             a_file.write(new_line)

def write_classification_to_file(class_file: str, email_types: dict):

    with open(class_file, mode='w', encoding= 'utf-8') as a_file:

        for i in email_types.keys():
            a_file.write(f"{i} {email_types[i]}\n")



