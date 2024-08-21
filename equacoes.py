import math

def menu():
    print(" 1 - Calcular equação 1° grau.")
    print(" 2 - Calcular equação 2° grau.")
    print(" 3 - Sair do Programa.")

# equacao 2 grau
def calcular_grau_2(a, b, c):
    delta = (b**2)-(4*a*c)
    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0 :
        return f"Valor de x é {(-b)/(2*a)}." 
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta/(2*a))
        x2 = (-b - raiz_delta/(2*a))
        yield f"Valor de x1: {x1}."
        yield f"Valor de x2: {x2}."
# equacao 1 grau
calcular_grau_1 = lambda a,b: -b/a

