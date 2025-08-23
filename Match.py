def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("List:\n", lst)
    return ctr
list = ['abc', 'cfc', 'xyz', 'aba', '1221'] 
print("The number of words having first character and last character same are:", list)

    
