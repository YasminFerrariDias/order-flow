from add_item import add_item
from remove_item import remove_item
from change_quantity import change_quantity
from view_order import view_order
from calculate_order import calculate_order
from process_payment import process_payment
from finish_order import finish_order
from cancel_order import cancel_order
from show_menu import show_menu, show_options
from show_history import show_history

def main():
  show_menu()
  show_options()

  while True:
    choice = input("\nEscolha uma opção: ").strip()
    success = True

    if choice == "1":
      add_item()
    elif choice == "2":
      success = remove_item()
    elif choice == "3":
      success = change_quantity()
    elif choice == "4":
      success = view_order()
    elif choice == "5":
      total = calculate_order()
      if total > 0:
        print(f"Total do pedido: R${total:.2f}")
      else:
        success = False
    elif choice == "6":
      total = calculate_order()
      if total > 0:
        process_payment(total)
      else:
        success = False
    elif choice == "7":
      success = finish_order()
    elif choice == "8":
      success = cancel_order()
    elif choice == "9":
      success = show_history()
    elif choice == "0":
      print("Saindo do sistema. Até logo!")
      break
    else:
      print("Opção inválida. Tente novamente.")
      success = False

    if success:
      show_menu()
      show_options()

if __name__ == "__main__":
  main()