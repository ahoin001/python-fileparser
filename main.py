# #if the file is in the same directory
from collections import Counter
from isort import file


def sayHello():
    print("wow")


# sayHello()

# with statement closes file when block of code is finished
with open("test.txt", "rt") as f:
    wordFile = f.read()

# 1 Count Number of words in file

wordsTotal = len(wordFile.split())

print("==========================================")
print(f"There are {wordsTotal} words in this file")

# 2 List all words in the file
print("==========================================")
print(f"All words in file: {wordFile.split()}")


# 3 Count how many times each word appears in list Using Counter, returns dictionary for how many times each item occured
print("==========================================")
print(
    f"Using Counter, occurence of each item in list returned as dictionary: {Counter(wordFile.split())}"
)

appleRepeat = Counter(wordFile.split())["apple"]
print(f"The word apple occured {appleRepeat} times")

print("==========================================")

# 4 Iterate dictionary to format the output for the file we will make
dictOfWordOccur = Counter(wordFile.split())
formattedFileOutput = ""

for word in dictOfWordOccur:
    formattedFileOutput = formattedFileOutput + f"{word}: {dictOfWordOccur[word]} \n"

print(formattedFileOutput)

# 5 Write the Content to file
with open("words", "w") as file:
    file.write(formattedFileOutput)
