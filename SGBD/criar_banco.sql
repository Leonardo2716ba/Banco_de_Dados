CREATE TABLE IF NOT EXISTS Voo (
    status VARCHAR(50),
    codViagem INT PRIMARY KEY,
    horario DATETIME,
    origemVoo VARCHAR(50),
    destinoVoo VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Aeronave (
    Registro INT PRIMARY KEY,
    CombustivelDisp INT,
    Modelo VARCHAR(50),
    NumHangar INT,
    CodCompanhia INT,
    FOREIGN KEY (Modelo) REFERENCES TipoAeronave(Modelo) ON DELETE CASCADE,
    FOREIGN KEY (NumHangar) REFERENCES Hangar(Número) ON DELETE NO ACTION,
    FOREIGN KEY (CodCompanhia) REFERENCES CompanhiaAerea(Código) ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS CompanhiaAerea (
    Nome VARCHAR(100),
    Codigo INT PRIMARY KEY,
    Telefone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Hangar (
    Numero INT PRIMARY KEY,
    CapacidadeAeronaves INT
);

CREATE TABLE IF NOT EXISTS Piloto (
    Licenca VARCHAR(50) PRIMARY KEY,
    Nome VARCHAR(100),
    Telefone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS TipoAeronave (
    PesoMax INT,
    MaxCombustivel INT,
    Modelo VARCHAR(50) PRIMARY KEY,
    CapacPassageiros INT
);

CREATE TABLE IF NOT EXISTS TipoServico (
    Codigo INT PRIMARY KEY,
    Descricao VARCHAR(100),
    Horas INT
);

CREATE TABLE IF NOT EXISTS Funcionario (
    Salario DECIMAL(10, 2),
    Nome VARCHAR(100),
    Identificador INT PRIMARY KEY,
    Endereco VARCHAR(150),
    DataNasc DATE
);

CREATE TABLE IF NOT EXISTS ComissarioBordo (
    Comissao DECIMAL(5, 2),
    Identificador INT PRIMARY KEY,
    FOREIGN KEY (Identificador) REFERENCES Funcionario(Identificador) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS TecManutencao (
    Especialidade VARCHAR(100),
    Identificador INT PRIMARY KEY,
    FOREIGN KEY (Identificador) REFERENCES Funcionario(Identificador) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Passageiro (
    Nome VARCHAR(100),
    DataNasc DATE,
    Telefone VARCHAR(20),
    Nacionalidade VARCHAR(50),
    CPF VARCHAR(15) PRIMARY KEY,
    NumPassaporte VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Reserva (
    CPF VARCHAR(15),
    CodViagem1 INT,
    CodViagem2 INT,
    DataVoo DATE,
    DataReserva DATE,
    NumAssento INT,
    DataVooFeito DATE,
    PRIMARY KEY (CPF, CodViagem1, DataVoo),
    FOREIGN KEY (CPF) REFERENCES Passageiro(CPF) ON DELETE CASCADE,
    FOREIGN KEY (CodViagem1) REFERENCES Voo(CodViagem) ON DELETE NO ACTION,
    FOREIGN KEY (CodViagem2, DataVooFeito) REFERENCES VooFeito(CodViagem1, Data) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Bagagem (
    NumRegistro INT,
    PesoKg DECIMAL(10, 2),
    CPF VARCHAR(15),
    CodViagem INT,
    DataVoo DATE,
    PRIMARY KEY (NumRegistro, CPF, CodViagem, DataVoo)
    FOREIGN KEY (CPF, CodViagem, DataVoo) REFERENCES Reserva(CPF, CodViagem1, DataVoo) ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS VooFeito (
    CodViagem INT,
    Portao VARCHAR(10),
    RegistroAeronave INT,
    Data DATE,
    PRIMARY KEY (codViagem, Data)
    FOREIGN KEY (CodViagem) REFERENCES Voo(CodViagem) ON DELETE NO ACTION,
    FOREIGN KEY (RegistroAeronave) REFERENCES Aeronave(Registro) ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS ServicoFeito (
    RegistroAeronave INT,
    CodServico INT,
    Data DATE,
    PRIMARY KEY (RegistroAeronave, CodServico, Data),
    FOREIGN KEY (RegistroAeronave) REFERENCES Aeronave(Registro) ON DELETE NO ACTION,
    FOREIGN KEY (CodServico) REFERENCES TipoServico(Codigo) ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS Executa (
    IdFuncionario INT,
    RegistroAeronave INT,
    CodServico INT,
    Data DATE,
    PRIMARY KEY (IdFuncionario, RegistroAeronave, CodServico, Data),
    FOREIGN KEY (IdFuncionario) REFERENCES TecManutencao(Identificador) ON DELETE NO ACTION,
    FOREIGN KEY (RegistroAeronave, CodServico, Data) REFERENCES ServicoFeito(RegistroAeronave, CodServico, Data) ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS Acompanha (
    IdFuncionario INT,
    CodViagem INT,
    DataViagem DATE,
    PRIMARY KEY (IdFuncionario, CodViagem, DataViagem),
    FOREIGN KEY (IdFuncionario) REFERENCES ComissarioBordo(Identificador) ON DELETE NO ACTION,
    FOREIGN KEY (CodViagem, DataViagem) REFERENCES VooFeito(CodViagem, Data) ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS PodeSerFeito (
    CodViagem INT,
    RegistroAeronave INT,
    PRIMARY KEY (CodViagem, RegistroAeronave),
    FOREIGN KEY (CodViagem) REFERENCES Voo(CodViagem) ON DELETE CASCADE,
    FOREIGN KEY (RegistroAeronave) REFERENCES Aeronave(Registro) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Pilotada (
    Modelo VARCHAR(50),
    LicencaPiloto VARCHAR(50),
    PRIMARY KEY (Modelo, LicencaPiloto),
    FOREIGN KEY (Modelo) REFERENCES TipoAeronave(Modelo) ON DELETE CASCADE,
    FOREIGN KEY (LicencaPiloto) REFERENCES Piloto(Licenca) ON DELETE CASCADE
);


