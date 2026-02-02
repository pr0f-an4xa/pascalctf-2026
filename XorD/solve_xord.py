import random

encrypted_hex = "cb35d9a7d9f18b3cfc4ce8b852edfaa2e83dcd4fb44a35909ff3395a2656e1756f3b505bf53b949335ceec1b70e0"
encrypted = bytes.fromhex(encrypted_hex)

random.seed(1337)

flag = ""
for b in encrypted:
    random_key = random.randint(0, 255)
    flag += chr(b ^ random_key)

print(flag)
