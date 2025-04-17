from dotenv import load_dotenv
import os
import pyodbc

# Carrega variáveis do .env
load_dotenv()

# Informações de conexão
server = "server,12345"  # <- Servidor com porta
database = "banco_de_dados"
ApplicationIntent = "ReadOnly"
Encrypt = "Yes"
App = "Office"
username = os.getenv("DB_USER")
password = os.getenv("DB_PASS")

# Exibe informações da conexão
print(f"Tentando conectar a {server} / Banco: {database}")
print(f"Usuário: {username}")
print(f"Senha: {'***' if password else '[VAZIA]'}")

conn = None  # Inicializa a variável conn

try:
    # Conexão com o SQL Server
    conn = pyodbc.connect(
        fr"DRIVER={{ODBC Driver 17 for SQL Server}};"
        fr"SERVER={server};"
        fr"applicationintent={ApplicationIntent};"
        fr"Encrypt={Encrypt};"
        fr"DATABASE={database};"
        fr"App={App};"
        fr"UID={username};"
        fr"PWD={password};"
        fr"TrustServerCertificate=yes;"
        fr"Connection Timeout=10;"
    )
    print("✅ Conexão bem-sucedida!")

except Exception as e:
    print("❌ Erro na conexão:", e)

finally:
    if conn:
        conn.close()
