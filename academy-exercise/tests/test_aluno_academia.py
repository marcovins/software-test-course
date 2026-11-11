import pytest

from aluno_academia import ALUNO_ACADEMIA


@pytest.mark.parametrize(
    "peso, altura, esperado",
    [(72, 1.8, 22.22222222), (80, 2, 20), (54, 1.5, 24)],
    ids=["altura-decimal", "altura-inteira", "imc-24"],
)
def test_calculo_imc_com_peso_e_altura_positivos(peso, altura, esperado):
    aluno = ALUNO_ACADEMIA("Aluno", "M", peso, altura, 30)
    assert aluno.calcular_imc() == pytest.approx(esperado)


@pytest.mark.parametrize(
    "peso, altura",
    [(-70, 1.75), (0, 1.75), (70, -1.75), (70, 0),
     (-70, -1.75), (-70, 0), (0, -1.75), (0, 0)],
    ids=["peso-negativo", "peso-zero", "altura-negativa", "altura-zero",
         "ambos-negativos", "peso-negativo-altura-zero",
         "peso-zero-altura-negativa", "ambos-zero"],
)
def test_calculo_imc_com_peso_ou_altura_invalidos(peso, altura):
    aluno = ALUNO_ACADEMIA("Aluno", "M", peso, altura, 30)
    with pytest.raises(ValueError):
        aluno.calcular_imc()


@pytest.mark.parametrize(
    "sexo, idade, imc, esperado",
    [
        ("M", 40, 29.99, True),
        ("M", 41, 29, True),
        ("M", 60, 25, True),
        ("M", 18, 20, True),
        ("M", 30, 27, True),
        ("M", 39, 27.99, True),
        ("M", 39, 28, False),
        ("M", 30, 29, False),
        ("M", 40, 30, False),
        ("M", 60, 31, False),
        ("F", 40, 27.99, True),
        ("F", 41, 27, True),
        ("F", 60, 22, True),
        ("F", 18, 20, True),
        ("F", 30, 25, True),
        ("F", 39, 25.99, True),
        ("F", 39, 26, False),
        ("F", 30, 27, False),
        ("F", 40, 28, False),
        ("F", 60, 29, False),
    ],
    ids=[
        "homem-40-imc-abaixo", "homem-41-vip", "homem-60-vip",
        "homem-18-vip", "homem-30-vip", "homem-39-imc-abaixo",
        "homem-jovem-imc-no-limite", "homem-jovem-imc-acima",
        "homem-40-imc-no-limite", "homem-60-imc-acima",
        "mulher-40-imc-abaixo", "mulher-41-vip", "mulher-60-vip",
        "mulher-18-vip", "mulher-30-vip", "mulher-39-imc-abaixo",
        "mulher-jovem-imc-no-limite", "mulher-jovem-imc-acima",
        "mulher-40-imc-no-limite", "mulher-60-imc-acima",
    ],
)
def test_classificacao_vip(sexo, idade, imc, esperado):
    # Com altura de 2 m, peso = IMC * 4.
    aluno = ALUNO_ACADEMIA("Aluno", sexo, imc * 4, 2, idade)
    assert aluno.is_vip() is esperado


@pytest.mark.parametrize("sexo", ["M", "F"], ids=["homem", "mulher"])
@pytest.mark.parametrize(
    "peso, altura",
    [(0, 2), (-1, 2), (80, 0), (80, -2)],
    ids=["peso-zero", "peso-negativo", "altura-zero", "altura-negativa"],
)
def test_classificacao_vip_rejeita_medidas_invalidas(sexo, peso, altura):
    aluno = ALUNO_ACADEMIA("Aluno", sexo, peso, altura, 40)
    with pytest.raises(ValueError):
        aluno.is_vip()


@pytest.mark.parametrize(
    "sexo",
    ["M", "masculino", "Homem", " F ", "feminino", "Mulher"],
    ids=["sigla-m", "masculino", "homem", "sigla-f-com-espacos",
         "feminino", "mulher"],
)
def test_formatos_de_sexo(sexo):
    aluno = ALUNO_ACADEMIA("Aluno", sexo, 80, 2, 30)
    assert aluno.is_vip() is True


@pytest.mark.parametrize("sexo", ["", "X"], ids=["vazio", "desconhecido"])
def test_sexo_invalido(sexo):
    aluno = ALUNO_ACADEMIA("Aluno", sexo, 80, 2, 30)
    with pytest.raises(ValueError):
        aluno.is_vip()
