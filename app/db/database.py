import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Load .env from the project root (the folder containing this file's parent app/).
PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

# A local SQLite database is used by default so the project can run without
# installing/configuring PostgreSQL. Set DATABASE_URL in .env to use PostgreSQL.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{(PROJECT_ROOT / 'crop_prediction.db').as_posix()}",
)

engine_options = {"pool_pre_ping": True}
if not DATABASE_URL.startswith("sqlite"):
    engine_options["pool_recycle"] = 300

engine = create_engine(DATABASE_URL, **engine_options)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Create the tables required by the API for SQLite or PostgreSQL."""
    with engine.begin() as connection:
        if engine.dialect.name == "sqlite":
            connection.execute(text("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(150) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    google_id VARCHAR(255) UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """))
            connection.execute(text("""
                CREATE TABLE IF NOT EXISTS irrigation_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    location VARCHAR(150) NOT NULL,
                    state VARCHAR(150),
                    country VARCHAR(100),
                    latitude REAL NOT NULL,
                    longitude REAL NOT NULL,
                    soil_type VARCHAR(100),
                    temperature REAL,
                    humidity REAL,
                    rain REAL,
                    soil_moisture REAL,
                    evapotranspiration REAL,
                    forecast_rain_24h REAL,
                    irrigation_status VARCHAR(50),
                    recommendation TEXT,
                    user_id INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
                )
            """))
            connection.execute(text("""
                CREATE TABLE IF NOT EXISTS prediction_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    location VARCHAR(150),
                    state VARCHAR(150),
                    country VARCHAR(100),
                    latitude REAL,
                    longitude REAL,
                    predicted_crop VARCHAR(50),
                    predicted_yield REAL,
                    yield_unit VARCHAR(100),
                    fertilizer_recommendation TEXT,
                    annual_rainfall REAL,
                    temperature REAL,
                    humidity REAL,
                    rain REAL,
                    soil_moisture REAL,
                    soil_temperature REAL,
                    season VARCHAR(50),
                    prediction_year INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
                )
            """))
        else:
            connection.execute(text("""
                CREATE TABLE IF NOT EXISTS users (
                    id BIGSERIAL PRIMARY KEY,
                    name VARCHAR(150) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    google_id VARCHAR(255) UNIQUE,
                    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
                )
            """))
            connection.execute(text("""
                CREATE TABLE IF NOT EXISTS irrigation_history (
                    id BIGSERIAL PRIMARY KEY,
                    location VARCHAR(150) NOT NULL,
                    state VARCHAR(150),
                    country VARCHAR(100),
                    latitude DOUBLE PRECISION NOT NULL,
                    longitude DOUBLE PRECISION NOT NULL,
                    soil_type VARCHAR(100),
                    temperature DOUBLE PRECISION,
                    humidity DOUBLE PRECISION,
                    rain DOUBLE PRECISION,
                    soil_moisture DOUBLE PRECISION,
                    evapotranspiration DOUBLE PRECISION,
                    forecast_rain_24h DOUBLE PRECISION,
                    irrigation_status VARCHAR(50),
                    recommendation TEXT,
                    user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
                    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
                )
            """))
            connection.execute(text("""
                CREATE TABLE IF NOT EXISTS prediction_history (
                    id BIGSERIAL PRIMARY KEY,
                    user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                    location VARCHAR(150),
                    state VARCHAR(150),
                    country VARCHAR(100),
                    latitude DOUBLE PRECISION,
                    longitude DOUBLE PRECISION,
                    predicted_crop VARCHAR(50),
                    predicted_yield DOUBLE PRECISION,
                    yield_unit VARCHAR(100),
                    fertilizer_recommendation TEXT,
                    annual_rainfall DOUBLE PRECISION,
                    temperature DOUBLE PRECISION,
                    humidity DOUBLE PRECISION,
                    rain DOUBLE PRECISION,
                    soil_moisture DOUBLE PRECISION,
                    soil_temperature DOUBLE PRECISION,
                    season VARCHAR(50),
                    prediction_year INTEGER,
                    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
                )
            """))

        connection.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_irrigation_history_created_at
            ON irrigation_history(created_at DESC)
        """))
        connection.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_irrigation_history_user_id
            ON irrigation_history(user_id)
        """))
        connection.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_prediction_history_user_id
            ON prediction_history(user_id)
        """))
        connection.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_prediction_history_created_at
            ON prediction_history(created_at DESC)
        """))
