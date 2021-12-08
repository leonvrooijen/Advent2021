f = open("input question 2.py", "r")


Distance = 0
Depth = 0
Command = ""
Speed = ""
Aim = 0


for line in list(f.read().splitlines()):
    Sentence = line.split()
    Command = Sentence[0]
    Speed = int(Sentence[1])


    if Command == "forward":
        Distance = int(Distance) + int(Speed)
        Depth = Depth + (int(Aim) * int(Speed))
    elif Command == "up":
        Aim = int(Aim) - int(Speed)
    elif Command == "down":
        Aim = int(Aim) + int(Speed)


print(Distance*Depth)