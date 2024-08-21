import equacoes as eq

if __name__ == "__main__":
    while True:
        eq.menu()
        opcoes = input("Escolha a opção: ")
        match opcoes:
            case "1":
                a = float(input("valor de 'a': ").replace(",","."))
                b = float(input("valor de 'b': ").replace(",","."))
                print(f"valor de x: {eq.calcular_grau_1(a, b)}.")
                continue
            case "2":
                a = float(input("valor de 'a': ").replace(",","."))
                b = float(input("valor de 'b': ").replace(",","."))
                c = float(input("valor de 'c': ").replace(",","."))
                result = eq.calcular_grau_2(a, b, c)
                for x in result:
                    print(x)
                continue
            case "3":
                print("saindo do programa")
                break
            case _:
                print("Opção Inválida")
                continue