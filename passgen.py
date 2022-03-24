import random
import string
from sys import argv
import pyperclip

script, length = argv
length = int(length)
plaintext = string.digits + string.punctuation + string.ascii_letters
password = ''.join(random.choices(plaintext, k=length))
pyperclip.copy(password)
print(password)
