def is_isogram(string):
    #your code here
    string1=string.lower()
    for char in string1:
        if string1.count(char)>1:
           return False
    return True
print(is_isogram("vYBwSDPKOYJiZTCLaYZmIYfwIiIbRuIqmNbmEo"))