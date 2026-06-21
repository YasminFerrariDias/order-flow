def process_payment(total):
  payment_method = None
    
  while payment_method not in ["dinheiro", "cartao", "pix"]:
    payment_method = input("Forma de pagamento (dinheiro/cartao/pix): ").lower()
        
    if payment_method not in ["dinheiro", "cartao", "pix"]:
      print("Forma de pagamento inválida, tente novamente!")
        
  payment_details = {"forma": payment_method}
    
  if payment_method == "dinheiro":
    amount_paid = None
        
    while amount_paid is None or amount_paid < total:
      amount_paid = float(input(f"Total: R${total:.2f}. Valor pago: R$"))
            
      if amount_paid < total:
        print("Valor pago insuficiente, tente novamente!")
        
    change = amount_paid - total
    payment_details["amount_paid"] = amount_paid
    payment_details["change"] = change
    print(f"Troco: R${change:.2f}")
        
  elif payment_method == "cartao":
    installments = None
        
    while installments is None or installments < 1 or installments > 3:
      installments = int(input("Em quantas parcelas (1 a 3)? "))
            
      if installments < 1 or installments > 3:
        print("Número de parcelas inválido, tente novamente.")
        
    installment_value = total / installments
    payment_details["installments"] = installments
    payment_details["installment_value"] = installment_value
    print(f"{installments}x de R${installment_value:.2f}")
        
  elif payment_method == "pix":
    print(f"Pagamento de R${total:.2f} via Pix confirmado!")
    
  return payment_details