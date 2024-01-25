from lib.menus import *

# Interagir com o usuário
if __name__ == "__main__":
    popular_banco() #Descomentar apenas se o banco não estiver preenchido
    while True:
            print("Escolha qual informação deseja realizar uma operação")
            print("1. Voos")
            print("2. Aeronave")
            print("3. Modelos de Aeronave")
            print("4. Passageiros")
            print("5. Reservas")
            print("6. Funcionários")
            print("7. Encerrar Sistema")

            escolha = input("Digite o número da operação desejada: ")
            limpar_terminal()
            if escolha == "1":
                menu_voos()
            elif escolha == "2":
                menu_aeronaves()
            elif escolha == "3":
                menu_modelos()
            elif escolha == "4":
                menu_passageiros()
            elif escolha == "5":
                menu_reservas()
            elif escolha == "6":
                menu_funcionarios()
            elif escolha == "7":
                print("Saindo do sistema.")
                break
            else:
                limpar_terminal()
                print("Opção inválida. Tente novamente.")
            escolha = input("Presione qualquer tecla")
            limpar_terminal()


    
