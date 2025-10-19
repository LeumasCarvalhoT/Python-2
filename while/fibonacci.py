print('Sequência de Fibonacci')
fib = int(input('Quantos termos você quer exibir?: '))
c = 1
a = 0
b = 1
f = 0
print('{} -> {} -> '.format(a, b), end='')
while c != fib - 1:
    f = a + b
    a = b
    b = f
    c += 1
    print('{} -> '.format(f), end='')
print('FIM')