import random

i = input("Geben Sie die max. Zahl ein bis zu der Sie rechnen wollen: ")
r = input("Geben Sie die Anzahl der Aufgaben ein: ")
w = input("Geben Sie den Operator ein: ")
f = True
ergeb = []

for e in range(int(r)):
    r = random.randint(1, int(i))
    t = random.randint(1, int(i))
    if(w == '+'):
        o = r + t
    if (w == '-'):
        o = r - t
    if (w == '*'):
        o = r * t
    if (w == '/'):
        o = r / t
    ergeb.append(o)
    print(str(r) + " " + w + " " + str(t) + " = ")

while f:
    u = input("Fertig? [j/n]: ")
    if u == 'j':
        print(ergeb)
        break







