# PROJETO – PICKING: RECOLHA DE PRODUTOS EM ARMAZÉNS

## 📜 Descrição do Problema

Este projeto visa o desenvolvimento de uma aplicação para otimizar a recolha de produtos das prateleiras de um armazém, processo denominado de _picking_. O sistema busca:

- Distribuir os _picks_ (produtos) pelos agentes de recolha.
- Definir a sequência de recolha dos produtos por cada agente para minimizar o tempo de entrega do último produto no ponto de entrega.
- Minimizar a distância total percorrida pelos agentes.
- Reduzir o número de colisões entre os agentes.

### 📄 Estrutura de Dados

O programa começa por solicitar ao utilizador a escolha do problema a ser resolvido, armazenado num ficheiro de texto. O exemplo a seguir ilustra um destes ficheiros:

    19, 21
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    2 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1
    1 0 2 1 0 1 1 0 2 1 0 1 1 0 1 1 0 1 1 0 1
    1 0 1 1 0 1 1 0 1 1 0 2 1 4 1 2 0 1 1 0 1
    1 0 2 1 0 1 2 0 1 1 0 1 1 0 1 1 0 1 1 0 1
    1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1
    1 0 1 1 0 1 1 0 1 1 0 2 1 0 1 1 0 1 1 0 1
    1 4 1 1 0 1 2 0 1 2 0 1 1 0 1 1 0 1 2 0 1
    1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1
    1 0 1 1 0 1 1 0 1 1 0 1 1 0 2 1 0 1 1 0 1
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1
    1 0 1 1 0 1 1 0 1 2 0 1 1 0 1 1 0 1 1 0 1
    1 0 1 1 0 1 1 0 1 1 4 2 2 0 2 1 0 2 1 0 2
    1 0 1 2 0 1 1 0 1 1 0 1 1 0 1 2 0 1 1 0 1
    1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1
    0 0 0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0


A primeira linha indica as dimensões do armazém. Segue-se uma matriz que descreve:

- A estrutura do armazém.
- Posição dos produtos.
- Ponto de recolha.
- Posição inicial dos agentes.

Os valores na matriz são interpretados da seguinte forma:
- **0**: Espaço livre.
- **1**: Prateleira vazia.
- **2**: Prateleira com produto a ser recolhido.
- **3**: Ponto de entrega.
- **4**: Agente.

Após a atribuição dos produtos aos agentes, cada agente movimenta-se de forma ótima até cada produto designado e, após recolher todos, dirige-se ao ponto de entrega. Considera-se que um agente recolhe um produto ao passar pela célula adjacente ao produto.

### ⚠️ Detecção de Colisões

Dois agentes colidem ao tentar ocupar a mesma célula simultaneamente. O foco deste projeto não é achar um caminho alternativo após a colisão, mas sim detetar colisões e penalizar soluções que as contenham. O processo evolutivo favorece soluções sem colisões, visando encontrar a melhor solução possível sem incidentes.
