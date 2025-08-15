number = input("Insira o número: ")

def par_impar(a):
    if(a % 2 == 0):
        return "par"
    else:
        return "impar"

print(par_impar(int(number)))