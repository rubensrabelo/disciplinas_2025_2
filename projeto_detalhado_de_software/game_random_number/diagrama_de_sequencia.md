*Listar as responsabilidades:*

*Ator:*
Usuário

*Entidades:*
1. ValidarNumero:
    * numeroIgual
2. GerarNumeroAleatorio:
    * gerarNumero
3. DiferencaNumero:
    * informarMaiorOuMenor
4. Jogo:
    * informarResultado
4. Menu:
    * gerarMenu


---

```mermaid
sequenceDiagram
    actor Usuario
    participant ValidarNumero
    participant GerarNumeroAleatorio
    participant DiferencaNumero
    participant Jogo
    Cliente ->> Garcom: Chama
    Garcom ->> Pedido: Anota o pedido
    Pedido ->> Pagamento: Coloca status como aberto
    Pedido ->> Cozinha: Manda pedido
    Cozinha ->> Pedido: Muda Status para recebido
    Cozinha ->> Pedido: Muda Status para em preparo
    Cozinha ->> Pedido: Muda Status para feito
    Pedido -->> Garcom: Manda notificação de pronto
    Garcom ->> Cliente: Manda pedido
    Garcom ->> Pedido: Muda Status para entregue
    Cliente ->> Garcom: Pede a conta
    Garcom ->> Pagamento: Escolhe a forma de pagamento
    Pagamento -->> Cliente: Gera a fonte de pagamento
    Pagamento ->> Pagamento: Muda status para pago
    Pagamento ->> Caixa: Envia notificação de pagamento
    Caixa -->> Cliente: Manda recibo de pagamento
```