def calcular_multa_localidade(velocidade: float) -> float:
    if velocidade <= 50:
        return 0.0
    elif velocidade < 90:
        return 60.0
    elif velocidade < 120:
        return 120.0
    else:
        return 320.0
    
def calcular_multa_fora_localidade(velocidade: float) -> float:
    if velocidade <= 90:
        return 0.0
    elif velocidade < 120:
        return 60.0
    else:
        return 120.0
    
def calcular_multa_autoestrada(velocidade: float) -> float:
    if velocidade <= 120:
        return 0.0
    elif velocidade < 150:
        return 60.0
    elif velocidade < 175:
        return 120.0
    else:
        return 360.0

def exibir_menu() -> None:
#    Exibe o Menu de Opções:
    print("\n" + "=" * 50)
    print("CALCULADOR DE MULTAS POR EXCESSO DE VELOCIDADE")
    print("=" * 50)
    print("1 - Localidade")
    print("2 - Fora da Localidade")
    print("3 - Autoestrada")
    print("4 - sair")
    print("=" * 50)

def main() -> None:
#   Função principal do programa:
    while True:
        exibir_menu()
        opcao = input("Selecione o tipo de via (1-3) ou sair do programa (4): ").strip()

        if opcao == '4':
            print("\nObrigado por utilizar o sistema. até logo!")
            break

        try:
            velocidade = float(input("Digite a velocidade do veículo (km/h): ").strip())
            
            if velocidade <= 0:
                print("A Velocidade deve ser um valor positivo!")
                continue
        
        except ValueError:
            print("Erro: Por Favor, digite um valor numérico válido!")
            continue

        if opcao == '1':
            multa = calcular_multa_localidade(velocidade)
            tipo_via = "Localidade"
        elif opcao == '2':
            multa = calcular_multa_fora_localidade(velocidade)
            tipo_via = "Fora da Localidade"
        elif opcao == '3':
            multa = calcular_multa_autoestrada(velocidade)
            tipo_via = "Autoestrada"
        else:
            print("Opção inválida! Por favor, selecione uma opção válida.")
            continue

        print("\n" + "=" * 50)
        print(f"Tipo de Via: {tipo_via}")
        print(f"Velocidade registrada: {velocidade} km/h")
        
        if multa > 0:
            print(f"VALOR DA MULTA: €{multa:.2f}")
        else:
            print("Nenhuma multa aplicada. Velocidade dentro do limite permitido.")
        
        print("=" * 50)

if __name__ == "__main__":
    main()