list_number = []


def ordem(array):

    for i in range(3):
        entrada = input(f"Digite o valor {i+1}: ")
        list_number.append(int(entrada))

    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return "não está em ordem crescente"
    
    return "crescente"

print(ordem(list_number))