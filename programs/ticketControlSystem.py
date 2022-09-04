from numbers import Number
import os


ageReq = 18
ticketPrice = 35
studentCheckAge = [20,21,22,23,24,25,26,27,28,29]
exitCommand = str

print("System kontroli biletów w kinie.\n")
print("Witamy w kinie!")

while True:
        
    age = int(input("Ile masz lat?: "))
    clientMoney = float(input("Ile posiadasz pieniędzy?: "))

    if age < 18:
        print("Niestety film jest od 18 lat.")
        

    elif age == 18 or age == 19:
        legitymacjaSzkolna = input("Czy posiadasz legitymację szkolną?: ")

        if legitymacjaSzkolna == 'y':
            ticketPrice *= 0.50
            print("Twój bilet kosztuje teraz: " + str(ticketPrice))

            if clientMoney < ticketPrice:
                print("Nie stać Cię na bilet. " + "Brakuje Ci jeszcze " + str(ticketPrice - clientMoney))
            

        elif legitymacjaSzkolna != 'y':
            ticketPrice = 35
            print("Twój bilet kosztuje teraz: " + str(ticketPrice))
            if clientMoney < ticketPrice:
                print("Nie stać Cię na bilet. " + "Brakuje Ci jeszcze " + str(ticketPrice - clientMoney))



    elif (age in studentCheckAge):
        legitymacjaStudencka = input("Czy posiadasz legitymację studencką?:")
        if legitymacjaStudencka == 'y':
            ticketPrice *= 0.50
            print("Twój bilet kosztuje teraz: " + str(ticketPrice))

            if clientMoney < ticketPrice:
                print("Nie stać Cię na bilet. " + "Brakuje Ci jeszcze " + str(ticketPrice - clientMoney))
                
        elif legitymacjaStudencka != 'y':
            ticketPrice = 35
            print("Twój bilet kosztuje teraz: " + str(ticketPrice))
            if clientMoney < ticketPrice:
                print("Nie stać Cię na bilet. " + "Brakuje Ci jeszcze " + str(ticketPrice - clientMoney))
                
                

    elif age > 29 and age < 65:
        ticketPrice = 35
        print("Twój bilet kosztuje teraz: " + str(ticketPrice))
        if clientMoney < ticketPrice:
            print("Nie stać Cię na bilet. " + "Brakuje Ci jeszcze " + str(ticketPrice - clientMoney))

    elif age >= 65:
        ticketPrice *= 0.35
        print("Posiadasz zniżkę seniora, twój bilet kosztuje ", ticketPrice)

    if clientMoney - ticketPrice >= 0:
        print("Kupiłeś bilet! Życzymy miłego seansu!!! Oto twoja reszta", clientMoney - ticketPrice)



    exitCommand = input("Napisz " + "\"anuluj\" " + "aby wyjść" + " \nAlbo cokolwiek by kontynuować    :    "   )

    if exitCommand == "anuluj": break

    else:
        os.system("cls")

