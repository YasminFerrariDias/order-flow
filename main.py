from add_item import add_item
from remove_item import remove_item
from change_quantity import change_quantity
from view_order import view_order
from calculate_order import calculate_order
from payment_methods import payment_methods
from finish_order import finish_order
from cancel_order import cancel_order
from show_menu import show_menu, show_options
from show_history import show_history

def main():
  show_options()

  while True:
    choice = input("\nEscolha uma opção: ").strip()

    if choice == "1":
      show_menu()
    elif choice == "2":
      add_item()
    elif choice == "3":
      remove_item()
    elif choice == "4":
      change_quantity()
    elif choice == "5":
      view_order()
    elif choice == "6":
      total = calculate_order()
      if total > 0:
        print(f"Total do pedido: R${total:.2f}")
    elif choice == "7":
      total = calculate_order()
      if total > 0:
        payment_methods(total)
    elif choice == "8":
      finish_order()
    elif choice == "9":
      cancel_order()
    elif choice == "10":
      show_history()
    elif choice == "0":
      print("Saindo do sistema. Até logo!")
      break
    else:
      print("Opção inválida. Tente novamente.")

    show_options()

if __name__ == "__main__":
  main()