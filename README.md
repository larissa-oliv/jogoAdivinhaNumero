# Jogo de Adivinhação de Números

## Descrição
Este é um projeto de estudo simples de um jogo de adivinhação de números em Python. O objetivo do jogo é adivinhar um número secreto escolhido aleatoriamente pelo computador dentro de um limite de tentativas.

## Regras do Jogo
- O computador escolhe um número aleatório entre 1 e 10.
- O jogador tem 3 tentativas para adivinhar o número secreto.
- O jogador recebe dicas se o palpite está "muito baixo" ou "muito alto".
- Se o jogador adivinhar corretamente, o jogo exibe uma mensagem de vitória.
- Se o jogador não adivinhar em 3 tentativas, o jogo revela o número secreto e encerra.

## Funcionalidades
- Limite de tentativas para adivinhar o número.
- Feedback para o jogador em cada palpite.
- Mensagem final indicando sucesso ou revelando o número secreto.

## Como Executar
1. **Clone este repositório**:
    ```sh
    git clone https://github.com/larissa-oliv/jogoAdivinhaNumero.git
    ```

2. **Navegue até o diretório do projeto**:
    ```sh
    cd jogoAdivinhaNumero
    ```

3. **Execute o jogo**:
    ```sh
    python adivinha_numero.py
    ```

## Exemplo de Execução
```plaintext
Bem-vindo ao jogo de adivinhação!
Estou pensando em um número entre 1 e 10.
Você tem 3 tentativas para adivinhar.
Faça um palpite: 5
Muito alto!
Faça um palpite: 3
Muito baixo!
Faça um palpite: 4
Parabéns! Você acertou o número 4 em 3 tentativas.
