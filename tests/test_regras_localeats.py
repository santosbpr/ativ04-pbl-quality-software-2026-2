import pytest
from src.regras_localeats import pedido_atingiu_valor_minimo

# Responsável: [Breno Santos]
def test_pedido_atinge_valor_minimo_exato():
    resultado = pedido_atingiu_valor_minimo(30.00)
    assert resultado is True

# Responsável: [Breno Santos]
def test_pedido_abaixo_valor_minimo():
    resultado = pedido_atingiu_valor_minimo(29.99)
    assert resultado is False

# Responsável: [Breno Santos]
def test_pedido_valor_negativo_gera_erro():
    with pytest.raises(ValueError):
        pedido_atingiu_valor_minimo(-5.00)