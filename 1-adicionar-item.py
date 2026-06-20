import order
import menu

def adicionarItem():
    item_encontrado = None
    
    while item_encontrado is None:
        codigo = int(input("Qual o código do item? "))
        
        for item in menu.menu:
            if item["id"] == codigo:
                item_encontrado = item
                break
        
        if item_encontrado is None:
            print("Código inválido, tente novamente.")