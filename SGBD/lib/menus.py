import sqlite3
import os
import time
from datetime import datetime
nome_do_banco = 'sistema_aeroporto.db'

# Conecta ao banco de dados
conn = sqlite3.connect(nome_do_banco)
cursor = conn.cursor()

def limpar_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

# Função para popular o banco com informações fictícias
def popular_banco():

    # Popula CompanhiaAerea
    cursor.execute("INSERT OR IGNORE INTO CompanhiaAerea VALUES ('Companhia 1', 1, '123-456-7890')")
    cursor.execute("INSERT OR IGNORE INTO CompanhiaAerea VALUES ('Companhia 2', 2, '987-654-3210')")

    # Popula Hangar
    cursor.execute("INSERT OR IGNORE INTO Hangar VALUES (1, 10)")
    cursor.execute("INSERT OR IGNORE INTO Hangar VALUES (2, 15)")

    # Popula TipoAeronave
    cursor.execute("INSERT OR IGNORE INTO TipoAeronave VALUES (5000, 1000, 'Modelo1', 150)")
    cursor.execute("INSERT OR IGNORE INTO TipoAeronave VALUES (7000, 1200, 'Modelo2', 200)")

    # Popula Aeronave
    cursor.execute("INSERT OR IGNORE INTO Aeronave VALUES (1, 5000, 'Modelo1', 1, 1)")
    cursor.execute("INSERT OR IGNORE INTO Aeronave VALUES (2, 7000, 'Modelo2', 2, 2)")

    # Popula Piloto
    cursor.execute("INSERT OR IGNORE INTO Piloto VALUES ('Licenca1', 'Piloto1', '111-222-3333')")
    cursor.execute("INSERT OR IGNORE INTO Piloto VALUES ('Licenca2', 'Piloto2', '444-555-6666')")

    # Popula ComissarioBordo
    cursor.execute("INSERT OR IGNORE INTO ComissarioBordo VALUES (0.05, 1)")
    cursor.execute("INSERT OR IGNORE INTO ComissarioBordo VALUES (0.07, 2)")

    # Popula TecManutencao
    cursor.execute("INSERT OR IGNORE INTO TecManutencao VALUES ('Especialidade1', 3)")
    cursor.execute("INSERT OR IGNORE INTO TecManutencao VALUES ('Especialidade2', 4)")

    # Popula Passageiro
    cursor.execute("INSERT OR IGNORE INTO Passageiro VALUES ('Passageiro1', '1990-01-01', '777-888-9999', 'Brasileiro', '11111111111', 'Passaporte1')")
    cursor.execute("INSERT OR IGNORE INTO Passageiro VALUES ('Passageiro2', '1985-02-15', '999-888-7777', 'Estrangeiro', '22222222222', 'Passaporte2')")

    # Popula Voo
    cursor.execute("INSERT OR IGNORE INTO Voo VALUES ('Programado', 1, '2024-02-01 12:00:00', 'Origem1', 'Destino1')")
    cursor.execute("INSERT OR IGNORE INTO Voo VALUES ('Realizado', 2, '2024-02-02 14:30:00', 'Origem2', 'Destino2')")

    # Popula TipoServico
    cursor.execute("INSERT OR IGNORE INTO TipoServico VALUES (1, 'Servico1', 2)")
    cursor.execute("INSERT OR IGNORE INTO TipoServico VALUES (2, 'Servico2', 3)")

    # Popula Reserva
    cursor.execute("INSERT OR IGNORE INTO Reserva VALUES ('11111111111', 1, 2, '2024-02-01', '2024-01-20', 1, '2024-02-01')")

    # Popula Bagagem
    cursor.execute("INSERT OR IGNORE INTO Bagagem VALUES (1, 20.5, '11111111111', 1, '2024-02-01')")

    # Popula VooFeito
    cursor.execute("INSERT OR IGNORE INTO VooFeito VALUES (1, 'Gate1', 1, '2024-02-01')")
    cursor.execute("INSERT OR IGNORE INTO VooFeito VALUES (2, 'Gate2', 2, '2024-02-02')")

    # Popula ServicoFeito
    cursor.execute("INSERT OR IGNORE INTO ServicoFeito VALUES (1, 1, '2024-02-01')")
    cursor.execute("INSERT OR IGNORE INTO ServicoFeito VALUES (2, 2, '2024-02-02')")

    # Popula Executa
    cursor.execute("INSERT OR IGNORE INTO Executa VALUES (3, 1, 1, '2024-02-01')")
    cursor.execute("INSERT OR IGNORE INTO Executa VALUES (4, 2, 2, '2024-02-02')")

    # Popula Acompanha
    cursor.execute("INSERT OR IGNORE INTO Acompanha VALUES (1, 1, '2024-02-01')")
    cursor.execute("INSERT OR IGNORE INTO Acompanha VALUES (2, 2, '2024-02-02')")

    # Popula PodeSerFeito
    cursor.execute("INSERT OR IGNORE INTO PodeSerFeito VALUES (1, 1)")
    cursor.execute("INSERT OR IGNORE INTO PodeSerFeito VALUES (2, 2)")

    # Popula Pilotada
    cursor.execute("INSERT OR IGNORE INTO Pilotada VALUES ('Modelo1', 'Licenca1')")
    cursor.execute("INSERT OR IGNORE INTO Pilotada VALUES ('Modelo2', 'Licenca2')")

    conn.commit()
    print("Banco de dados populado com sucesso!")

# Função para inserir dados na tabela Modelo
def inserir_modelo():
    modelo = input("Modelo da aeronave: ")
    peso_max = int(input("Peso máximo: "))
    max_combustivel = int(input("Máximo de combustível: "))
    capac_passageiros = int(input("Capacidade de passageiros: "))

    cursor.execute("INSERT OR IGNORE INTO TipoAeronave VALUES (?, ?, ?, ?)",
                   (peso_max, max_combustivel, modelo, capac_passageiros))
    conn.commit()
    print("Modelo inserido com sucesso!")

# Função para consultar modelos
def consultar_modelos():
    cursor.execute("SELECT * FROM TipoAeronave")
    modelos = cursor.fetchall()

    for modelo in modelos:
        print(modelo)

# Função para atualizar o máximo de combustível de uma aeronave
def atualizar_max_combustivel():
    modelo = input("Modelo da aeronave para atualizar o máximo de combustível: ")
    novo_max_combustivel = int(input("Novo máximo de combustível: "))

    cursor.execute("UPDATE TipoAeronave SET MaxCombustivel = ? WHERE Modelo = ?", (novo_max_combustivel, modelo))
    conn.commit()
    print("Máximo de combustível atualizado com sucesso!")

# Função para excluir modelo
def excluir_modelo():
    modelo = input("Modelo da aeronave para excluir: ")

    cursor.execute("DELETE FROM TipoAeronave WHERE Modelo = ?", (modelo,))
    conn.commit()
    print("Modelo excluído com sucesso!")


# Exemplo de inserção de dados (operação de atualização)
def inserir_dados():
    status = input("Status do voo: ")
    cod_viagem = int(input("Código da viagem: "))
    horario = input("Horário do voo (YYYY-MM-DD HH:MM:SS): ")
    origem_voo = input("Origem do voo: ")
    destino_voo = input("Destino do voo: ")

    # Insere dados na tabela Voo
    cursor.execute("INSERT OR IGNORE INTO Voo VALUES (?, ?, ?, ?, ?)",
                   (status, cod_viagem, horario, origem_voo, destino_voo))
    conn.commit()
    print("Dados inseridos com sucesso!")

# Exemplo de consulta (operação de leitura)
def consultar_voos():
    cursor.execute("SELECT * FROM Voo")
    voos = cursor.fetchall()

    for voo in voos:
        print(voo)

# Exemplo de atualização de dados (operação de atualização)
def atualizar_status_voo():
    cod_viagem = int(input("Código da viagem para atualizar o status: "))
    novo_status = input("Novo status do voo: ")

    # Atualiza o status do voo
    cursor.execute("UPDATE Voo SET status = ? WHERE codViagem = ?", (novo_status, cod_viagem))
    conn.commit()
    print("Status do voo atualizado com sucesso!")

# Exemplo de exclusão de dados (operação de exclusão)
def excluir_voo():
    cod_viagem = int(input("Código da viagem para excluir: "))

    # Exclui o voo com base no código da viagem
    cursor.execute("DELETE FROM Voo WHERE codViagem = ?", (cod_viagem,))
    conn.commit()
    print("Voo excluído com sucesso!")

# Função para inserir dados na tabela Aeronave
def inserir_aeronave():
    registro = int(input("Número de registro da aeronave: "))
    combustivel_disp = int(input("Combustível disponível: "))
    modelo = input("Modelo da aeronave: ")
    num_hangar = int(input("Número do hangar: "))
    cod_companhia = int(input("Código da companhia aérea: "))

    cursor.execute("INSERT OR IGNORE INTO Aeronave VALUES (?, ?, ?, ?, ?)",
                   (registro, combustivel_disp, modelo, num_hangar, cod_companhia))
    conn.commit()
    print("Aeronave inserida com sucesso!")

# Função para consultar aeronaves
def consultar_aeronaves():
    cursor.execute("SELECT * FROM Aeronave")
    aeronaves = cursor.fetchall()

    for aeronave in aeronaves:
        print(aeronave)

# Função para atualizar o combustível disponível de uma aeronave
def atualizar_combustivel_aeronave():
    registro = int(input("Número de registro da aeronave para atualizar o combustível disponível: "))
    novo_combustivel_disp = int(input("Novo combustível disponível: "))

    cursor.execute("UPDATE Aeronave SET CombustivelDisp = ? WHERE Registro = ?", (novo_combustivel_disp, registro))
    conn.commit()
    print("Combustível disponível atualizado com sucesso!")

# Função para excluir aeronave
def excluir_aeronave():
    registro = int(input("Número de registro da aeronave para excluir: "))

    cursor.execute("DELETE FROM Aeronave WHERE Registro = ?", (registro,))
    conn.commit()
    print("Aeronave excluída com sucesso!")

# Função para inserir dados na tabela TipoAeronave
def inserir_tipo_aeronave():
    peso_max = int(input("Peso máximo da aeronave: "))
    max_combustivel = int(input("Máximo de combustível: "))
    modelo = input("Modelo da aeronave: ")
    capac_passageiros = int(input("Capacidade de passageiros: "))

    cursor.execute("INSERT OR IGNORE INTO TipoAeronave VALUES (?, ?, ?, ?)",
                   (peso_max, max_combustivel, modelo, capac_passageiros))
    conn.commit()
    print("Tipo de aeronave inserido com sucesso!")

# Função para consultar tipos de aeronaves
def consultar_tipos_aeronaves():
    cursor.execute("SELECT * FROM TipoAeronave")
    tipos_aeronaves = cursor.fetchall()

    for tipo_aeronave in tipos_aeronaves:
        print(tipo_aeronave)

# Função para atualizar o peso máximo de uma aeronave
def atualizar_peso_max_aeronave():
    modelo = input("Modelo da aeronave para atualizar o peso máximo: ")
    novo_peso_max = int(input("Novo peso máximo: "))

    cursor.execute("UPDATE TipoAeronave SET PesoMax = ? WHERE Modelo = ?", (novo_peso_max, modelo))
    conn.commit()
    print("Peso máximo atualizado com sucesso!")

# Função para excluir tipo de aeronave
def excluir_tipo_aeronave():
    modelo = input("Modelo da aeronave para excluir: ")

    cursor.execute("DELETE FROM TipoAeronave WHERE Modelo = ?", (modelo,))
    conn.commit()
    print("Tipo de aeronave excluído com sucesso!")

# Função para inserir dados na tabela Passageiro
def inserir_passageiro():
    nome = input("Nome do passageiro: ")
    data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
    telefone = input("Telefone do passageiro: ")
    nacionalidade = input("Nacionalidade do passageiro: ")
    cpf = input("CPF do passageiro: ")
    num_passaporte = input("Número do passaporte: ")

    cursor.execute("INSERT OR IGNORE INTO Passageiro VALUES (?, ?, ?, ?, ?, ?)",
                   (nome, data_nascimento, telefone, nacionalidade, cpf, num_passaporte))
    conn.commit()
    print("Passageiro inserido com sucesso!")

# Função para consultar passageiros
def consultar_passageiros():
    cursor.execute("SELECT * FROM Passageiro")
    passageiros = cursor.fetchall()

    for passageiro in passageiros:
        print(passageiro)

# Função para atualizar telefone de um passageiro
def atualizar_telefone_passageiro():
    cpf = input("CPF do passageiro para atualizar o telefone: ")
    novo_telefone = input("Novo telefone: ")

    cursor.execute("UPDATE Passageiro SET Telefone = ? WHERE CPF = ?", (novo_telefone, cpf))
    conn.commit()
    print("Telefone do passageiro atualizado com sucesso!")

# Função para excluir passageiro
def excluir_passageiro():
    cpf = input("CPF do passageiro para excluir: ")

    cursor.execute("DELETE FROM Passageiro WHERE CPF = ?", (cpf,))
    conn.commit()
    print("Passageiro excluído com sucesso!")

# Função para inserir dados na tabela Reserva
def inserir_reserva():
    cpf = input("CPF do passageiro: ")
    cod_viagem1 = int(input("Código da primeira viagem: "))
    cod_viagem2 = int(input("Código da segunda viagem: "))
    data_voo = input("Data do voo (YYYY-MM-DD): ")
    data_reserva = input("Data da reserva (YYYY-MM-DD): ")
    num_assento = int(input("Número do assento: "))
    data_voo_feito = input("Data do voo feito (YYYY-MM-DD): ")

    cursor.execute("INSERT OR IGNORE INTO Reserva VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (cpf, cod_viagem1, cod_viagem2, data_voo, data_reserva, num_assento, data_voo_feito))
    conn.commit()
    print("Reserva inserida com sucesso!")

# Função para consultar reservas
def consultar_reservas():
    cursor.execute("SELECT * FROM Reserva")
    reservas = cursor.fetchall()

    for reserva in reservas:
        print(reserva)

# Função para atualizar o número do assento em uma reserva
def atualizar_assento_reserva():
    cpf = input("CPF do passageiro para atualizar o assento: ")
    novo_assento = int(input("Novo número do assento: "))

    cursor.execute("UPDATE Reserva SET NumAssento = ? WHERE CPF = ?", (novo_assento, cpf))
    conn.commit()
    print("Número do assento na reserva atualizado com sucesso!")

# Função para excluir reserva
def excluir_reserva():
    cpf = input("CPF do passageiro para excluir a reserva: ")

    cursor.execute("DELETE FROM Reserva WHERE CPF = ?", (cpf,))
    conn.commit()
    print("Reserva excluída com sucesso!")

# Função para inserir dados na tabela Funcionario
def inserir_funcionario():
    salario = float(input("Salário do funcionário: "))
    nome = input("Nome do funcionário: ")
    identificador = int(input("Identificador do funcionário: "))
    endereco = input("Endereço do funcionário: ")
    data_nasc = input("Data de nascimento do funcionário (YYYY-MM-DD): ")

    print("\nEscolha o tipo de funcionário:")
    print("1. Comissário de Bordo")
    print("2. Técnico de Manutenção")
    tipo_funcionario = input("Digite o número da opção desejada: ")

    if tipo_funcionario == "1":
        comissao = float(input("Comissão do comissário de bordo: "))
        cursor.execute("INSERT OR IGNORE INTO ComissarioBordo VALUES (?, ?)", (comissao, identificador))
    elif tipo_funcionario == "2":
        especialidade = input("Especialidade do técnico de manutenção: ")
        cursor.execute("INSERT OR IGNORE INTO TecManutencao VALUES (?, ?)", (especialidade, identificador))
    else:
        print("Opção inválida. Inserção cancelada.")
        return

    cursor.execute("INSERT OR IGNORE INTO Funcionario VALUES (?, ?, ?, ?, ?)",
                   (salario, nome, identificador, endereco, data_nasc))
    conn.commit()
    print("Funcionário inserido com sucesso!")

# Função para consultar funcionários
def consultar_funcionarios():
    cursor.execute("SELECT * FROM Funcionario")
    funcionarios = cursor.fetchall()

    for funcionario in funcionarios:
        print(funcionario)

# Função para atualizar o endereço de um funcionário
def atualizar_endereco_funcionario():
    identificador = int(input("Identificador do funcionário para atualizar o endereço: "))
    novo_endereco = input("Novo endereço: ")

    cursor.execute("UPDATE Funcionario SET Endereco = ? WHERE Identificador = ?", (novo_endereco, identificador))
    conn.commit()
    print("Endereço do funcionário atualizado com sucesso!")

# Função para excluir funcionário
def excluir_funcionario():
    identificador = int(input("Identificador do funcionário para excluir: "))

    # Excluir também da tabela específica (ComissarioBordo ou TecManutencao)
    cursor.execute("DELETE FROM ComissarioBordo WHERE Identificador = ?", (identificador,))
    cursor.execute("DELETE FROM TecManutencao WHERE Identificador = ?", (identificador,))

    cursor.execute("DELETE FROM Funcionario WHERE Identificador = ?", (identificador,))
    conn.commit()
    print("Funcionário excluído com sucesso!")

def menu_funcionarios():
    print("Escolha qual tipo de funcionário deseja realizar a operação:")
    print("1. Comissário de Bordo")
    print("2. Técnico de Manutenção")
    print("3. Voltar ao menu principal")
    tipo_funcionario = input("Digite o número da opção desejada: ")

    if tipo_funcionario == "1":
        menu_comissarios_bordo()
    elif tipo_funcionario == "2":
        menu_tecnicos_manutencao()
    elif tipo_funcionario == "3":
        return
    else:
        print("Opção inválida. Tente novamente.")

def menu_comissarios_bordo():
    print("\nEscolha a operação:")
    print("1. Inserir dados de comissário de bordo")
    print("2. Consultar comissários de bordo")
    print("3. Atualizar comissão de comissário de bordo")
    print("4. Excluir comissário de bordo")
    escolha = input("Digite o número da operação desejada para Comissários de Bordo: ")
    if escolha == "1":
        inserir_funcionario()
    elif escolha == "2":
        consultar_funcionarios()
    elif escolha == "3":
        atualizar_endereco_funcionario()
    elif escolha == "4":
        excluir_funcionario()
    else:
        print("Opção inválida. Tente novamente.")

def menu_tecnicos_manutencao():
    print("\nEscolha a operação:")
    print("1. Inserir dados de técnico de manutenção")
    print("2. Consultar técnicos de manutenção")
    print("3. Atualizar especialidade de técnico de manutenção")
    print("4. Excluir técnico de manutenção")
    escolha = input("Digite o número da operação desejada para Técnicos de Manutenção: ")

    if escolha == "1":
        inserir_funcionario()
    elif escolha == "2":
        consultar_funcionarios()
    elif escolha == "3":
        atualizar_endereco_funcionario()
    elif escolha == "4":
        excluir_funcionario()
    else:
        print("Opção inválida. Tente novamente.")

def menu_aeronaves():
    print("\nEscolha a operação:")
    print("1. Inserir dados de aeronave")
    print("2. Consultar aeronaves")
    print("3. Atualizar combustível disponível de aeronave")
    print("4. Excluir aeronave")
    escolha = input("Digite o número da operação desejada: ")
    if escolha == "1":
        inserir_aeronave()
    elif escolha == "2":
        consultar_aeronaves()
    elif escolha == "3":
        atualizar_combustivel_aeronave()
    elif escolha == "4":
        excluir_aeronave()
    else:
        print("Opção inválida. Tente novamente.")

def menu_modelos():
    print("\nEscolha a operação:")
    print("1. Inserir dados de modelo")
    print("2. Consultar modelos")
    print("3. Atualizar máximo de combustível")
    print("4. Excluir modelo")
    escolha = input("Digite o número da operação desejada: ")
    if escolha == "1":
        inserir_tipo_aeronave()
    elif escolha == "2":
        consultar_tipos_aeronaves()
    elif escolha == "3":
        atualizar_peso_max_aeronave()
    elif escolha == "4":
        excluir_tipo_aeronave()
    else:
        print("Opção inválida. Tente novamente.")

def menu_passageiros(): 
    print("\nEscolha a operação:")
    print("1. Inserir dados de passageiro")
    print("2. Consultar passageiros")
    print("3. Atualizar telefone de passageiro")
    print("4. Excluir passageiro")
    escolha = input("Digite o número da operação desejada: ")

    if escolha == "1":
        inserir_passageiro()
    elif escolha == "2":
        consultar_passageiros()
    elif escolha == "3":
        atualizar_telefone_passageiro()
    elif escolha == "4":
        excluir_passageiro()
    else:
        print("Opção inválida. Tente novamente.")

def menu_reservas():
    print("\nEscolha a operação:")
    print("1. Inserir dados de reserva")
    print("2. Consultar reservas")
    print("3. Atualizar assento de reserva")
    print("4. Excluir reserva")
    escolha = input("Digite o número da operação desejada: ")

    if escolha == "1":
        inserir_reserva()
    elif escolha == "2":
        consultar_reservas()
    elif escolha == "3":
        atualizar_assento_reserva()
    elif escolha == "4":
        excluir_reserva()
    else:
        print("Opção inválida. Tente novamente.")


def menu_voos():   
    print("\nEscolha a operação:")
    print("1. Inserir dados de voo")
    print("2. Consultar voos")
    print("3. Atualizar status de voo")
    print("4. Excluir voo")
    escolha = input("Digite o número da operação desejada: ")

    if escolha == "1":
        inserir_dados()
    elif escolha == "2":
        consultar_voos()
    elif escolha == "3":
        atualizar_status_voo()
    elif escolha == "4":
        excluir_voo()
    else:
        print("Opção inválida. Tente novamente.")