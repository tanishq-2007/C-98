from fileinput import filename


def countWordFromFile():
    fileName= input('Enter the File name: ')
    numberOfWords=0
    file= open(fileName,'r')
    for line in file:
        words= line.split()
        numberOfWords=numberOfWords+len(words)
    print('number of words: ')
    print(numberOfWords)
countWordFromFile()