def analyzer(strr):
    vowels=0
    consonants=0
    numericals=0
    special_char=0
    vowel_set = "aeiouAEIOU"
    consonant_set = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for ch in strr:
        if ch.isnumeric():
            numericals+=1
        elif ch in vowel_set:
            vowels+=1
        elif ch in consonant_set:
            consonants+=1
        else:
            special_char+=1
    print("vowels:",vowels)
    print("consonants: ",consonants)
    print("numericals: ",numericals)
    print("special chacters: ",special_char)
    
strr=input("enter the string: ")
analyzer(strr)
print(strr[::-1])