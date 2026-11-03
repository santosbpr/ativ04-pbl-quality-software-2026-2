# Atividade 4: Testes Automatizados do LocalEats

## TDD de Breno Santos
* **Regra escolhida:** Regra 1 - verificar valor mínimo do pedido.
* **Primeiro teste escrito:** `test_pedido_atinge_valor_minimo_exato`.
* **Por que o teste falhou inicialmente:** A função `pedido_atingiu_valor_minimo` ainda não tinha sido importada ou criada para avaliar se os pedidos acima de R$ 30,00 retornavam True e abaixo retornavam False.
* **Implementação mínima realizada:** Criação da estrutura base da função retornando apenas a avaliação booleana (o mínimo necessário para o teste passar).
* **Segundo teste escrito:** `test_pedido_valor_negativo_gera_erro`.
* **Melhoria ou refatoração realizada:** Inserção da condicional para levantar a exceção `ValueError` ao receber valores negativos, conforme exigido pela regra de negócio.

## Identificação das responsabilidades
*A tabela abaixo segue o formato exigido, utilizando os identificadores TU01 e seguintes para testes unitários, e TF01 e seguintes para testes funcionais*:

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
| ------ | ------ | ------ | ------ | ------ |
| TU01 | Breno Santos | Unitário | Valor mínimo do pedido | tests/test_regras_localeats.py::test_pedido_atinge_valor_minimo_exato |
| TU02 | Breno Santos | Unitário | Pedido abaixo do mínimo | tests/test_regras_localeats.py::test_pedido_abaixo_valor_minimo |
| TU03 | Breno Santos | Unitário | Valor negativo gera erro | tests/test_regras_localeats.py::test_pedido_valor_negativo_gera_erro |
| TF01 | Breno Santos | Funcional | Apresentação da página inicial | tests/test_localeats.py::test_verificar_pagina_inicial |

## Uso de inteligência artificial
* **Ferramenta utilizada:** Gemini.
* **Como a ferramenta foi utilizada:** Apoio para estruturar a base inicial do projeto, compreender falhas de ambiente de execução, instalar dependências e criar testes com Playwright e Pytest.
* **Uma sugestão que precisou ser alterada ou rejeitada:** O código funcional sugerido inicialmente buscava um elemento genérico ("h1"), o que causou falha no teste por não refletir os elementos realmente encontrados no LocalEats. A sugestão foi alterada para utilizar a verificação de um texto real da interface.
* **Como o código sugerido foi verificado:** Através da execução do comando automatizado com pytest e análise da falha apontada no relatório final.