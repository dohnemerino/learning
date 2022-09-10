# Decryptor Script
import string

# Import Message
encrpt_message_file = open("Encryption/encrypted_message.txt", "r")
import_message = encrpt_message_file.read()
encrpt_message_file.close()

message_split = import_message.split(" ##::: ", 1)

key = message_split[0]
encrypt_message = message_split[1]
 
 # ASCii reference set
set = string.ascii_letters + string.digits + string.punctuation + " "

codex = []

#convert strings to lists for indexing
start_list = []
for unit in encrypt_message:
    start_list.append(unit)

ref_list = []
for s in set:
    ref_list.append(s)

encrypt_list = []
for k in key:
    encrypt_list.append(k)

# Convert start list to numeric index values
for n in start_list:
    for x in encrypt_list:
        if n == x:
            codex.append(encrypt_list.index(n))

plain_output = []

# map values to encryption key
for c in codex:
    ref_val = ref_list[c]
    plain_output.append(ref_val)

# write files to text document
secure_file = open("Encryption/decrypted_message.txt", "w")
encrpt_string = secure_file.write(''.join(plain_output))
secure_file.close()