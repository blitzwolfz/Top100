letters = "abcdefghijklmnopqrstuvwxyz"
lst = []

for x in range(len(letters)):
    lst.append(letters[x])


name = ["m", "i", "s", "i", "u", "r", "a"]

index = 2
counter = 0
total = 0
x = 0

while True:
    name[index] = lst[x]
    print(*name, sep="")

    if counter == 10:
        ok = input("Stop")
        counter = 0
    
    counter += 1
    total += 1
    x += 1

    if total == len(letters):
        break

