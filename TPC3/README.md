# TPC3 

## Autor

- Nome: Maria Mendes
- Número: A113316
- Foto:
 <img width="300" alt="IMG_6232" src="https://github.com/user-attachments/assets/86a39e15-5023-43e3-9055-66513c2fda8c" />


## Resumo
Neste trabalho o objetivo era criar um jogo em Python no qual o objetivo é ser o primeiro a atingir exatamente o número 100. Para isto, o jogador e o computador alternam somando um numero de 1 a 10 ao total.

O jogo tem duas vertentes. Na primeira, o computador joga primeiro e escolhe sempre o 1, o que lhe garante a vitória. Isto acontece porque o computador consegue manter o total em 1, 12, 23, 34, ..., 89 (números que deixam resto 1 na divisão por 11), respondendo a cada jogada x do jogador com 11 - x. Assim, o total chega sempre a 100 na jogada do computador.

Na segunda vertente, o jogador joga primeiro. Neste caso, o computador só consegue vencer se o jogador falhar a estratégia: sempre que o total não estiver num dos números acima, o computador calcula a jogada que o coloca nessa sequência, ficando com o controlo do jogo. Se o jogador já estiver numa posição vencedora, o computador joga um valor aleatório e espera por um erro do adversário.

## Resultados
- [Jogo](quemchegaao100primeiro.py)
