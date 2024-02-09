#!/usr/bin/env python3
"""Understanding dictionaries """

# Marvel character information    
marvelchars= {
    "Starlord":
        {"real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenaline"}
                }

# Function to print the character's information in the desired format
def print_character_info(char_name, char_stat, value):
    print(f"{char_name}'s {char_stat} is: {value}")

# Prompt the user to enter a character name
char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): ").capitalize()

# Prompt the user to enter a character attribute
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ").lower()

# Check if the entered character exists in the dictionary
if char_name in marvelchars:
    # Check if the entered statistic exists for the character
    if char_stat in marvelchars[char_name]:
        # Retrieve the value of the entered statistic for the character
        value = marvelchars[char_name][char_stat]
        # Print the character's information
        print_character_info(char_name, char_stat, value)
    else:
        print("Invalid statistic specified.")
else:
    print("Invalid character name specified.")

