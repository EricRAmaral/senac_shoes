CREATE DATABASE pessoas;
USE pessoas;

CREATE TABLE clientes ( 
			id INTEGER PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(100) NOT NULL,
            email TEXT UNIQUE NOT NULL,
            idade INTEGER,
            data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO clientes(nome, email, idade)
		VALUES('Maria Silva', 'maria@email.com', 28);

INSERT INTO clientes(nome, email, idade)
		VALUES('Bianca Moura', 'bianca@email.com', 23);

SELECT * FROM clientes;
SELECT nome, email FROM clientes WHERE idade > 25;

UPDATE clientes SET idade = 29 WHERE nome = "Maria Silva";

DELETE FROM clientes WHERE nome = "Maria Silva";