import order
from view_order import view_order

def change_quantity():
  if order.order == []:
    print("Não existe nenhum item na lista.")
    return False

  view_order()

  try:
    cod = int(input("Informe o código do item que deseja atualizar: "))
  except ValueError:
    print("Entrada inválida, digite um número.")
    return False

  for item in order.order:
    if item['id'] == cod:
      try:
        quantity = int(input("Informe a nova quantidade: "))
      except ValueError:
        print("Entrada inválida, digite um número.")
        return False

      if quantity <= 0:
        print("Quantidade inválida.")
        return False

      item['quantity'] = quantity
      print(f"Quantidade de {item['name']} atualizada para {quantity}.")
      view_order()
      return True

  print("Código inválido, item não encontrado.")
  return False