def fake_bin(x):

    string = ''
    for i in x:
        if int(i) < 5:
            i = 0
            string += str(i)
        else:
            i = 1
            string += str(i)
    return string


string = "12345678910"
print(fake_bin(string))
