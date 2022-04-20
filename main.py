from collections import Counter

# Used to take arguments from command line
import sys
import argparse

# Create the argparser (Easily constructs command line interface)
my_parser = argparse.ArgumentParser(
    description="Input a file and and recieve parsed data from it"
)

# Add the arguments or flags for user to input

my_parser.add_argument(
    "users_file", metavar="users_file", type=str, help="the file you want parsed"
)

# Execute the parse_args() method. Args now gives access to arguments we created before
args = my_parser.parse_args()

user_file = args.users_file

# print(user_file)

with open(user_file, "rt") as f:
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

