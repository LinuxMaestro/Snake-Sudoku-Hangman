import random
from Hangman.word_list import words, chances, welcome_message

# GET A WORD, THAT WILL BE AN ANSWER
def getWord():
    word = random.choice(words)
    return word


def get_dict_answer(answer):
    dict_answer = {}
    for i in range(len(answer)):
        if answer[i] in dict_answer:
            dict_answer[answer[i]].append(i)
        else:
            dict_answer[answer[i]] = [i]
    return dict_answer


def clear():
    print("/n"*200)

# PLAY
def play():
    answer = getWord()
    n = len(answer)
    dict_answer = get_dict_answer(answer)
    i = 6
    curr_answer = ["_"] * n
    dict_curr = {}
    print(welcome_message)
    while i > -1:
        print(*curr_answer)
        print(chances[i], i+1)
        print(f"Inputs Tried are ", *dict_curr.keys())
        ask = input()
        m = len(ask)
        if m not in [1, n]:
            print("Your input must be either the guess of the word or a letter")
            continue
        if m == 1:
            if not ask.isalpha():
                print("INVALID INPUT, PLEASE PUT ALPHABETICAL VALUES!")
                continue
            if ask in dict_curr:
                print("Input Already Tried")
                continue
            elif ask in dict_answer:
                print(f"Congrats! {ask} is a right choice!")
                dict_curr[ask] = 1
                changes = dict_answer[ask]
                for change in changes:
                    curr_answer[change] = ask
            else:
                i -= 1
                dict_curr[ask] = 1
                print("Wrong...")
        else:
            if ask in dict_curr:
                print("Input Already Tried")
                continue
            elif ask == answer:
                print("Success, You have made it!")
                break
            else:
                print("Wrong.... Try again")
                i -= 1
                dict_curr[ask] = 1
    print(f"The correct answer was \"{answer}\"")


def main():
    yes = 1
    while yes:
        play()
        ask = input("Would you like to play again? y or n")
        if ask == 'n':
            break

if __name__ == "__main__":
    main()


