import order
import menu

def add_item():
  item_found = None

  while item_found is None:
    try:
      code = int(input("Qual o código do item? "))
    except ValueError:
      print("Entrada inválida, digite um número.")
      continue

    for item in menu.menu:
      if item["id"] == code:
        item_found = item
        break

    if item_found is None:
      print("Código inválido, tente novamente.")

  quantity = None

  while quantity is None or quantity <= 0:
    try:
      quantity = int(input("Qual a quantidade? "))
    except ValueError:
      print("Entrada inválida, digite um número.")
      continue

    if quantity <= 0:
      print("Quantidade inválida, tente novamente.")
      quantity = None

  for existing in order.order:
    if existing["id"] == item_found["id"]:
      existing["quantity"] += quantity
      print(f"Quantidade de {item_found['name']} atualizada no pedido!")
      return

  new_item = {
    "id": item_found["id"],
    "name": item_found["name"],
    "price": item_found["price"],
    "quantity": quantity
  }

  order.order.append(new_item)
  print(f"{quantity}x {item_found['name']} adicionado ao pedido!")  