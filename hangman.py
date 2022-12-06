import requests
import random
import string

WORDLIST_URL = "https://raw.githubusercontent.com/Tom25/Hangman/master/wordlist.txt"
ALLOWED_TURN = 10

def get_online_file():
    """
    This funtion gets a wordlist from web url.

    Returns:
        Return a list of string.
    """
    resp = requests.get(WORDLIST_URL)
    if resp.status_code == 200:
        return resp.text.split("\n")


def start_game():
    """
    This is the main funtion of this program  
    """

    print("[I] LODING WORDLIST FILE FROM SERVER...")
    list_of_word = get_online_file()
    print(f"[I] LODED {len(list_of_word)} WORDS FROM ONLINE WORDLIST")
    print("---" * 30)

    name = input("[I] Enter a name to start the game:- ")
    print(f"[-->] Welcome {name} to our guessing frind name game:- ")
    print("---" * 30)
    print("[NOTE] Try to guess the words in 10 attempts:- ")

    guessmade = ""
    turns = ALLOWED_TURN
    random_word = random.choice(list_of_word)
    valid_entry = string.ascii_lowercase

    while len(random_word) > 0:

        main_word = ""

        for letter in random_word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "

        if main_word == random_word:
            print("Yay you won!")
            break

        print(f"[I] Guess the words : {main_word}")
        guess = input("[I] Enter the guess:- ")

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print("[!] Please enter a valid input:- ")

        # below two lines gonna check the user guess is available in
        # random generated word or not and reduce the turns
        if guess not in random_word:
            turns = turns - 1

            # below code gonna represent the hangman status in status of
            # turns left
            if turns == 9:
                print("9 turns left:- ")
                print("---------------------------")
            elif turns == 8:
                print("8 turns left:- ")
                print("---------------------------")
                print("            o              ")
                print("            |              ")
            elif turns == 7:
                print("7 turns left:- ")
                print("---------------------------")
                print("           \o/             ")
                print("            |              ")
            elif turns == 6:
                print("6 turns left:- ")
                print("---------------------------")
                print("           \o/             ")
                print("            |              ")
                print("           / \             ")
            elif turns == 5:
                print("5 turns left:- ")
                print("---------------------------")
                print("           \o/             ")
                print("            |              ")
                print("           / \             ")
            elif turns == 4:
                print("4 turns left:- ")
                print("---------------------------")
                print("                 |         ")
                print("           \o/             ")
                print("            |              ")
                print("           / \             ")
            elif turns == 3:
                print("3 turns left:- ")
                print("---------------------------")
                print("                 |         ")
                print("                 |         ")
                print("           \o/             ")
                print("            |              ")
                print("           / \             ")
            elif turns == 2:
                print("2 turns left:- ")
                print("---------------------------")
                print("                 |         ")
                print("                 |         ")
                print("           \o/             ")
                print("            |              ")
                print("           / \             ")
            elif turns == 1:
                print("1 turns left:- ")
                print("---------------------------")
                print("                 |         ")
                print("                 |         ")
                print("           \o/   |         ")
                print("            |              ")
                print("           / \             ")
                print("Try harder you only get one chance in next you gonna die:- ")
            elif turns == 0:
                print("4 turns left:- ")
                print("---------------------------")
                print("                 |         ")
                print("                 |         ")
                print("           \o/___|(I am dead)       ")
                print("            |     (you killed me)         ")
                print("           / \    (with your wrong guess)          ")
                print(f"[+] The word was:= {main_word}")
                break

if __name__ == "__main__":
    start_game()
