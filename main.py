import order
import history
import calculate_total
import payment

def finalizarPedido():
    if len(order.order) == 0:
        print("O pedido está vazio. Adicione itens antes de finalizar.")
        return

    total = calculate_total.calculate_order()
    pagamento = payment.process_paymeny(total)

    print("\n----- COMPROVANTE -----")
    
    for item in order.order:
        subtotal = item["price"] * item["quantity"]
        print(f"{item['quantity']}x {item['name']} - R${subtotal:.2f}")
        
    print(f"Total: R${total:.2f}")
    print(f"Forma de pagamento: {pagamento['forma']}")
    
    if pagamento["forma"] == "dinheiro":
        print(f"Troco: R${pagamento['troco']:.2f}")
        
    elif pagamento["forma"] == "cartao":
        print(f"{pagamento['parcelas']}x de R${pagamento['valor_parcela']:.2f}")
        
    print("------------------------\n")

    registro_pedido = {
        "itens": order.order.copy(),
        "total": total,
        "pagamento": pagamento
    }
    history.history.append(registro_pedido)
    order.order.clear()