import hashlib
sad ='Hello World@2Aa'
hash_object = hashlib.sha1(sad)
hex_dig = hash_object.hexdigest()
print(hex_dig)