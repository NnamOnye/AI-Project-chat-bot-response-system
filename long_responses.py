import random


R_KNOWING = "I dont know everything, my database is not big enough yet "

def unknown():
    response = ["could you please rephrase that...?","...","I dont know everything, my database is not big enough yet","what does that mean"][random.randrange(4)]
    return response
