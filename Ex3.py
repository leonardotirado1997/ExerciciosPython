import math

# Exercício 3: Calcular sen⁻¹(x) em graus considerando o quadrante

print("=" * 60)
print("EXERCÍCIO 3 - CÁLCULO DE ARCO SENO COM QUADRANTE")
print("=" * 60)

# Entrada dos dados
x = float(input("Digite o valor de x (entre -1 e 1): "))
q = int(input("Digite o quadrante (1, 2, 3 ou 4): "))

# Verificar se |x| > 1 (erro)
if abs(x) > 1:
    print("ERRO: |x| deve ser menor ou igual a 1!")
else:
    # Calcular o arco seno principal em radianos
    arco_rad = math.asin(x)
    
    # Converter para graus (valor principal entre -90° e 90°)
    arco_graus_principal = math.degrees(arco_rad)
    
    print(f"\nValor principal de sen⁻¹({x}) = {arco_graus_principal:.2f}°")
    print(f"Quadrante escolhido: {q}")
    
    # Ajustar o ângulo de acordo com o quadrante
    if q == 1:
        # 1° quadrante: 0° a 90°
        angulo = arco_graus_principal
        # Se for negativo, não pertence ao Q1
        if angulo < 0:
            print(f"ATENÇÃO: {angulo:.2f}° não está no 1° quadrante!")
        else:
            print(f"Ângulo no 1° quadrante: {angulo:.2f}°")
    
    elif q == 2:
        # 2° quadrante: 90° a 180°
        # sen(θ) = sen(180° - θ)
        angulo = 180 - arco_graus_principal
        print(f"Ângulo no 2° quadrante: {angulo:.2f}°")
    
    elif q == 3:
        # 3° quadrante: 180° a 270°
        # sen(θ) = sen(180° + θ) onde θ é negativo
        angulo = 180 - arco_graus_principal
        # Ajuste para o 3° quadrante (180° + |θ|)
        angulo = 180 + abs(arco_graus_principal)
        print(f"Ângulo no 3° quadrante: {angulo:.2f}°")
    
    elif q == 4:
        # 4° quadrante: 270° a 360°
        angulo = 360 + arco_graus_principal  # arco_graus_principal é negativo
        print(f"Ângulo no 4° quadrante: {angulo:.2f}°")
    
    else:
        print("ERRO: Quadrante inválido! Digite 1, 2, 3 ou 4.")
    
    # Verificação do seno
    seno_calculado = math.sin(math.radians(angulo))
    print(f"\nVerificação: sen({angulo:.2f}°) = {seno_calculado:.4f} (original: {x})")