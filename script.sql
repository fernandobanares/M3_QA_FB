
-- Crear tabla equivalente al modelo Registro
CREATE TABLE registro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL
);

-- Insertar 5 registros de ejemplo
INSERT INTO registro (nombre, email) VALUES ('Carlos', 'carlos@gmail.com');
INSERT INTO registro (nombre, email) VALUES ('Laura', 'laura@outlook.com');
INSERT INTO registro (nombre, email) VALUES ('Tomas', 'tomas@gmail.com');
INSERT INTO registro (nombre, email) VALUES ('Lucía', 'lucia@gmail.com');
INSERT INTO registro (nombre, email) VALUES ('Carmen', 'carmen@mail.com');
