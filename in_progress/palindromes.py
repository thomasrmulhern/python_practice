def is_pal1(word):
    '''
    (str) -> bool
    Check if string is palindrome reversing the whole word
    >>> is_pal1('tacocat')
    True
    >>> is_pal1('A Toyota! Race fast, safe car! A Toyota!')
    True
    is_pal1('soccer')
    False
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
    (str) -> bool
    Check if string is palindrome only reversing the second half of the word
    >>> is_pal2('tacocat')
    True
    >>> is_pal2('A Toyota! Race fast, safe car! A Toyota!')
    True
    is_pal2('soccer')
    False
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
    (str) -> bool
    Check if string is palindrome comparing opposite character pairs for half the length of the string
    >>> is_pal3('tacocat')
    True
    >>> is_pal3('A Toyota! Race fast, safe car! A Toyota!')
    True
    is_pal3('soccer')
    False
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
    (str) -> bool
    Check if string is palindrome comparing opposite character pairs for half the length of the string
    >>> is_pal3('tacocat')
    True
    >>> is_pal3('A Toyota! Race fast, safe car! A Toyota!')
    True
    is_pal3('soccer')
    False
    '''
    import re
    s_word = word.strip(' ').lower().replace(' ', '')       # prep string
    s_word = re.sub(r'[^\w\s]','',s_word)                   # clean punctuation
    i = 0                                                   # init first of two index points
    j = len(s_words)                                        # init second of two index points
    while i < j and s[i] == s[j]:                           # compare indexed string chars until index points have crossed
        i = i + 1
        j = j - 1
    if i < j:                                               # if index points have crossed, sting is a palindrome
        print (word, 'IS a palindrome')
    else:                                                   # if the loop breaks prior it is not a palindrome
        print(word, 'is NOT a palindrome')
