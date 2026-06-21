import order
import menu

def add_item():
  item_found = None
  
  while item_found is None:
    code = int(input("Qual o código do item? "))
    
    for item in menu.menu:
      if item["id"] == code:
        item_found = item
        break
    
    if item_found is None:
      print("Código inválido, tente novamente.")
      
  quantity = None
  
  while quantity is None or quantity <= 0:
    quantity = int(input("Qual a quantidade? "))
      
    if quantity <= 0:
      print("Quantidade inválida, tente novamente.")
      quantity = None
        
  new_item = {
    "id": item_found["id"],
    "name": item_found["name"],
    "price": item_found["price"],
    "quantity": quantity
  }
  
  order.order.append(new_item)
  print(f"{quantity}x {item_found['name']} adicionado ao pedido!")