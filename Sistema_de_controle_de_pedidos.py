print("    CONTROLE DE PEDIDOS")

nome = input("Qual o seu nome? ")
pedidos = []

while True:
    pedido = input("\nDigite o item do pedido (ou 'fim' para encerrar): ")

    if pedido.lower() == "fim":
        break

    quantidade = int(input("Quantidade: "))
    cor = input("Cor: ")

    pedidos.append({
        "item": pedido,
        "quantidade": quantidade,
        "cor": cor
    })

print("\n    PEDIDOS REGISTRADOS")

if len(pedidos) == 0:
    print("Nenhum pedido foi registrado.")
else:
    for i, p in enumerate(pedidos, start=1):
        print(f"\nPedido {i}")
        print(f"Item: {p['item']}")
        print(f"Quantidade: {p['quantidade']}")
        print(f"Cor: {p['cor']}")

    print("\n    Escolha a forma de pagamento:")
    print("1 - Dinheiro")
    print("2 - Cartão")
    print("3 - Pix")

    pagamento = input("Opção: ")

    if pagamento == "1":
        forma = "Dinheiro"
    elif pagamento == "2":
        forma = "Cartão"
    elif pagamento == "3":
        forma = "Pix"
    else:
        forma = "Inválido"

    if forma == "Inválido":
        print("\nPagamento inválido.")
    else:
        print("\n    RESUMO FINAL")
        print(f"Cliente: {nome}")
        print(f"Total de pedidos: {len(pedidos)}")
        print(f"Forma de pagamento: {forma}")
        print("Pedido registrado com sucesso.")



