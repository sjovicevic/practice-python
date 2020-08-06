# Generating random password combination between 20 and 30 characters using python in-built modules

import random 
import string

def gen_password(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(n))


n = random.randint(20,30)
print(gen_password(n))
