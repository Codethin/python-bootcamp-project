import hashlib
rawdata = input("enter your data here: ")
encrypted = hashlib.md5(rawdata.encode()).hexdigest()
print(encrypted)
