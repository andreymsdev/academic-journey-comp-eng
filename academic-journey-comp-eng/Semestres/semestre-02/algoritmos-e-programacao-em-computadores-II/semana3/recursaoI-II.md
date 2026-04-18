# Recursão I e II
Professor Marcelo G. Manzato

## Semana 3


Recursão é aquele conceito que parece um "bug" até que você entende que é apenas *uma função chamando a si mesma* com um problema levemente menor a cada vez.

Para que a recursão não rode para sempre `(e cause o famoso RecursionError)`, precisamos de dois ingredientes:

1. **Caso Base:** A condição de parada.

2. **Caso Recursivo:** Onde a função chama a si mesma.

---

**Exemplo I:** Fatorial: [Fatorial.py](codes/fatorial.py)

O fatorial de um número `n` (denotado como n!) é o produto de todos os números inteiros positivos de `1` até `n`. Matematicamente: `n!=n×(n−1)!`.

**Exemplo II:** Sequência de Fibonacci: [Fibonacci.py](codes/fibonacci.py)

Neste exemplo, a função se divide em duas outras chamadas. A regra é: cada número é a soma dos dois anteriores `(0,1,1,2,3,5,8,...)`.

A fórmula matemática é:
`F(n)=F(n−1)+F(n−2)`

---

**Lembretes:**

Embora a recursão seja bonita, no Python ela pode ser lenta para casos como o de Fibonacci (pois ela refaz muitos cálculos). Em situações reais, muitas vezes usamos memoização ou iteração (loops) para ganho de performance.

Basicamente a ideia é super simples: uma função que se chama. 

- Lógica de Loop: Você abre a caixa, olha se a chave está lá. Se tiver outra caixa, você a tira, coloca no chão e repete o processo até acabar.

- Lógica Recursiva: Você abre a caixa. Se tiver outra caixa dentro, você chama a "função abrir caixa" novamente para essa nova caixa. Você só para quando encontra a chave.

A recursão é muito usada em Estruturas de Dados.