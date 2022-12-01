import string
import random
caps = string.ascii_uppercase
smalls = string.ascii_lowercase
nums = string.digits
punctuations = string.punctuation
password = []
password.extend(caps)
password.extend(smalls)
password.extend(nums)
password.extend(punctuations)
random.shuffle(password)
length = int(input('Enter How long password You need [Enter in integer]:'))
new_password = ''.join(password[0:length])
print(f'Your password is: {new_password}')