import psycopg2

def connect_to_db():
    try:
        # Параметри підключення до бази даних
        dbname = "postgres"
        user = "postgres"
        password = "mysecretpassword"
        host = "127.0.0.1"
        port=5432

        # Підключення до бази даних
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

        print("Підключення до бази даних успішно.")
        return conn

    except Exception as e:
        print(f"Помилка підключення до бази даних: {e}")
        return None
