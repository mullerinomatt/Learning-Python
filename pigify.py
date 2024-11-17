"""  
A collection of functions to support the translation of words into Pig Latin.

This module contains two functions.  The first function searchs for the location of the 
first vowel.  The second function uses this as a helper to perform the conversion.

Author: Matthew J. Muller
Date: 11/17/2024
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns -1 if there are no vowels.
    
    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.
    
    Examples: 
        first_vowel('hat') returns 1
        first_vowel('grrm') returns -1
        first_vowel('sky') returns 2
        first_vowel('year') returns 1
    
    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """
    result=len(s)
    if 'a' in s:      
        result=introcs.find_str(s,'a')
    if 'e' in s and introcs.find_str(s,'e') < result:
        result= introcs.find_str(s,'e')
    if 'i' in s and introcs.find_str(s,'i')<result:
        result=introcs.find_str(s,'i')
    if 'o' in s and introcs.find_str(s,'o')<result:
        result=introcs.find_str(s,'o')
    if 'u' in s and introcs.find_str(s,'u')<result:
        result= introcs.find_str(s,'u')
    if 'y'in s[1:] and introcs.find_str(s[1:],'y')<result:
        result=introcs.find_str(s[1:],'y')+1 

    return -1 if result==len(s) else result


def pigify(s):
    """
    Returns a copy of s converted to Pig Latin
    
    Pig Latin is childish encoding of English that adheres to the following rules:
    
    1.  The vowels are 'a', 'e', 'i', 'o', 'u', as well as any 'y'
        that is not the first letter of a word. All other letters are consonants.
        
        For example, 'yearly' has three vowels  ('e', 'a', and the last 'y') 
        and three consonants (the first 'y', 'r', and 'l').
    
    2.  If the English word begins with a vowel, append 'hay' to the end of the word 
        to get the Pig Latin equivalent. For example, 'ask 'askhay' and 'use' becomes 
        'usehay'.
    
    3.  If the English word starts with 'q', then it must be followed by'u'; move 
        'qu' to the end of the word, and append 'ay'.  Hence 'quiet' becomes
        'ietquay' and 'quay' becomes 'ayquay'.
    
    4.  If the English word begins with a consonant, move all the consonants up to 
        the first vowel (if any) to the end and add 'ay'.  For example, 'tomato' 
        becomes 'omatotay', 'school' becomes 'oolschay'. 'you' becomes 'ouyay' and 
        'ssssh' becomes 'sssshay'.
    
    Parameter s: the string to change to Pig Latin
    Precondition: s is a nonempty string with only lowercase letters. If s starts with
    'q', then it starts with 'qu'.
    """

    #begins with a vowel
    if 'a' in s[0] or 'e' in s[0] or 'i' in s[0] or 'o' in s[0] or 'u' in s[0]:
        return s + 'hay'
    
    #begins with q
    if s[0]== 'q':
        return (s[2:] + s[0:2] + 'ay')
    
    #begins with consonant and has a vowel
    if ('a' not in s[0] or 'e' not in s[0] or 'i' not in s[0] or 'o' not in s[0] or 'u' not in s[0]) and first_vowel(s)>0:
        return (s[first_vowel(s):] + s[:first_vowel(s)] + 'ay')

    #begins with consonant and has no vowel
    if ('a' not in s[0] or 'e' not in s[0] or 'i' not in s[0] or 'o' not in s[0] or 'u' not in s[0]) and first_vowel(s)<0:
        return (s + 'ay')
