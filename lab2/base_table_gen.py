import string
import random

def text_generator(size=random.randrange(1,100), chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_data(n,c,t):
    for k in range(0,n):
        instert_rand_data(c,t,"data:"+str(k))

def instert_rand_data(c,t,v):
    # c.execute("INSERT INTO "+t+" (value) VALUES (?)",(text_generator(),))
    c.execute("INSERT INTO "+t+" (value) VALUES (?)",(v,))