# Encryptor
import string
import random

set = string.ascii_letters + string.digits + string.punctuation + " "

key = ''.join(random.sample(set,len(set)))

# Import Message
message_file = open("Encryption/message.txt", "r")
message = message_file.read()
message_file.close()

codex = []

#convert strings to lists for indexing
start_list = []
for unit in message:
    start_list.append(unit)

ref_list = []
for s in set:
    ref_list.append(s)

encrypt_list = []
for k in key:
    encrypt_list.append(k)

# Convert start list to numeric index values
for n in start_list:
    for x in ref_list:
        if n == x:
            codex.append(ref_list.index(n))

encrypt_output = []

# map values to encryption key
for c in codex:
    encrypt_val = encrypt_list[c]
    encrypt_output.append(encrypt_val)

# write files to text document
secure_file = open("Encryption/encrypted_message.txt", "w")
encrpt_string = secure_file.write(key + " ##::: " +''.join(encrypt_output))
secure_file.close()
