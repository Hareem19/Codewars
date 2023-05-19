def accum(s):
    i=0
    List=[]
    for i in range(len(s)):
        List.append((s[i].upper() + s[i].lower() * i))
    return "-".join(List)
    # your code
    accum("abcd") -> "A-Bb-Ccc-Dddd"
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# def accum(s):
#     result = []
#     for i in range(len(s)):
#         result.append(s[i].upper() + s[i].lower() * i)
#     return "-".join(result)
print(accum("cat"))
