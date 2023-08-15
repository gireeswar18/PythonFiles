print("Python Pattern Programs")
#square
print("Square")
for i in range(5):
    print("* " * 5)

#increasing triangle pattern
print("Increasing triangle pattern")
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end = " ")
    print()

#decreasing triangle pattern
print("Decreasing triangle pattern")
for i in range(5):
    for j in range(i, 5):
        print("*" , end = " ")
    print()

#Right sided triangle
print("Right sided triangle")
for i in range(5):
    for j in range(i, 5):
        print(" ", end = " ")
    for k in range(i+1):
        print("*", end = " ")
    print()

#Reverse right sided triangle
print("Reverse right sided triangle")
for i in range(5):
    for j in range(i+1):
        print(" ", end = " ")
    for k in range(i, 5):
        print("*", end = " ")
    print()

#Hill pattern
print("Hill pattern")
for i in range(5):
    for j in range(i, 5):
        print(" ", end = " ")
    for j in range(i+1):
        print("*", end = " ")
    for k in range(i):
        print("*", end = " ")
    print()

#Reverse Hill pattern
print("Reverse hill pattern")
for i in range(5):
    for j in range(i+1):
        print(" ", end = " ")
    for k in range(i, 5):
        print("*", end = " ")
    for l in range(i, 4):
        print("*", end = " ")
    print()

#Diamond pattern
print("Diamond pattern")
for i in range(4):
    for j in range(i, 5):
        print(" ", end = " ")
    for k in range(i+1):
        print("*", end = " ")
    for l in range(i):
        print("*", end = " ")
    print()
for i in range(5):
    for j in range(i+1):
        print(" ", end = " ")
    for k in range(i, 5):
        print("*", end = " ")
    for l in range(i, 4):
        print("*", end = " ")
    print()


#pyramid
print("Pyramid")
for i in range(5):
    for j in range(i, 5):
        print(" ", end = "")
    for k in range(i+1):
        print("*", end = " ")
    print()

#Double hill
print("Double Hill")
for i in range(5):
    for j in range(i, 5):
        print(" ", end = "")
    for k in range(i+1):
        print("*", end = " ")
    for l in range(i, 3):
        print(" ", end = " ")
    for m in range(i+1):
        if (m == 4):
            break
        print("*", end = " ")
    print()

#Timesand
print("Time sand")
for i in range(5):
    for j in range(i+1):
        print(" ", end = " ")
    for k in range(i, 5):
        print("*", end =" ")
    for k in range(i, 4):
        print("*", end = " ")
    print()
for i in range(5):
    if i == 0:
        continue
    for j in range(i, 5):
        print(" ", end = " ")
    for k in range(i+1):
        print("*", end = " ")
    for k in range(i):
        print("*", end = " ")
    print()
