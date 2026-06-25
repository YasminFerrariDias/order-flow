import order

def view_order():
  if order.order == []:
    print("Nenhum item no pedido.")
    return False

  print("\n===== PEDIDO =====")
  for item in order.order:
    subtotal = item['quantity'] * item['price']
    print(f"[{item['id']}] {item['name']} - {item['quantity']}x R${item['price']:.2f} = R${subtotal:.2f}")
  print("====================\n")
  return True