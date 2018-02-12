from hashlib import md5
from string import *

thash = "0fa57905158d7b8511b94f8dcd6f6edf"
hash_list = "54229abfcfa5649e7003b83dd4755294.ca46c1b9512a7a8315fa3c5a946e8265." \
        "b6d767d2f8ed5d21a44b0e5886680cb9.1d7f7abc18fcb43975065399b0d1e48e"

alpha = ascii_uppercase + ascii_lowercase

# for l in alpha:
#     for l2 in alpha:
#         for l3 in alpha:
#             for l4 in alpha:
#                 for l5 in alpha:
#                     crackthis = l + l2 + l3 + l4 + l5
#                     hct = md5(crackthis.encode('UTF-8')).hexdigest()
#                     for h in hash_list:
#                         if hct == h:
#                             print(crackthis)

for l in range(500):
    for l2 in range(500):
        for l3 in range(500):
            crackthis = str(l) + str(l2) + str(l3)
            hct = md5(crackthis.encode('UTF-8')).hexdigest()
            for h in hash_list.split('.'):
                if hct == h:
                    print(crackthis)

