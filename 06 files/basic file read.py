
fh = open("E:\Python Projects\\test.txt", "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)