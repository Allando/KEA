from hashlib import md5
import string
import threading

letters = string.ascii_lowercase
digits = string.digits

listOfHashes = ["cafbed007b2f8ad3629c9d493e2d01c1", "1f91e749b20c34099f488b60fda381e9",
                "d9687be677a820405d77009772535d9d", "1761f003af811a880960c472c3b95a64"]

#breakme = "cdd9789b85fcea8eb6d062d639c44ced"

for l in letters:
    for l2 in letters:
        for l3 in letters:
            for l4 in letters:
                for l5 in letters:
                    hashLetters = l + l2 + l3 + l4 + l5

                    hashthis = hashLetters

                    hashedString = md5(hashLetters.encode('utf-8')).hexdigest()
                    for breakme in listOfHashes:
                        if hashedString == breakme:
                            print("found", hashthis)


for d in  range(10):
    for d1 in  range(10):
        for d2 in  range(10):
            for d3 in  range(10):
                for d4 in  range(10):
                    hashDigits = str(d) + str(d1) + str(d2) + str(d3) + str(d4)
                    for c in hashLetters:

                        hashthis = hashLetters

                        hashedString = md5(hashthis.encode('utf-8')).hexdigest()
                        for breakme in listOfHashes:
                            if hashedString == breakme:
                                print("found", hashthis)