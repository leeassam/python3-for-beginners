'''
Create a temperature class. Make two methods :
convertFahrenheit - It will take celsius and convert it into Fahrenheit.
convertCelsius - It will take Fahrenheit and will convert it into Celsius.
'''

class temperature :

    def convertCelcius(self, temp_f):
        if temp_f is not None:
            temp_c = (temp_f - 32) * (5/9)
            temp_c = round(temp_c, 1)
            return temp_c

    def convertFarenheit(self, temp_c):
        if temp_c is not None:
            temp_f = (temp_c * (9/5)) + 32
            temp_f = round(temp_f, 1)
            return temp_f

def main() :
    temp = temperature()
    temp_c = 35
    temp_f = 100
    print(f"{temp_c} C is equivalent to {temp.convertFarenheit(temp_c)} F")
    print(f"{temp_f} F is equivalent to {temp.convertCelcius(temp_f)} C")


if __name__ == "__main__" :
    main()