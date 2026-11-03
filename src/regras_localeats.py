def pedido_atingiu_valor_minimo(valor_pedido):
    if valor_pedido < 0:
        raise ValueError("Valores negativos geram erro.")
    return valor_pedido >= 30.00