'''
File: Counter.py
Author: M. Viernes
Description: Analyzes the text file and counts the percentages of char usage in the whole document.
'''

import string


# feeds the txt file for counting the percentage of each char through iteration.
def char_percentage_analyzer(text_file):
    """
    Returns the result of reading a text file through counting
    and calculating each char percentage that constitutes the text.
    """
    with open(text_file, "r", encoding="utf-8") as file_reader:
        txt = file_reader.read()
        text_len = len(txt)
    print("The file has a text size of ", text_len)
    
    # iterate each standard ascii chars 
    total = 0
    ascii_letters = string.ascii_letters + " "
    for letter in ascii_letters: 
        char_percentage = _analyze_charintext(txt, letter)
        total += char_percentage
        _print_percentage(letter, char_percentage)
    print("The total percentage of text: %04.2f%%" % total)
    print("The remaining non word character: %04.2f%%" % (100 - total))


def _analyze_charintext(text_file, letter):
    """
    Returns the char percentage of each ascii chars through comparison of each letters in text file.
    """
    count = 0
    text_count = len(text_file)
    for i in range(text_count):
        if text_file[i] == letter:
            count += 1
    return (count/text_count) * 100


def _print_percentage(letter, char_percentage):
    print("Character \'%s\' percentage: %04.2f%%" % (letter, char_percentage) )
    

def main():
    try:    
        txt = input("Enter the text file: ")
        txt_input = "textfile.txt" if txt == "" else txt
        char_percentage_analyzer(txt_input)
    except Exception as e:
        print("Use an existing file <name.txt>")

if __name__ == '__main__':
    main()
