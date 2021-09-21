#Generate a class 'Generator' to implement following methods:
import random
import string
class Genrator:
    def random_integerNumber(min, max):
        return random.randint(min,max)
    def random_decimalNumber(min,max,p):
        return round(random.uniform(min, max),p)
    def random_string(l):
        return ''.join((random.choice(string.ascii_uppercase) for x in range(l)))
    def random_string_lower(l):
        return ''.join((random.choice(string.ascii_lowercase) for x in range(l)))
    def random_string_both(l):
        return ''.join((random.choice(string.ascii_letters) for x in range(l)))
    def random_substringfromstring(string):
        min=random.randint(0,len(string))
        max=random.randint(0,len(string))
        if(min>max):
            c=min
            min=max
            max=c
        return string[min:max]
    def random(l):
        return ''.join((random.choice(string.ascii_letters+string.digits) for x in range(l)))
a=Genrator
print("Random Integer :",a.random_integerNumber(1,20)    )
print("Random Decimal Number :",a.random_decimalNumber(1,20,2))
print("Random Uppercase String :",a.random_string(10))
print("Random Lowercase String :",a.random_string_lower(10))
print("Random Lowercase and Uppercase Combine String :",a.random_string_both(10))
print("Random Substring from String :",a.random_substringfromstring("Hello Hitesh"))
print("Random String with Numbers:",a.random(8))