# Código pego do site:
# https://www.ime.usp.br/~vwsetzer/python-exemplos.html


class Fibonacci:
    def __init__(self, n):
        self.N = n  # Número de ordem de cada elemento da sequência
        self.fib_a = 1
        self.fib_b = 1

    def calcula_fib(self):
        if self.N < 2:
            raise ValueError("O valor mínimo de N deve ser 2")

        for i in range(2, self.N):
            aux = self.fib_a + self.fib_b  # Cada novo elemento será a soma dos dois anteriores
            self.fib_a = self.fib_b  # O segundo elemento torna-se o primeiro
            self.fib_b = aux  # O segundo elemento recebe a soma dos dois anteriores

        return self.fib_b


if __name__ == "__main__":
    limite = int(input('Entre com o N (>= 2): '))
    f = Fibonacci(limite)
    fib = f.calcula_fib()
    print(f"O fibonacci de {limite} é {fib}")
