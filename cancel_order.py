import order

def cancel_order():
  if order.order == []:
    print("Não existe nenhum pedido em andamento.")
    return False

  answer = input("Tem certeza que deseja cancelar o pedido? (s/n): ")
  if answer == 's' or answer == 'S':
    order.order.clear()
    print("Pedido cancelado com sucesso!")
    return True
  elif answer == 'n' or answer == 'N':
    return False
  else:
    print("Resposta inválida, digite 's' ou 'n'!")
    return False