import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def trans(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]  
    elif word.upper() in data:
        return data[word.upper()]      
    elif len(get_close_matches(word,data.keys())) > 0 :
        yn = input("Did you mean %s instead ? press Y if yes...N if no : " %  get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "please try again..!!" 
        else:
            return "we could not read your character..."       
    else:
        return "The word does not exist....Please try again... "    

word = input("enter the word : ")
out = trans(word)

if type(out) == list :
    for i in out :
        print(i)
else:
    print(out)        