
from model.contacts import Contacts
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string (prefix, maxilen):
    symbols = string.ascii_letters+string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxilen))])


testdata = [Contacts(name = "", lastN="", address="", email1="")]  + [
    Contacts (name = random_string("name", 10), lastN = random_string("lastname", 10), address = random_string("address", 10), home = random_string("home phone", 10))
    for i in range (n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# Задание 18
# with open(file, "w") as out_file:
#     out_file.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))


#Задание 19
with open(file, "w") as out_file:
    jsonpickle.set_encoder_options("json",  indent=2)
    out_file.write(jsonpickle.encode(testdata))
