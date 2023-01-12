import random


R_KNOWING = "I dont know everything/phrases my database is not large enough"

def unknown():
    response = ["could you please rephrase that...?","...","I dont know everything/phrases my database is not large enough","what does that mean"][random.randrange(4)]
    return response