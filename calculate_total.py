import order

def calculate_order():
  total = 0

  for item in order.order:
        total += item["price"] * item["quantity"]

  if total > 100:
    total = total * 0.95
    print("Desconto de 5% aplicado (pedido acima de R$100)!")

  resposta = input("Deseja incluir taxa de serviço de 10%? (sim/não) ")
  
  if resposta.lower() == "sim":
    total = total * 1.10
    
  return total