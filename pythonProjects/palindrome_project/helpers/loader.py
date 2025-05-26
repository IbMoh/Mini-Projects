import sys

def read_file(file):
    word_list = []
    try:
        with open(file,'r') as r_file:
            line = r_file.read().strip().split('\n')
            for x in line:
                word_list.append(x.lower())
    
    except IOError as e:
        print(f"An Error occured when reading {file} {e}.")
        sys.exit(1)
    
    return word_list