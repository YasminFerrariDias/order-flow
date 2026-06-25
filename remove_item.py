import order
from view_order import view_order

def remove_item():
  if order.order == []:
    print("Não existe nenhum item na lista.")
    return False

  view_order()

  try:
    cod = int(input("Digite o código do item para remover: "))
  except ValueError:
    print("Entrada inválida, digite um número.")
    return False

  for item in order.order:
    if item['id'] == cod:
      order.order.remove(item)
      print(f"{item['name']} removido do pedido.")
      return True

  print("Código inválido, item não encontrado.")
  return False