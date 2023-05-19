def get_count(sentence):
    coun=0
    i=len(sentence)
    for i in sentence :
        if sentence[i]=="a" or "e" or "i" or "o" or "u":
            coun+=1
    return coun
get_count("hareem")