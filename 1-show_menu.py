import menu

def show_menu():
  print("\n===== CARDÁPIO =====")
  for item  in menu.menu:
    print(f"[{item['id']}] {item['name']} - R${item['price']:.2f} ({item['category']})")
    print("====================\n")

show_menu()