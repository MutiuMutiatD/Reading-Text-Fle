# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from cgitb import text
from fileinput import filename
from posixpath import split


def read_file_content(filename):
    # [assignment] Add your code here 
    with open('myfile.txt') as f:
        contents = f.read()
        print(contents)
        return contents



def word_count():
    text = read_file_content("myfile.txt")
    split_text = text.split()
    count = dict()
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
    return count
word_count()