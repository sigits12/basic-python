name = input("What's your name ? > ")
sex = input("What's your sex ? (male/female) > ")
bb = int(input("Input weight (Kg) > "))
tb1 = int(input("Input Hight (Cm) > "))
tb2 = tb1 / 100
bmi = bb / (tb2 * tb2)


def male():
    if bmi < 17:
        cc = "Thin"
    elif bmi >= 17 and bmi < 23:
        cc = "Normal"
    elif bmi >= 23 and bmi < 27:
        cc = "Fat"
    else:
        cc = "Obesitas"
    return cc


def female(self):
    if bmi < 18:
        cc = "Thin"
    elif bmi >= 18 and bmi < 25:
        cc = "Normal"
    elif bmi >= 25 and bmi < 27:
        cc = "Fat"
    else:
        cc = "Obesitas"
    return cc


def kesimpulan(cc):
    print("Hei ", name, " !")
    print("Your weight is ", bb, "Kg")
    print("Your weight is= ", bb, " Kg")
    print("Your height is= ", tb2, " M")
    print("Your Body Mass Index is= ", bmi)
    print("With these results, we conclude that you are ", hasil_bmi, " people.")


if sex == "male":
    result = male()
    kesimpulan(result)
elif sex == "female":
    result = male()
    kesimpulan(result)
else:
    exit()
