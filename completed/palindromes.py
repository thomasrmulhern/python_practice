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
        print(word, 'is a palindrome')
    else:
        print(word, 'is not a palindrome')


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
            print(word,  'is a palindrome')
        else:
            print(word,  'is not a palindrome')
    else:
        if s_word[:((len(s_word)-1)//2)] == s_word[((len(s_word)-1)//2)+1:][::-1]:
            print(word, 'is a palindrome')
        else:
            print (word, 'is not a palindrome')
