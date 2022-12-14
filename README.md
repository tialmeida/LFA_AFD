# Autômato Finito Determinístico (AFD)

Este projeto é um trabalho entragável da disciplina de Linguagens Formais e Autômatos. 
Nele é possível encontrar um algorimo capaz de processar qualquer AFD.

> :technologist: Aluno: Tiago Almeida Santos - 2022134470

## Como utilizar
1. Instale o [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows);
2. Execute o arquivo [main.py](main.py);
3. Dê as seguintes entradas:
   1. Estados;
   2. Símbolos do alfabeto;
   3. Número total de transições;
   4. Triplas contendo:
      1. Estado de origem;
      2. Caractere de transição;
      3. Estado de destino;
   5. Estado inicial;
   6. Estados finais;
   7. Palavras de teste a serem reconhecidas;
4. Veja quais palavras são aceitas e quais não são. 

> Estados, símbolos do alfabeto, itens das triplas, estados finais e palavras de testes devem ser separados por um espaço.
> <br>Estado inicial deve ser único. E o número total de transições deve ser um número inteiro.

<br>O algoritmo foi projetado pensando nos requisitos:
- Qualquer AFD deve ser capaz de ser processada;
- A quantidade de entradas pode variar entra zero e um número finito;
- Não deve ser impresso nada além do resultado final;
- Padrão de entrada e saída definidos pelo professor;
- Não deve ser utilizado mais de um arquivo.

Após definidos os requisitos, primeiro foi necessário armazenar na memória todas 
as informações de entrada. Todos as entradas que possuíam mais de um valor possível
foram armazenadas em vetores.
Exceto no caso das triplas de transições, nas quais não foi utilizada formalmente uma estrutura de grafos, 
mas foi utilizado a classe Transtion que continha três atributos: `origin_state`, `destiny_state` e `symbol`; e foi
armazenado em um vetor uma instância da classe Transtion para cada tripla.

A complexidade de um algoritmo é analisada em termos de espaço e tempo. Levando em conta na nossa análise
apenas o tempo, podemos pensar que a complexidade desse algoritmo em específico depende do tamanho `|w|`
da palavra a ser reconhecida. Afinal, para cada símbolo da palavra será necessário percorrer a mesma quantidade
de passos e utilizar o mesmo poder computacional. Sendo assim, pode-se dizer que a complexidade desse algoritmo
é dada por `O(|w|)`.