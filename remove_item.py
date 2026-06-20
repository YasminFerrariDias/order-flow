import order
from view_order import view_order

def remove_item():
  if order.order == []:
    print("Não existe nenhum item na lista.")
  else:
    view_order()
    cod = int(input("Digite o código do item para remover: "))
      
    for item in order.order:
      if item['id'] == cod:
        order.order.remove(item)
        print(f"{item['name']} removido do pedido.")
        return
        
    print("Código inválido, item não encontrado.")
    