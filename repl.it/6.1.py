number = int(input())
sqrList = []
sqrNum = 1

while True:
    if sqrNum**2 > number:
        break
    else:
        sqrList.append(str(sqrNum**2))
        sqrNum += 1

print(" ".join(sqrList))