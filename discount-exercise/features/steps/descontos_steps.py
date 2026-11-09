from math import isclose

from behave import given, then, when

from client import Client


@given('um cliente de {idade:d} anos que estuda "{estuda}" e trabalha "{trabalha}"')
def criar_cliente(context, idade, estuda, trabalha):
    respostas = {"sim": True, "não": False}
    context.cliente = Client(
        "Cliente de teste", idade,
        is_student=respostas[estuda], is_worker=respostas[trabalha],
    )


@when('aplico o desconto a uma compra de {preco:f} reais')
def aplicar_desconto(context, preco):
    context.valor_final = context.cliente.discount_strategy.apply_discount(preco)


@then('o desconto deve ser de {percentual:d} por cento')
def verificar_percentual(context, percentual):
    obtido = context.cliente.discount_strategy.discount_rate * 100
    assert isclose(obtido, percentual, rel_tol=0, abs_tol=1e-9), (
        f"Desconto esperado: {percentual}%; obtido: {obtido}%"
    )


@then('o valor final deve ser {valor:f} reais')
def verificar_valor_final(context, valor):
    assert isclose(context.valor_final, valor, rel_tol=0, abs_tol=1e-9), (
        f"Valor esperado: R$ {valor:.2f}; obtido: R$ {context.valor_final:.2f}"
    )
