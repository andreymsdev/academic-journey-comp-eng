# Estruturas de repetição - for
Professor Marcelo G. Manzato

## Semana 6

Estruturas de controle de fluxo que permitem repetir uma sequência de comandos. 

Número de repetições pode ser indeterminado, porém deve ser *finito*.

**Comando for**

```python
for <variável> in <sequencia>:
    <bloco de código indentado>
<bloco de código não indentado>
```

---

```python
l = ['cao', 'gato', 'coelho']
for i in l:
    print(i)
```
[Lista](codes/lista.py)
---

```python
s = 'algoritmos'
for c in s:
    if c in 'aeiou'
        print(c)
```

---
```python
função range(). formato:

range (star,stop, step)
```
---

```python
for x in range(10):
    print(x)
```
[Range](codes/range.py)

---

**Acumuladores**

São variáveis pra ir agregando somas parciais.

*exemplo*
Como calcular a soma de todos os números pares de 1 a 100?
> [Exemplo 1](codes/acumuladores.py)
> [Exemplo 2](codes/loopsalinhados.py)