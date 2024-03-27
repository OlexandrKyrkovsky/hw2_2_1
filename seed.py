from faker import Faker
import psycopg2
import random

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="mysecretpassword",
    host="127.0.0.1",
    port=5432
)

# Створення курсора для виконання SQL-запитів
cur = conn.cursor()

# Ініціалізація Faker
fake = Faker()

# Функція для заповнення таблиці користувачів
def seed_users(num_users):
    for _ in range(num_users):
        fullname = fake.name()
        email = fake.email()
        cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
    conn.commit()
    print(f"{num_users} users seeded successfully.")

# Функція для заповнення таблиці завдань
def seed_tasks(num_tasks, num_users):
    for _ in range(num_tasks):
        title = fake.text(max_nb_chars=50)
        description = fake.text()
        status_id = random.randint(1, 3)  # Випадково обираємо ідентифікатор статусу (1, 2 або 3)
        user_id = random.randint(1, num_users)  # Випадково обираємо ідентифікатор користувача
        cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                    (title, description, status_id, user_id))
    conn.commit()
    print(f"{num_tasks} tasks seeded successfully.")

try:
    # Виклик функцій для заповнення таблиць
    seed_users(10)  # Заповнимо 10 користувачів
    seed_tasks(20, 10)  # Заповнимо 20 завдань для 10 користувачів
except Exception as e:
    print(f"Error: {e}")
finally:
    # Закриття курсора та з'єднання з базою даних
    cur.close()
    conn.close()
