import order

def view_order(): 
  print("\n===== PEDIDO =====")
  for item in order.order: 
    subtotal = item['quantity'] * item['price']
    print(f"[{item['id']}] {item['name']} - {item['quantity']}x R${item['price']:.2f} = R${subtotal:.2f}")
  print("====================\n")

