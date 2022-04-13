from collections import Counter

try:
    with open("test.txt", "rt") as f:
        wordFile = f.read()
        formattedFileOutput = f"Total Words: {len(wordFile.split())} \n \n"
        # Count the occurences of each word into dictionary
        dictOfWordOccur = Counter(wordFile.split())

        # Print line for each word and their occurences
        for word in dictOfWordOccur:
            formattedFileOutput = (
                formattedFileOutput + f"{word}: {dictOfWordOccur[word]} \n"
            )

        try:
            # Write the completed output to a new file .words, overwrite if it exsists
            with open(".words", "w") as file:
                file.write(formattedFileOutput)
        except IOError:
            print(f"Problem writing to output file")

        print(formattedFileOutput)

except IOError:
    print(f"Problem opening file")
