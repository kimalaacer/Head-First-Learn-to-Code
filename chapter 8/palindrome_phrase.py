# this is to check a list os word if they are palindromes.

# We are using RegEx to to strip the phrase from whitespaces and punctuations.
import re
phrase='a man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: panama.'
word=re.sub(r'\W','',phrase)
def is_palindrome(word):
    if len (word)<=1:
        return True
    else:
        if word[0]==word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False
print(phrase, is_palindrome(word))
