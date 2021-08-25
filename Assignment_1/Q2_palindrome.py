#Write a python script to take input from user (String) and to verify it whether string is Symmetrical or Palindrome.
s=input()
if s == s[::-1]:#"[::-1]"is used to reverse string  
    print('string is palindrome')
else:
    print('string is not palindrome')