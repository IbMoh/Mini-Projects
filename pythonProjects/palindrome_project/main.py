import helpers.loader as loader

def is_this_a_palindromes(wordList):
    palindromes_list = []
    for x in wordList:
        if x == x[::-1] and len(x) > 1:
            palindromes_list.append(x)

    print(f"words found: {len(palindromes_list)}")
    print(*palindromes_list, sep='\n')

def main():
    file = 'dictionary.txt'
    words = loader.read_file(file)
    is_this_a_palindromes(words)

if __name__ == '__main__':
    main()
