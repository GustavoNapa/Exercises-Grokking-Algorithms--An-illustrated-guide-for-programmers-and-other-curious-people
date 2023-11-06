# def pesquisa_binaria(lista, item):
#     baixo = 0
#     alto = len(lista)
    
#     if(len(lista) <= 1):
#         if(lista[0] == item):
#             return True
        
#         return False
    
#     while baixo <= alto:
#         meio = int((baixo + alto) / 2)
#         chute = lista[meio]
        
#         if chute == item:
#             return True
#         if chute > item:
#             alto = meio
#         else:
#             baixo = meio
        
#         return pesquisa_binaria(lista[baixo:alto], item)
    
# minha_lista = [1, 2, 3, 5, 7, 9]

# print(pesquisa_binaria(minha_lista, 3))
# print(pesquisa_binaria(minha_lista, -1))

def binary_search(list, item):
    lower = 0
    upper = len(list)
    
    if(len(list) <= 1):
        if(list[0] == item):
            return True
        
        return False
    
    while lower <= upper:
        middle = int((lower + upper) / 2)
        kick = list[middle]
        
        if kick == item:
            return True
        if kick > item:
            upper = middle
        else:
            lower = middle
        
        return binary_search(list[lower:upper], item)
    
my_list = [1, 2, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
print(binary_search(my_list, 9))
print(binary_search(my_list, 15))