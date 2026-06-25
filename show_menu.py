import menu

def show_menu():
  print("\n===== CARDÁPIO =====")
  for item in menu.menu:
    print(f"[{item['id']}] {item['name']} - R${item['price']:.2f} ({item['category']})")
  print("====================\n")

def show_options():
  print("\n===== O QUE DESEJA FAZER? =====")
  print("[1] Adicionar item ao pedido")
  print("[2] Remover item do pedido")
  print("[3] Alterar quantidade de item")
  print("[4] Ver pedido atual")
  print("[5] Calcular total")
  print("[6] Escolher forma de pagamento")
  print("[7] Finalizar pedido")
  print("[8] Cancelar pedido")
  print("[9] Consultar histórico")
  print("[0] Sair do sistema")
  print("================================")
  