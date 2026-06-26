import menu

def show_menu():
  print("\n===== CARDÁPIO =====")
  for item in menu.menu:
    print(f"[{item['id']}] {item['name']} - R${item['price']:.2f} ({item['category']})")
  print("====================\n")

def show_options():
  print("\n===== O QUE DESEJA FAZER? =====")
  print("[1] Ver cardápio")
  print("[2] Adicionar item ao pedido")
  print("[3] Remover item do pedido")
  print("[4] Alterar quantidade de item")
  print("[5] Ver pedido atual")
  print("[6] Calcular total")
  print("[7] Escolher forma de pagamento")
  print("[8] Finalizar pedido")
  print("[9] Cancelar pedido")
  print("[10] Consultar histórico")
  print("[0] Sair do sistema")
  print("================================")