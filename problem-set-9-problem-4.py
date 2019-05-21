# Module 6 - Problem Set No. 9 - Problem 4

"""
READ ALL INFORMATION CAREFULLY AND THEN READ IT AGAIN

IMPORTANT - PROVIDE AN IPO (Inputs, Processes, and Output) AT THE TOP OF 
EACH PROGRAM USING COMMENTS.

Morse code is a code where each letter of the English alphabet, each digit, 
and various punctuation characters are represented by a series of dots and 
dashes. The table in the morse-code.png image that is part of this repository 
shows part of the morse code conversions. Write a program that asks the user 
to enter a string, and then converts that string to Morse code.

HINTS
========================
- Use a loop to iterate through the inputted string going one letter a time.
- Use the statement below in your code. Each element in the list represents a 
  charecter from the sample Morse code chart provided in the problem. The 
  first element in the list is a space.
- So the letter 'A' or 'a' is in the list at position 13 and would be 
  morse_list[13].
- Use the string accumator pattern to concatenate all of the morese code 
  values together and display them at the end.
- There other ways to approach this problem.
- Solutions from the internet will not be accepted and a grade of zero for the 
  entire assignment will be entered

Annotated list - split over multiple lines - feel free to update as necessary

                  #     ,         .         0       1        2        3
morse_list = [' ', '--..--', '.-.-.-', '-----','.----', '..---', '...--',
                #4        5        6        7        8        9
                '....-', '.....', '-....', '--...', '---..', '----.',
                #A     B       C       D      E    F       G      H   
                '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
                #I     J       K      L       M     N     O      P
                '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
                #Q       R      S      T    U      V       W      X
                '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
                #Y       Z
                '-.--', '--..']
IPO
==========
INPUTS: 
PROCESSES: 
OUTPUTS: 

"""

def main():
    morse_list = [' ', '--..--', '.-.-.-', '-----', '.----', '..---', '...--',
                  '....-', '.....', '-....', '--...', '---..', '----.',
                  '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
                  '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
                  '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
                  '-.--', '--..']

    char_list = [' ', ',', '.', '0', '1', '2', '3',
                 '4', '5', '6', '7', '8', '9',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z']

    finalMorse_list = []
    sequence = input('Enter any sequence of lowercase letters and/or numbers: ')

    for i in sequence:
        character = i
        for j in char_list:
            if character == j:
                x = char_list.index(j)
                finalMorse_list.append(morse_list[x])

    print(finalMorse_list)


main()