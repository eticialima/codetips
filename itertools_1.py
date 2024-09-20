import itertools

# Cria um contador que começa em 2000 e continua indefinidamente (não utilizado aqui)
itertools.count(2000)

# Cria um iterador que repete infinitamente as cores 'red', 'yellow', 'green' (não utilizado aqui)
itertools.cycle(['red', 'yellow', 'green'])

# Aplica a função pow(base, exp) em cada número de 0 a 9 (range(10)), elevando-os ao quadrado (exp = 2)
response = list(map(pow, range(10), itertools.repeat(2)))

# Imprime a lista de números ao quadrado
print(response) 