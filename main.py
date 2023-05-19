def get_count(sentence):
    count=0
    for i in len(sentence):
        if sentence[i]=="a" or "e" or "i" or "o" or "u":
            count+=1
    return count