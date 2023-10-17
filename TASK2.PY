temp = float(input("Enter Temperature: "))

unit = input("Enter unit('C' for Celcius or 'F' for Fahrenheit):")
if unit == 'C' or unit== 'C':
    newTemp=9/5*temp+32
    print("Temperature in Celcius=",newTemp)
elif unit=='F' or unit=='f':
    newTemp=5/9*(temp-32)
    print("Temperature in Fahrenheit=",newTemp)
else:
    print("Unknown unit",unit)    