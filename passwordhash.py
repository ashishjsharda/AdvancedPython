'''
Created on Oct 31, 2019
Password Hashing
@author: asharda
'''

import hashlib
password='pas$$word'
h=hashlib.md5(password.encode())
print(h.hexdigest())
