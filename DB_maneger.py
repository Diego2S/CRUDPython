import sqlite3
from pathlib import Path
from ler_csv import insert_DB

# Configurações do banco
ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

# Criação da tabela (garantir existência ao iniciar o sistema)
def create_table():
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            f'''
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                weight REAL
            )
            '''
        )
        connection.commit()

create_table()  # Executa ao importar o módulo


# Função de chamada segura
def safe_db_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except sqlite3.OperationalError as e:
        print(f"[OperationalError] Erro de operação no banco de dados: {e}")
    except sqlite3.IntegrityError as e:
        print(f"[IntegrityError] Violação de integridade: {e}")
    except sqlite3.ProgrammingError as e:
        print(f"[ProgrammingError] Erro de programação: {e}")
    except sqlite3.InterfaceError as e:
        print(f"[InterfaceError] Erro na interface de conexão: {e}")
    except sqlite3.DatabaseError as e:
        print(f"[DatabaseError] Erro geral no banco: {e}")
    except Exception as e:
        print(f"[Exception] Erro inesperado: {e}")
    return None


# Adicionar registro
def add_DB(name, weight):
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)'
        cursor.execute(sql, [name, weight])
        connection.commit()
        print("Registro inserido com sucesso.")


# Deletar todos os registros
def del_DB(id):
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        sql = f'DELETE FROM {TABLE_NAME} WHERE id = (?)'
        cursor.execute(sql, (id,))
        connection.commit()
        if cursor.rowcount == 0:
            print(f"Nenhum registro com ID {id} foi encontrado.")
        else:
            print(f"Registro com ID {id} deletado com sucesso.")



# Atualizar um ou mais campos

def update_DB(id, name=None, weight=None):
    if name is None and weight is None:
        print("Nada para atualizar.")
        return

    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        if name is not None:
            sql = f'UPDATE {TABLE_NAME} SET name = ? WHERE id = ?'
            cursor.execute(sql, (name, id))
            connection.commit()
            print("Nome atualizado.")

        if weight is not None:
            sql = f'UPDATE {TABLE_NAME} SET weight = ? WHERE id = ?'
            cursor.execute(sql, (weight, id))
            connection.commit()
            print("Peso atualizado.")

        



# Filtrar por nome (LIKE)
def filter_name_DB(name):
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        sql = f'SELECT * FROM {TABLE_NAME} WHERE name LIKE ?'
        cursor.execute(sql, (f'%{name}%',))
        results = cursor.fetchall()
        return results


# Buscar por ID (parcial, convertendo para texto)
def search_id_DB(id):
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        sql = f'SELECT * FROM {TABLE_NAME} WHERE CAST(id AS TEXT) LIKE ?'
        cursor.execute(sql, (f'%{id}%',))
        results = cursor.fetchall()
        return results
