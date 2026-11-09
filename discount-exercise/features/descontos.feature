# language: pt
Funcionalidade: Descontos conforme idade e situação do cliente
  Como responsável pelas vendas
  Quero aplicar os descontos previstos nas regras do negócio
  Para cobrar o valor correto de cada cliente

  Esquema do Cenário: Menor de 18 anos que somente estuda recebe 5 por cento
    Dado um cliente de <idade> anos que estuda "sim" e trabalha "não"
    Quando aplico o desconto a uma compra de 200.00 reais
    Então o desconto deve ser de 5 por cento
    E o valor final deve ser 190.00 reais

    Exemplos:
      | idade |
      | 16    |
      | 17    |

  Esquema do Cenário: Menor de 18 anos que estuda e trabalha recebe 8 por cento
    Dado um cliente de <idade> anos que estuda "sim" e trabalha "sim"
    Quando aplico o desconto a uma compra de 200.00 reais
    Então o desconto deve ser de 8 por cento
    E o valor final deve ser 184.00 reais

    Exemplos:
      | idade |
      | 16    |
      | 17    |

  Esquema do Cenário: Entre 18 e 60 anos quem somente estuda não recebe desconto
    Dado um cliente de <idade> anos que estuda "sim" e trabalha "não"
    Quando aplico o desconto a uma compra de 200.00 reais
    Então o desconto deve ser de 0 por cento
    E o valor final deve ser 200.00 reais

    Exemplos:
      | idade |
      | 18    |
      | 30    |
      | 60    |

  Esquema do Cenário: Entre 18 e 60 anos quem estuda e trabalha recebe 15 por cento
    Dado um cliente de <idade> anos que estuda "sim" e trabalha "sim"
    Quando aplico o desconto a uma compra de 200.00 reais
    Então o desconto deve ser de 15 por cento
    E o valor final deve ser 170.00 reais

    Exemplos:
      | idade |
      | 18    |
      | 30    |
      | 60    |

  Esquema do Cenário: Acima de 60 anos o desconto é de 10 por cento independentemente da ocupação
    Dado um cliente de <idade> anos que estuda "<estuda>" e trabalha "<trabalha>"
    Quando aplico o desconto a uma compra de 200.00 reais
    Então o desconto deve ser de 10 por cento
    E o valor final deve ser 180.00 reais

    Exemplos:
      | idade | estuda | trabalha |
      | 61    | não    | não      |
      | 61    | sim    | não      |
      | 61    | não    | sim      |
      | 61    | sim    | sim      |
      | 64    | sim    | sim      |
      | 65    | não    | não      |
      | 70    | não    | não      |
