import pytest
from src.calculadora import calcula_preco_final, calcula_desconto, calcula_imposto

pytestmark = pytest.mark.unit

# -- Validações caminhos válidos: desconto -- 
@pytest.mark.parametrize("preco, desconto, esperado", [
    (100, 10, 90.00),
    (100, 0, 100.0),
    (100, 100, 0.0),
])
def test_desconto_valido(preco, desconto, esperado):
    assert calcula_desconto(preco, desconto) == esperado

# -- Validações caminhos válidos: imposto -- 
@pytest.mark.parametrize("preco, aliquota, esperado", [
    (90, 10, 99.0),
    (100, 0, 100.0),
])
def test_imposto_valido(preco, aliquota, esperado):
    assert calcula_imposto(preco, aliquota) == esperado

# -- Validações caminhos válidos: fluxo completo --
def test_calculadora_completa():
    assert calcula_preco_final(100, 10, 18) == 106.2

# -- Erros: todas as entradas inválidas juntas --
@pytest.mark.parametrize("preco, desconto, aliquota", [
    (100, 101, 10),    # desconto maior que 100%
    (100, -10, 10),    # desconto negativo
    (100, 10, -10),    # imposto negativo
    (-100, 10, 10),    # preço negativo
])
def test_entradas_invalidas_levantam_erro(preco, desconto, aliquota):
    with pytest.raises(ValueError):
        calcula_preco_final(preco, desconto, aliquota)