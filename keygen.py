import string
import random

set = string.ascii_letters + string.digits + string.punctuation + " "

key = ''.join(random.sample(set,len(set)))

text_file = open("key.txt", "w")
n = text_file.write(key)
text_file.close()