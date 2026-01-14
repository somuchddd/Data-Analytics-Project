import time
import random
import psycopg2

con = psycopg2.connect(
    host='postgres',
    database='projectdb',
    user='projectuser',
    password='12345project'
)

users = [
    {'id': 1, 'name': 'Варвара', 'weight': 52, 'gender': 'Женщина'},
    {'id': 2, 'name': 'Карина', 'weight': 58, 'gender': 'Женщина'},
    {'id': 3, 'name': 'Анна', 'weight': 45, 'gender': 'Женщина'},
    {'id': 4, 'name': 'Мария', 'weight': 62, 'gender': 'Женщина'},
    {'id': 5, 'name': 'Никита', 'weight': 75, 'gender': 'Мужчина'},
    {'id': 6, 'name': 'Артём', 'weight': 82, 'gender': 'Мужчина'},
    {'id': 7, 'name': 'Михаил', 'weight': 88, 'gender': 'Мужчина'},
    {'id': 8, 'name': 'Максим', 'weight': 78, 'gender': 'Мужчина'},
    {'id': 9, 'name': 'Денис', 'weight': 85, 'gender': 'Мужчина'},
    {'id': 10, 'name': 'Иван', 'weight': 73, 'gender': 'Мужчина'}
]

activities = {
    'Ходьба': {'steps_per_minute': (50, 100), 'hr': (90, 115), 'met': 2.5},
    'Быстрая ходьба': {'steps_per_minute': (100, 130), 'hr': (100, 130), 'met': 5},
    'Медленный бег': {'steps_per_minute': (130, 150), 'hr': (130, 150), 'met': 6},
    'Бег': {'steps_per_minute': (150, 170), 'hr': (140, 160), 'met': 8},
    'Быстрый бег': {'steps_per_minute': (170, 200), 'hr': (150, 180), 'met': 10},
    'Отдых': {'steps_per_minute': (0, 20), 'hr': (50, 80), 'met': 1},
}


while True:
    user = random.choice(users)

    activity_name = random.choice(list(activities.keys()))
    activity = activities[activity_name]

    if activity_name == 'Отдых':
        duration = random.randint(5, 120)
    elif activity_name in ['Ходьба', 'Быстрая ходьба']:
        duration = random.randint(10, 60)
    else:
        duration = random.randint(5, 30)

    spm = random.randint(*activity['steps_per_minute'])
    steps = duration * spm
    
    hr = random.randint(*activity['hr'])

    calories = round(activity['met'] * user['weight'] * duration / 60, 1)

    cursor = con.cursor()
    cursor.execute('''
        INSERT INTO fitness_data
        (person_id, person_name, weight, gender, activity_type, steps, heart_rate, calories_burned, duration_minutes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                   
    ''', (user['id'], user['name'], user['weight'], user['gender'],
        activity_name, steps, hr, calories, duration)
    )

    con.commit()
    cursor.close()

    time.sleep(1)