import menu
import order

def process_paymeny(total):
  forma_pagamento = None
  
  while forma_pagamento not in ["dinheiro", "cartao", "pix"]:
    forma_pagamento = input("Forma de pagamento (dinheiro/cartao/pix): ").lower()
    
    if forma_pagamento not in ["dinheiro", "cartao", "pix"]:
      print("Forma de pagamento inválida, tente novamente!")
      
  detalhes_pagamento = {"forma": forma_pagamento}
  
  if forma_pagamento == "dinheiro":
    valor_pago = None
    
    while valor_pago is None or valor_pago < total:
      valor_pago = float(input(f"Total: R%{total:2.f}. Valor pago: R%"))
      
      if valor_pago < total:
        print("valor pago insuficiente, tente novamente!")
    
    troco = valor_pago - total
    detalhes_pagamento["valor_pago"] = valor_pago
    detalhes_pagamento["troco"] = troco
    print(f"Troco: R${troco:.2f}")
    
  elif forma_pagamento == "cartao":
    parcelas = None
 
    while parcelas is None or parcelas < 1 or parcelas > 3:
      parcelas = int(input("Em quantas parcelas (1 a 3)? "))
 
      if parcelas < 1 or parcelas > 3:
        print("Número de parcelas inválido, tente novamente.")
 
    valor_parcela = total / parcelas
    detalhes_pagamento["parcelas"] = parcelas
    detalhes_pagamento["valor_parcela"] = valor_parcela
    print(f"{parcelas}x de R${valor_parcela:.2f}")
 
  elif forma_pagamento == "pix":
    print(f"Pagamento de R${total:.2f} via Pix confirmado!")
 
    return detalhes_pagamento