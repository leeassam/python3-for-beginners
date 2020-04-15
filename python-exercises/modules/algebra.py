'''
Create a module named algebra. Implement the following functions
	add( *num)
	subtract (firstNum, *otherNum)
	divide (numerator, denominator)
	multiply (*num)
'''

def add (*num) :
    result = 0
    for i in num:
        result += i
    return result

def subtract (firstNum, *otherNum) :
    result = None
    if firstNum is not None:
        result = firstNum
        for i in otherNum:
            result -= i
    return result

def divide (numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError
    elif numerator is None or denominator is None :
        raise ValueError ("A numerator and denominator is required")
    else :
        return round( (numerator / denominator), 2)

def multiply (*num) :
    if num is None:
        raise ValueError ("At least one number must be provided")
    else :
        result = 1
        for i in num :
            result *= i
        return result


def main():
    print(add(3,4,5,6))
    print (subtract(50,6,5,4))
    print(divide(45,5))
    print(multiply(4,5,6,7))
    subtract()
    divide(45)

if __name__ == "__main__":
    main()