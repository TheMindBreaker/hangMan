def read():
    import random

    lines = open("words.txt").readlines()
    line = lines[0]

    words = line.split()
    myword = random.choice(words)
