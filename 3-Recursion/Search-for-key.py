# def procure_pela_chave(caixa_principal):
#     pilha = caixa_principal.crie_uma_pilha_para_busca()
#     while pilha is not void:
#         caixa = pilha.pegue_caixa()
#         for item in caixa:
#             if item.e_uma_caixa():
#                 print("Achei uma chave")
#             else:
#                 pilha.append(item)

## Casso recursivo

# def procure_pela_chave(caixa):
#     for item in caixa:
#         if item.e_uma_caixa:
#             procure_pela_chave(item)
#         elif item.e_uma_chave:
#             print("Achei a chave")

def search_for_key(box):
    for item in box:
        if item.isBox:
            search_for_key(item)
        elif item.isKey:
            print("I find the key!")