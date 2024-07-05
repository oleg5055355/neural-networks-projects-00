import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def dictionary(word):
    word=word.lower()
    if word in data:
        return (data[word])
    elif word.title() in data:
        return (data[word.title()])
    elif word.upper() in data:
        return (data[word.upper()])
    elif len(get_close_matches(word,data.keys()))>0:
        print("did you mean %s    "%get_close_matches(word,data.keys())[0])
        tell=input("press y for yes or n for no")
        if tell == "y":
            return (data[get_close_matches(word,data.keys())[0]])
        elif tell == "n":
            return ("error in word")
        else:
            return("word not found")
    else:
        print("word not found")

word=input("Enter word")
result=dictionary(word)

if type(result)== list:
    for item in result:
        print(item)
else:
    print(result)











