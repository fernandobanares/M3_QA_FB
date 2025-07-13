import sqlite3

# Conexión a archivo SQLite externo a Django
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Ejecutar script SQL
with open('script.sql', 'r') as archivo:
    sql_script = archivo.read()
    cursor.executescript(sql_script)
    print("Base de datos y registros creados.")

# Leer usuarios
print("\nUsuarios actuales:")
cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)

# Insertar un nuevo usuario
cursor.execute("INSERT INTO usuarios (nombre, email, activo) VALUES (?, ?, ?)",
               ("Nuevo", "nuevo@mail.com", 1))
print("\nNuevo usuario insertado.")

# Actualizar usuario
cursor.execute("UPDATE usuarios SET activo = 0 WHERE nombre = 'Laura'")
print("Usuario 'Laura' actualizado.")

# Eliminar usuario
cursor.execute("DELETE FROM usuarios WHERE nombre = 'Carlos'")
print("Usuario 'Carlos' eliminado.")

# Guardar y cerrar
conn.commit()
conn.close()
print("\nCambios guardados en usuarios.db")
