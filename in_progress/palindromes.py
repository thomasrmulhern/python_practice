def is_pal1(word):
    '''
    check if string is palindrome reversing the whole word
    Examples:
    tacocat == True
    taco cat == True
    A Toyota! Race fast, safe car! A Toyota! == True
    soccer == False
    '''
    import re
    s_word = word.strip(' ').lower().replace(' ', '')
    s_word = re.sub(r'[^\w\s]','',s_word)
    if s_word == s_word[::-1]:
        print(word, 'IS a palindrome')
        return True
    else:
        print(word, 'is NOT a palindrome')
        return False

def is_pal2(word):
    '''
    check if string is palindrome only reversing the second half of the word
    Examples:
    tacocat == True
    taco cat == True
    A Toyota! Race fast, safe car! A Toyota! == True
    soccer == False
    '''
    import re
    s_word = word.strip(' ').lower().replace(' ', '')
    s_word = re.sub(r'[^\w\s]','',s_word)
    if len(s_word) % 2 == 0:
        if s_word[:(len(s_word)//2)] == s_word[(len(s_word)//2):][::-1]:
            print(word,  'IS a palindrome')
            return True
        else:
            print(word,  'is NOT a palindrome')
            return False
    else:
        if s_word[:((len(s_word)-1)//2)] == s_word[((len(s_word)-1)//2)+1:][::-1]:
            print(word, 'IS a palindrome')
            return True
        else:
            print (word, 'is NOT a palindrome')
            return False

def is_pal3(word):
    '''
    check if string is palindrome checking opposite character pairs for half the length of the string
    Examples:
    tacocat == True
    taco cat == True
    A Toyota! Race fast, safe car! A Toyota! == True
    soccer == False
    '''
    import re
    s_word = word.strip(' ').lower().replace(' ', '')
    s_word = re.sub(r'[^\w\s]','',s_word)
    if len(s_word) % 2 == 0:
        for _ in range(len(s_word)//2):
            for x,y in zip(s_word, s_word[::-1]):
                if x != y:
                    print(word, 'is NOT a palindrome')
                    return False
        print(word, 'IS a palindrome')
        return True
    else:
        for _ in range((len(s_word)-1)//2):
            for x,y in zip(s_word, s_word[::-1]):
                if x != y:
                    print(word, 'is NOT a palindrome')
                    return False
        print(word, 'IS a palindrome')
        return True

def is_pal3_refactor(word):
    '''
    check if string is palindrome checking opposite character pairs for half the length of the string
    Examples:
    tacocat == True
    taco cat == True
    A Toyota! Race fast, safe car! A Toyota! == True
    soccer == False
    '''
    import re
    s_word = word.strip(' ').lower().replace(' ', '')       # prep string
    s_word = re.sub(r'[^\w\s]','',s_word)                   # clean punctuation
    if len(s_word) % 2 == 0:
        for _ in range(len(s_word)//2) if len(s_word) % 2 == 0 and _ in range((len(s_word)-1)//2) if len(s_word) % 2 != 0:
            for x,y in zip(s_word, s_word[::-1])
                if x != y:
                    print(word, 'is NOT a palindrome')
                    return False
        print(word, 'IS a palindrome')
        return True
