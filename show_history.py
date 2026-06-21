import history

def show_history():
  if len(history.history) == 0:
    print("Nenhum pedido foi finalizado ainda.")
    return

  print("\n===== HISTÓRICO DE PEDIDOS =====")

  for number, order_record in enumerate(history.history, start=1):
    print(f"\nPedido #{number}")

    for item in order_record["items"]:
      print(f"  {item['quantity']}x {item['name']}")

    print(f"  Total: R${order_record['total']:.2f}")
    print(f"  Pagamento: {order_record['payment']['forma']}")

  print("=================================\n")