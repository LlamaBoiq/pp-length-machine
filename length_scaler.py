import random
running = True
while running:
    input()
    head = "D"
    body = "="
    balls = "8"

    bodylen = random.randrange(1, 20)
    if bodylen <= 3:
        print("Got a small pecker there pal")
    elif bodylen <= 11:
        print("Its got some decent size")
    elif bodylen >= 12:
        print("Phew were working with a monster!")
    print("{0}{1}{2}".format(balls, body * bodylen, head))