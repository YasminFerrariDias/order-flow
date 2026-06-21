import order
import menu

def adicionarItem():
  quantidade = None
  item_encontrado = None
  
  while item_encontrado is None:
    codigo = int(input("Qual o código do item? "))
    
    for item in menu.menu:
      if item["id"] == codigo:
        item_encontrado = item
        break
      
      if item_encontrado is None:
        print("Código inválido, tente novamente.")
        
    while quantidade is None or quantidade <= 0:
      quantidade = int(input("Qual a quantidade? "))
        
      if quantidade <= 0:
        print("Quantidade inválida, tente novamente.")
        quantidade = None
          
    novo_item = {
        "id": item_encontrado["id"],
        "name": item_encontrado["name"],
        "price": item_encontrado["price"],
        "quantity": quantidade
    }
    
  order.order.append(novo_item)
  print(f"{quantidade}x {item_encontrado['name']} adicionado ao pedido!")
