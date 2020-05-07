import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    if data.get(w) != None:
        return data[w]
    else:
        if len(get_close_matches(w,data.keys())) > 0:
            userReply = input("Did you mean %s ? Enter Yes or No : " % get_close_matches(w,data.keys())[0])
            if userReply == "Yes" or userReply == "yes" or userReply == "Y":
                return data[get_close_matches(w,data.keys())[0]]
            elif userReply == "No" or userReply == "no" or userReply == "N":
                return "Sorry couldn't find any other words :("
            else:
                return "We didn't understand your reply !"
        else:
            return "Word doesn't exist in the dictionary. Please check again !"


print("\n\n\t\tWelcome to Geetansh's Dictionary !!!")
choice = "Yes"
while choice == "Yes":
    print("\n\n")
    word = input("Enter the word: ")
    word = word.lower()
    output=translate(word)
    if type(output) == list:
        c = 1
        for item in output:
            print(str(c) + ". " + item )
            c = c+1
    else:
        print("1. "+ output)
    choice = input("\nWant to search for more words ? Enter Yes or No : ")

