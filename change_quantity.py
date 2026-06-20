import order
from view_order import view_order

def change_quantity():
    if order.order == []:
        print("Não existe nenhum item na lista.")
        return
    
    view_order()
    cod = int(input("Informe o código do item que deseja atualizar: "))

    for item in order.order:
        if item['id'] == cod:
            quantity = int(input("Informe a nova quantidade: "))
            if quantity <= 0:
                print("Quantidade inválida.")
                return
            item['quantity'] = quantity
            print(f"Quantidade de {item['name']} atualizada para {quantity}.")
            view_order()
            return

    print("Código inválido, item não encontrado.")
