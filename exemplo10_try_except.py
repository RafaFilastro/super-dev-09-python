def exemplo_sem_tratamento():
    print("Divisão: ", 10 / 0)
    # Lança a excessão: ZeroDivisionError: division by zero


def exemplo_com_tratamento():
    try:
        print("Divisão: ", 10 / 0)
    except ZeroDivisionError:
        print("Não é possivel dividir um número por zero")

    print("O programa continuou normalmente")


#ponto de entrada da aplicação, deve ter um único da aplicação inteira
if __name__ == "__main__":
    exemplo_sem_tratamento()
