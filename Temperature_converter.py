type1 = input("What type of temperature you want to convert: ")
type2 = input("What type of temperature you want to convert to: ")
temp1 = int(input("Give any temparature: "))


def celsius() :
    celsius_to_kelvin = ((temp1*100)/5) - 273   
    celsius_to_fahrenheit = ((temp1*9)/5)+32

    if type2 == "kelvin" : 
        print(f"Your Given Temperature in kelvin is: {celsius_to_kelvin}")
    elif type2 == "fahrenheit": 
        print(f"Your Given Temperature in fahrenheit is: {celsius_to_fahrenheit}")

def fahrenheit() :
    fahrenheit_to_kelvin = (100*(temp1-32)/9)+273
    fahrenheit_to_celsius = 5/9 * (temp1 - 32)
    if type2 == "celsius" :
        print(f"Your Given Temperature in celsius is: {fahrenheit_to_celsius}")
    elif type2 == "kelvin" :
        print(f"Your Given Temperature in kelvin is: {fahrenheit_to_kelvin}")

def kelvin() :
    kelvin_to_fahrenheit = (9*(temp1-273)/100)-32
    kelvin_to_celsius = ((temp1 - 273)*5)/100
    if type2 == "fahrenheit": 
        print(f"Your Given Temperature in fahrenheit is: {kelvin_to_fahrenheit}")
    elif type2 == "celsius" :
        print(f"Your Given Temperature in celsius is: {kelvin_to_celsius}")


if type1 == "celsius":
    celsius()
elif type1 == "fahrenheit":
    fahrenheit()
elif type1 == "kelvin":
    kelvin()
else:
    print("Your Given Type is not in our database")
