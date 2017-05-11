### >>> Comandos Básicos <<<

=== <p>
#### >>> Tipos de variáveis:
````programming  

>>> type(5)
<class 'int'>

>>> type(5.2)
<class 'float'>

>>> type("texto")
<class 'str'>

>>> type(True) # Atenção para a inicial maiúscula
<class 'bool'>

>>> type(False) # Atenção para a inicial maiúscula
<class 'bool'>
````

=== <p>
#### >>> Operadores:
````programming
+  adição
-  subtração
*  multiplicação
**  potência
/  divisão ( sempre resultará em um número decimal)
//  divisão com resultado inteiro
%  "resto da divisão"

Operadores relacionais:
== igual
!= diferente
> maior
< menor
>= maior ou igual
<= menor ou igual

>>> 2+3
5
>>> 6-2
4
>>> 7*3
21
>>> 2**5
32
>>> 4/2
2.0
>>> 5/2
2.5
>>> 2/3
0.6666666666666666
>>> 5/3
1.6666666666666667
>>> 7/3
2.3333333333333335
>>> 4//2
2
>>> 5//2
2
>>> 4%2
0
>>> 5%2
1
>>>  100 == 10*10
True
>>> 100 != 10*10
False
````
=== <p>
#### >>> Lista as funções nativa do python
````programming
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
````
=== <p>
#### >>> Ajuda sobre as funções nativas

Os argumentos entre parêntesesm são opcionais, o restante são obrigatórios.
````programing
>>> help(max)
Help on built-in function max in module builtins:

max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
````
=== <p>
#### >>> Importar módulos (ou pacotes) que contenham funções que deseja usar
````programing
import math

# Listando todas as funções contidas no módulo `math`
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

=== <p>
#### >>> Acessando o help da função `sqrt`
>>>help(math.sqrt)
Help on built-in function sqrt in module math:

sqrt(...)
    sqrt(x)
    
    Return the square root of x.

# Usando a função `sqrt`
>>> math.sqrt(4)
2.0

# Acessando constantes presentes no módulo `math`
>>> math.pi
3.141592653589793
````
=== <p>
#### >>> Funções:
##### Formato padrão de uma função

````programming
def nome_da_função (argumentos_da_função):
    # Linhas de comandos com recuo!
    Linhas de comando da função
    return (objeto resultado da função)
    # linha vazia
# Fim do Recuo.

# Exemplo
def minha_funcao (x):
    y=x**2
    return (y)

minha_funcao(5)
25
````
As variáveis criadas podem ser globais ou locais. Serão locais aquelas variáveis criadas dentro de uma função. 
Serão globais as variáveis criadas fora de uma função.
Sendo uma variável global `z`, ela não é alterar por uma função sem usar o comando `global`. Exemplo:

```` programming
x= 10

def minha_funcao (x):
    y=x**2
    x= 15
    return (y)


minha_funcao(5)
25
print(x)
10
````
```` programming
z= 10

def minha_funcao (x):
    y=x**2
    z= 15
    return (y)

minha_funcao(5)
25
print(z)
10
````

```` programming
z= 10

def minha_funcao (x):
    global z
    y=x**2
    z= 15
    return (y)

minha_funcao(5)
25
print(z)
15
````
=== <p>
#### >>> Input de dados
##### Pode se fazer um input de dado interativamente a partir do teclado, solicitando ao usuário que digite-o. O interpretador fica aguardando que o dado seja inserido para continuar a executar o restante do código. Todo dado inserido por meio da função `input` é interpredado como `string`, portanto ao usar números é necessário fazer a conversão usando `int`ou `float`. Exemplo:
```` programming
# Entrada da temperatura em Fahrenheit
F = float(input("Digite a temperatura em Fahrenheit: "))
>>> Digite a temperatura em Fahrenheit: 
````
