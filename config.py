import os

class Config:
    # PostgreSQL Database Configuration
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'postgresql://flowmindhub_user:flowmindhub_password@localhost:5432/flowmindhub_db'
    
    # Alternative individual settings
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_PORT = os.environ.get('DB_PORT') or '5432'
    DB_NAME = os.environ.get('DB_NAME') or 'flowmindhub_db'
    DB_USER = os.environ.get('DB_USER') or 'flowmindhub_user'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'flowmindhub_password'
    
    # Construct DATABASE_URL if not provided
    if not DATABASE_URL or DATABASE_URL == 'postgresql://flowmindhub_user:flowmindhub_password@localhost:5432/flowmindhub_db':
        DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
