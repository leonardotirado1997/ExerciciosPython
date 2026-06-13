# Exercício 4: Determinar número de termos para série exceder 10.000
# Série: 5k² - 2k, para k = 1, 2, 3, ...

print("\n" + "=" * 60)
print("EXERCÍCIO 4 - SÉRIE 5k² - 2k")
print("=" * 60)

# Inicialização
soma = 0           # Acumulador da soma
k = 0              # Contador de termos
limite = 10000     # Limite a ser excedido

print("Calculando termos até a soma exceder 10.000...")
print("-" * 50)
print("k     | Termo (5k² - 2k) | Soma acumulada")
print("-" * 50)

# Enquanto a soma não exceder o limite, continuar
while soma <= limite:
    k = k + 1                    # Próximo termo
    termo = 5 * k**2 - 2 * k     # Calcular o termo atual
    soma = soma + termo          # Adicionar à soma
    
    # Exibir o progresso a cada passo
    print(f"{k:3d}    | {termo:12d}      | {soma:12.0f}")
    
    # Se excedeu o limite e é o último termo, destacar
    if soma > limite and k > 0:
        print("-" * 50)
        print(f"✓ Soma EXCEDEU {limite}!")

print("-" * 50)
print(f"\nRESULTADO FINAL:")
print(f"Número de termos necessários: {k}")
print(f"Último termo calculado (k={k}): {termo}")
print(f"Soma total: {soma:.0f}")
print(f"Limite: {limite}")

# Verificação
print(f"\nVerificação: A soma {soma:.0f} > {limite}? {soma > limite}")