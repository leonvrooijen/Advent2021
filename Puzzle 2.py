f = open("input question 2.py", "r")


Distance = 0
Depth = 0
Direction = ""
Speed = ""


for line in list(f.read().splitlines()):
    for word in line.split():
        if word.isnumeric():
            Speed = word
        elif word == "forward":
            Direction = "forward"
        elif word == "up":
            Direction = "up"
        elif word == "down":
            Direction = "down"


    if Direction == "forward":
        Distance = int(Distance) + int(Speed)
    elif Direction == "up":
        Depth = int(Depth) - int(Speed)
    elif Direction == "down":
        Depth = int(Depth) + int(Speed)


print(Distance*Depth)