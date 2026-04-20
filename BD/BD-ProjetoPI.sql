CREATE TABLE eleitores(
id_eleitores INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
cpf VARCHAR(12) UNIQUE NOT NULL,
titulo_de_eleitor VARCHAR(12) UNIQUE NOT NULL,
mesario BOOLEAN DEFAULT FALSE NOT NULL,
chave_de_acesso VARCHAR(7) UNIQUE NOT NULL,
confirmacao_de_voto BOOLEAN DEFAULT FALSE NOT NULL
);

CREATE TABLE candidatos(
id_candidatos INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
partido VARCHAR(100) NOT NULL,
numero_candidato INT UNIQUE NOT NULL
);

CREATE TABLE votacao(
id_votacao INT PRIMARY KEY AUTO_INCREMENT,
numero_candidato INT,
protocolo_votacao VARCHAR(50) UNIQUE,
dia DATE,
voto_nulo BOOLEAN DEFAULT FALSE,
FOREIGN KEY (numero_candidato) REFERENCES candidatos(numero_candidato)
);

ALTER TABLE votacao
ADD FOREIGN KEY (numero_candidato) REFERENCES candidatos (numero_candidato);
INSERT INTO  eleitores (nome, cpf, titulo_de_eleitor, mesario, chave_de_acesso, confirmacao_de_voto) values ('Ana Beatriz', '12345678901', '123456789012', false, 'ANB1234', false);
INSERT INTO candidatos (nome, partido, numero_candidato) values ('Marcos Moreira', 'ABCD', 50 );
INSERT INTO votacao (numero_candidato, protocolo_votacao, dia, voto_nulo)
VALUES (
    (SELECT numero_candidato FROM candidatos WHERE numero_candidato = 50),
    '54321',
    '2026-06-06',
    false
    );
