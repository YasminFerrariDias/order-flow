history = []

def exibirHistorico():
    if len(history) == 0:
        print("Nenhum pedido foi finalizado ainda.")
        return

    print("\n===== HISTÓRICO DE PEDIDOS =====")

    for numero, pedido in enumerate(history, start=1):
        print(f"\nPedido #{numero}")

        for item in pedido["itens"]:
            print(f"  {item['quantity']}x {item['name']}")

        print(f"  Total: R${pedido['total']:.2f}")
        print(f"  Pagamento: {pedido['pagamento']['forma']}")

    print("=================================\n")