CREATE TABLE IF NOT EXISTS fitness_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    person_id INTEGER NOT NULL,
    person_name VARCHAR(30),
    weight INTEGER,
    gender VARCHAR(10),
    activity_type VARCHAR(50),
    steps INTEGER NOT NULL,
    heart_rate INTEGER NOT NULL,
    calories_burned DECIMAL(6,1) NOT NULL,
    duration_minutes INTEGER
)