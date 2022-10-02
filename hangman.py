from random import randint

print("H A N G M A N", "\n")
secret_words_list = ["python", "java", "swift", "javascript"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

win_score = 0
lost_score = 0


def menu():
    settings = ["play", "results", "exit"]
    while True:
        settings_input = str(
                        input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'))
        if settings_input in settings:
            if settings_input == "play":
                main()
                continue
            elif settings_input == "results":
                print("You won: {0} times \n You lost: {1} times".format(win_score, lost_score))
                continue
            elif settings_input == "exit":
                break
            else:
                return False


def main():
    attempt = 8
    hangman_word = [i for i in secret_words_list[randint(0, len(secret_words_list) - 1)]]
    hidden_hang_word = ["-" for _ in hangman_word]
    letter_input = str
    guessed_letters_list = []
    while attempt != 0:
        print("".join(hidden_hang_word))
        letter_input = str(input("Input a letter: "))
        if len(letter_input) != 1:
            Exception(print("Please, input a single letter."))
        elif letter_input not in alphabet:
            Exception(print("Please, enter a lowercase letter from the English alphabet."))
        elif letter_input in guessed_letters_list:
            Exception(print("You've already guessed this letter."))
        else:
            guessed_letters_list.append(letter_input)
            index = []

            def hidden_letter_index_find():
                for i in range(len(hangman_word)):
                    if letter_input == hangman_word[i]:
                        index.append(i)
                return True

            if letter_input in hangman_word:
                hidden_letter_index_find()
                for i in index:
                    hidden_hang_word[i] = letter_input
            else:
                print("That letter doesn't appear in the word")
                attempt -= 1
            if hidden_hang_word.count("-") == 0:
                print("You guessed the word {0}! \n You survived!".format("".join(hidden_hang_word)))
                global win_score
                win_score += 1
                break
            elif hidden_hang_word.count("-") > 0 and attempt == 0:
                print("You lost!")
                global lost_score
                lost_score += 1
    print("Thanks for playing!")


if __name__ == '__main__':
    menu()
