DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    activo BOOLEAN DEFAULT 1
);

INSERT INTO usuarios (nombre, email, activo) VALUES
('Fernando', 'fer@mail.com', 1),
('Laura', 'laura@mail.com', 1),
('Carlos', 'carlos@mail.com', 0),
('Marta', 'marta@mail.com', 1),
('Luis', 'luis@mail.com', 0);
