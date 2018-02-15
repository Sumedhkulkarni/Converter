class Temperature:
    def fartocel(self):
        far = float(input("Enter the temperature in fahrenheit\n"))
        cel = (far - 32) * (5 / 9)
        print("The temperature in celsius is {} C.\n".format(cel))
        print("___________________________________________________________________________\n")

    def celtofar(self):
        cel = float(input("Enter the temperature in celsius\n"))
        far = (cel * (9 / 5)) + 32
        print("The temperature in fahrenheit is {} f.\n".format(far))
        print("___________________________________________________________________________\n")

    def celtokel(self):
        cel = float(input("Enter the temperature in celsius\n"))
        kel = cel + 273.5
        print("The temperature in kelvin is {} K.\n".format(kel))
        print("___________________________________________________________________________\n")


class Length:
    def cmtom(self):
        cm = float(input("Enter the distance in cm.\n"))
        print("The distance in meter is {} m.\n".format(cm / 100))
        print("___________________________________________________________________________\n")

    def mtocm(self):
        m = float(input("Enter the distance in meter.\n"))
        print("The distance in centimeter is {} cm.\n".format(m * 100))
        print("___________________________________________________________________________\n")

    def cmtoinch(self):
        cm = float(input("Enter the distance in cm.\n"))
        print("The distance in inches is {} in.\n".format(cm * 0.3937008))                       # 1 cm = 0.3937008 inches
        print("___________________________________________________________________________\n")

    def inchtocm(self):
        inch = float(input("Enter the distance in inches.\n"))
        print("The distance in centimeter is {} cm.\n".format(inch / 0.3937008))
        print("___________________________________________________________________________\n")

    def mtoinch(self):
        m = float(input("Enter the distance in meter.\n"))
        print("The distance in inches is {}in.\n".format(m * 39.37008))                          # 1m = 39.37008 inches
        print("___________________________________________________________________________\n")

    def inchtom(self):
        inc = float(input("Enter the distance in inches.\n"))
        print("The distance in meters is {} m.\n".format(inc / 39.37008))
        print("___________________________________________________________________________\n")

    def mtofeet(self):
        m = float(input("Enter the distance in meter.\n"))
        print("The distance in feet is {}feet.\n".format(m * 3.28084))                           # 1 feet = 3.28084 feet
        print("___________________________________________________________________________\n")

    def feettom(self):
        f = float(input("Enter the distance in feet.\n"))
        print("The distance in meters is {} m.\n".format(f / 3.28084))
        print("___________________________________________________________________________\n")

    def feettoyard(self):
        f = float(input("Enter distance into feet.\n"))
        print("The distance in yards is {}.\n".format((f / 3.28084) * 1.09361))
        print("___________________________________________________________________________\n")

    def mtoyard(self):
        m = float(input("Enter the distance in meter.\n"))
        print("The distance in yards is {}.\n".format(m * 1.09361))                              # 1 meter = 1.09361 yards
        print("___________________________________________________________________________\n")

    def inchtoyard(self):
        inc = float(input("Enter the distance in inches.\n"))
        print("The distance in yards is {} inches.\n".format((inc / 39.370078) * 1.09361))
        print("___________________________________________________________________________\n")

    def mtomile(self):
        m = float(input("Enter the distance in meters.\n"))
        print("The distance in miles is {} miles.\n".format(m * 0.000621371))                    # 1 meter = 0.000621371 miles
        print("___________________________________________________________________________\n")


class Weight:
    def kgtopound(self):
        kg = float(input("Enter the weight in kg.\n"))
        print("The weight in pounds is {}.".format(kg * 2.20462))                                # 1 kg = 2.20462 pounds
        print("___________________________________________________________________________\n")

    def poundstokg(self):
        po = float(input("Enter the weight in pounds\n"))
        print("The weight in kilograms is {}kg.".format(po / 2.20462))
        print("___________________________________________________________________________\n")

    def gtopound(self):
        g = float(input("Enter the weight in grams"))
        print("The weight in pounds is {}.".format((g / 1000) * 2.20462))                        # convert grams into kg and then into pounds
        print("___________________________________________________________________________\n")


class Time:
    def bigtosmall(self):
        t = int(input("Enter the time in 24 hour format..\n"))
        if t < 12:
            print("After converting the time into 12 hour format the time will be {} AM.\n".format(t))
            print("___________________________________________________________________________\n")
        elif t is 12:
            print("After converting the time into 12 hour format the time will be 12 PM.\n")
            print("___________________________________________________________________________\n")
        elif t > 12 and t < 24 :
            print("After converting the time into 12 hour format the time will be {} PM.\n".format(t - 12))
            print("___________________________________________________________________________\n")
        elif t is 24:
            print("After converting the time into 12 hour format the time will be 00 AM.\n")
            print("___________________________________________________________________________\n")
        else:
            print("Please Enter Correct Time...Thank you..!!\n")
            print("___________________________________________________________________________\n")


class Final:
    while True:
        print("Enter 1 for Temperature conversion..\n"
              "Enter 2 for Length conversion..\n"
              "Enter 3 for Weight conversion..\n"
              "Enter 4 for Time conversion..\n"
              "Enter 5 for exit..\n\n"
              "Enter your choice please...\n")
        n = int(input())
        if n is 1:
            temp = Temperature()
            ch = int(input("Enter 1 to convert Fahrenheit into Celsius\n"
                           "Enter 2 to convert Celsius into Fahrenheit\n"
                           "Enter 3 to convert Celsius into Kelvin\n\n"
                           "Enter your choice\n"))
            if ch is 1:
                temp.fartocel()
            elif ch is 2:
                temp.celtofar()
            elif ch is 3:
                temp.celtokel()
            else: 
                print("Enter correct choice\n")
                print("___________________________________________________________________________\n")

        elif n is 2:
            leng = Length()
            ch = int(input("\n\nEnter 1 to convert centimeter into meter\n"
                           "Enter 2 to convert meter into centimeter\n"
                           "Enter 3 to convert centimeter into inches\n"
                           "Enter 4 to convert inches into centimeter\n"
                           "Enter 5 to convert meter into inches\n"
                           "Enter 6 to convert inches into meter\n"
                           "Enter 7 to convert meter into feet\n"
                           "Enter 8 to convert feet into meter\n"
                           "Enter 9 to convert feet into yards\n"
                           "Enter 10 to convert meter to yards\n"
                           "Enter 11 to convert inches into yards\n"
                           "Enter 12 to convert meter into miles\n\n"
                           "Enter your choice please....\n"))
            if ch is 1:
                leng.cmtom()
            elif ch is 2:
                leng.mtocm()
            elif ch is 3:
                leng.cmtoinch()
            elif ch is 4:
                leng.inchtocm()
            elif ch is 5:
                leng.mtoinch()
            elif ch is 6:
                leng.inchtom()
            elif ch is 7:
                leng.mtofeet()
            elif ch is 8:
                leng.feettom()
            elif ch is 9:
                leng.feettoyard()
            elif ch is 10:
                leng.mtoyard()
            elif ch is 11:
                leng.inchtoyard()
            elif ch is 12:
                leng.mtomile()
            else:
                print("Enter correct choice...")
                print("___________________________________________________________________________\n")

        elif n is 3:
            wet = Weight()
            ch = int(input("Enter 1 to convert Kilograms into Pounds\n"
                           "Enter 2 to convert Pounds into Kilograms\n"
                           "Enter 3 to convert Grams into Pounds\n\n"
                           "Enter your choice...\n"))
            if ch is 1:
                wet.kgtopound()
            elif ch is 2:
                wet.poundstokg()
            elif ch is 3:
                wet.gtopound()
            else:
                print("Enter correct choice please...\n\n")
                print("___________________________________________________________________________\n")

        elif n is 4:
            tim = Time()
            tim.bigtosmall()

        elif n is 5:
            exit()
        else:
            print("Enter correct choice please...\n\n")
            print("___________________________________________________________________________\n")


# final = Final()