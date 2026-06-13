# Algoritmo para calcular raízes reais de uma equação quadrática
# Usando a fórmula de Bhaskara: ax² + bx + c = 0

import math

def calcular_raizes(a, b, c):
    """
    Calcula as raízes reais da equação quadrática ax² + bx + c = 0
    """
    print(f"\nEquação: {a}x² + {b}x + {c} = 0")
    
    # Passo 1: Verificar se é uma equação quadrática válida
    if a == 0:
        print("ERRO: 'a' não pode ser zero. Não é uma equação quadrática!")
        return None
    
    # Passo 2: Calcular o discriminante (delta)
    delta = b**2 - 4*a*c
    print(f"Passo 1: Delta = b² - 4ac = {b}² - 4·{a}·{c} = {delta}")
    
    # Passo 3: Analisar o valor de delta
    if delta < 0:
        print("Passo 2: Delta é negativo (", delta, ")")
        print("Resultado: Não existem raízes reais!")
        return None
    
    elif delta == 0:
        print("Passo 2: Delta é igual a zero")
        # Raiz única (raiz dupla)
        x = -b / (2*a)
        print(f"Passo 3: x = -b / (2a) = -{b} / (2·{a}) = {x}")
        print(f"Resultado: A equação tem uma raiz real: x = {x}")
        return x
    
    else:  # delta > 0
        print("Passo 2: Delta é positivo (", delta, ")")
        print("Passo 3: Calcular as duas raízes:")
        
        # Calcular as duas raízes
        raiz_delta = math.sqrt(delta)
        print(f"   √Δ = √{delta} = {raiz_delta:.4f}")
        
        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*a)
        
        print(f"   x1 = (-b + √Δ) / (2a) = (-{b} + {raiz_delta:.4f}) / {2*a} = {x1:.4f}")
        print(f"   x2 = (-b - √Δ) / (2a) = (-{b} - {raiz_delta:.4f}) / {2*a} = {x2:.4f}")
        
        print(f"Resultado: A equação tem duas raízes reais: x1 = {x1:.4f} e x2 = {x2:.4f}")
        return (x1, x2)


# Programa principal com exemplos
if __name__ == "__main__":
    print("=" * 60)
    print("CALCULADORA DE EQUAÇÕES QUADRÁTICAS - FÓRMULA DE BHASKARA")
    print("=" * 60)
    
    # Exemplo 1: duas raízes reais diferentes
    print("\n--- EXEMPLO 1: Duas raízes reais ---")
    calcular_raizes(1, -5, 6)  # x² - 5x + 6 = 0 → raízes: 2 e 3
    
    # Exemplo 2: raiz dupla
    print("\n--- EXEMPLO 2: Raiz dupla ---")
    calcular_raizes(1, 4, 4)   # x² + 4x + 4 = 0 → raiz: -2
    
    # Exemplo 3: sem raízes reais
    print("\n--- EXEMPLO 3: Sem raízes reais ---")
    calcular_raizes(1, 2, 5)   # x² + 2x + 5 = 0 → delta negativo
    
    # Entrada interativa
    print("\n" + "=" * 60)
    print("ENTRADA INTERATIVA")
    print("=" * 60)
    
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        
        calcular_raizes(a, b, c)
    except ValueError:
        print("ERRO: Digite números válidos!")