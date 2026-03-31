# Tipos mutáveis e não mutáveis em Python
Professor Marcelo G. Manzato

## Semana 1

**Gerenciamento de memória**

Quando fazemos uma atribuição:

```python
    >>> a = 3
```

O **objeto** `int` com valor `3` e o nome **a** são criados.

```python
    >>> a = 3
    >>> b = 3.0
    >>> c = 'hello'
    >>> d = [2, 3, 5, 8, 11]
```

--> `int`, `bool`, `float`, `str` e `complex` são **imutáveis**!

---

Já no caso de lista, o valor pode alterar: 

```python
    >>> d = [2, 3, 5, 8, 11]
    >>> d[3] = 7
```

`D` de `3` recebe `7`, ou seja altera o `4` elemento da lista. 

**Como a mutabilidade de objetos afeta a passagem de parâmetros para funções?**

```python
    def g(x)
    x = 5 

    >>> a = 3
    >>> g (a) 
```
Executando o conteúdo da função `X` recebe `5`. E a segue apontando o valor de `3`, pois foi não foi alterado.

```python
    def h (lst):
        lst[0] = 5
    
    >>> myList =[3, 6, 9, 12]
    >>> h(myList)
```