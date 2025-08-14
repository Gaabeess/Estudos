number = input("Insira um número inteiro: ")

def fizzbuzz(a):

    if(a % 3 == 0 and a % 5 == 0):
        return "FizzBuzz"
    elif(a % 3 == 0):
        return "Fizz"
    elif(a % 5 == 0):
        return "Buzz"
    else:
        return a
    
print(fizzbuzz(int(number)))