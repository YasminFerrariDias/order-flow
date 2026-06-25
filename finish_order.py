import order
import history
from calculate_order import calculate_order
from process_payment import process_payment

def finish_order():
  if len(order.order) == 0:
    print("O pedido está vazio. Adicione itens antes de finalizar.")
    return False

  total = calculate_order()
  payment = process_payment(total)

  print("\n----- COMPROVANTE -----")

  for item in order.order:
    subtotal = item["price"] * item["quantity"]
    print(f"{item['quantity']}x {item['name']} - R${subtotal:.2f}")

  print(f"Total: R${total:.2f}")
  print(f"Forma de pagamento: {payment['forma']}")

  if payment["forma"] == "dinheiro":
    print(f"Troco: R${payment['change']:.2f}")

  elif payment["forma"] == "cartao":
    print(f"{payment['installments']}x de R${payment['installment_value']:.2f}")

  print("------------------------\n")

  order_record = {
    "items": order.order.copy(),
    "total": total,
    "payment": payment
  }

  history.history.append(order_record)
  order.order.clear()
  return True