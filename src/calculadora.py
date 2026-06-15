def calcula_desconto(preco_base: float, desconto: int) -> float:
    if preco_base < 0:
        raise ValueError("Preço base não pode ser negativo")
    if desconto < 0 or desconto > 100:
        raise ValueError("Desconto deve estar entre 0 e 100")
    valor_com_desconto = preco_base - ((preco_base * desconto) / 100)
    return round(valor_com_desconto, 2)


def calcula_imposto(preco: float, aliquota_imposto: float) -> float:
    if aliquota_imposto < 0:
        raise ValueError("Alíquota não pode ser negativa")
    valor_com_imposto = preco + ((preco * aliquota_imposto) / 100)
    return round(valor_com_imposto, 2)


def calcula_preco_final(preco_base: float, desconto: int, aliquota_imposto: float) -> float:
    preco_com_desconto = calcula_desconto(preco_base, desconto)
    preco_com_imposto = calcula_imposto(preco_com_desconto, aliquota_imposto)
    return preco_com_imposto


if __name__ == "__main__":
    preco_base = float(input("Informe o preço base: "))
    desconto = int(input("Informe o desconto: "))
    aliquota_imposto = float(input("Informe a aliquota de imposto: "))
    print(calcula_preco_final(preco_base, desconto, aliquota_imposto))