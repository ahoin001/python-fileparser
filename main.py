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

my_parser.add_argument(
    "-o",
    dest="desired_file_output_name",
    help="Provide name you want for the output file instead of .words",
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

        # If user pprovided a file name with -o arg, use that name for new file being written
        if args.desired_file_output_name:

            print(f"Creating new output file named: {args.desired_file_output_name}")

            # Write the completed output to a new file .words, overwrite if it exsists
            with open(f"{args.desired_file_output_name}", "w") as file:
                file.write(formattedFileOutput)
        else:
            # If no name given by user, create file as .words
            with open(".words", "w") as file:
                file.write(formattedFileOutput)

    except IOError:
        print(f"Problem writing to output file")
        print(formattedFileOutput)

