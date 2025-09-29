# PostgreSQL Setup for FlowMindHub

This guide will help you set up PostgreSQL for your FlowMindHub website.

## Prerequisites

1. **PostgreSQL Installation**: Make sure PostgreSQL is installed on your system
2. **Python Virtual Environment**: Activate your virtual environment
3. **Dependencies**: Install the required Python packages

## Installation Steps

### 1. Install PostgreSQL Dependencies

```bash
# Activate your virtual environment
source venv/bin/activate

# Install PostgreSQL dependencies
pip install -r requirements.txt
```

### 2. Install PostgreSQL (if not already installed)

#### On macOS (using Homebrew):
```bash
brew install postgresql
brew services start postgresql
```

#### On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

#### On Windows:
Download and install from: https://www.postgresql.org/download/windows/

### 3. Create Database and User

Connect to PostgreSQL as the superuser:

```bash
# On macOS/Linux
sudo -u postgres psql

# On Windows (if installed with default settings)
psql -U postgres
```

Run the following SQL commands:

```sql
-- Create database
CREATE DATABASE flowmindhub_db;

-- Create user
CREATE USER flowmindhub_user WITH PASSWORD 'flowmindhub_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE flowmindhub_db TO flowmindhub_user;

-- Grant schema privileges (PostgreSQL 15+)
\c flowmindhub_db
GRANT ALL ON SCHEMA public TO flowmindhub_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO flowmindhub_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO flowmindhub_user;

-- Exit PostgreSQL
\q
```

### 4. Configure Database Connection

The application uses the following default configuration in `config.py`:

```python
DATABASE_URL = 'postgresql://flowmindhub_user:flowmindhub_password@localhost:5432/flowmindhub_db'
```

You can customize this by setting environment variables:

```bash
export DATABASE_URL="postgresql://your_user:your_password@localhost:5432/your_database"
```

Or modify the `config.py` file directly.

### 5. Test the Setup

Run the application to test the PostgreSQL connection:

```bash
# Activate virtual environment
source venv/bin/activate

# Run the application
python app.py
```

The application will:
1. Connect to PostgreSQL
2. Create the necessary tables
3. Insert sample data
4. Start the web server on port 5001

### 6. Verify Database Setup

Check that the tables were created successfully:

```bash
# Connect to your database
psql -U flowmindhub_user -d flowmindhub_db

# List tables
\dt

# View sample data
SELECT * FROM services;
SELECT * FROM portfolio;
```

## Database Schema

The application creates three main tables:

### 1. `services` Table
```sql
CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    icon VARCHAR(100),
    price_range VARCHAR(100),
    features TEXT
);
```

### 2. `portfolio` Table
```sql
CREATE TABLE portfolio (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    image_url VARCHAR(500),
    category VARCHAR(100) NOT NULL,
    client_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3. `inquiries` Table
```sql
CREATE TABLE inquiries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    company VARCHAR(255),
    phone VARCHAR(50),
    service_type VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'new',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Admin Panel

Use the admin script to manage inquiries:

```bash
python admin.py
```

This will give you options to:
- View all client inquiries
- Update inquiry status
- View portfolio statistics
- View all services

## Troubleshooting

### Common Issues:

1. **Connection Refused**:
   - Make sure PostgreSQL is running: `brew services start postgresql` (macOS)
   - Check if the port 5432 is open

2. **Authentication Failed**:
   - Verify username and password in `config.py`
   - Check if the user has proper privileges

3. **Database Does Not Exist**:
   - Create the database: `CREATE DATABASE flowmindhub_db;`
   - Grant privileges to the user

4. **Permission Denied**:
   - Grant schema privileges: `GRANT ALL ON SCHEMA public TO flowmindhub_user;`

### Environment Variables

You can override the default configuration using environment variables:

```bash
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=flowmindhub_db
export DB_USER=flowmindhub_user
export DB_PASSWORD=flowmindhub_password
```

## Backup and Restore

### Backup:
```bash
pg_dump -U flowmindhub_user flowmindhub_db > backup.sql
```

### Restore:
```bash
psql -U flowmindhub_user flowmindhub_db < backup.sql
```

## Migration from SQLite

If you're migrating from SQLite, your data files are backed up as:
- `app_sqlite_backup.py` (original app.py)
- `admin_sqlite_backup.py` (original admin.py)
- `flowmindhub.db` (original SQLite database)

You can import data from SQLite to PostgreSQL if needed using tools like `pgloader` or custom scripts.

## Security Notes

1. **Change Default Passwords**: Update the default password in production
2. **Use Environment Variables**: Store sensitive data in environment variables
3. **Network Security**: Configure PostgreSQL to accept connections only from trusted hosts
4. **Regular Backups**: Set up automated backup procedures

## Next Steps

Once PostgreSQL is set up:
1. Test the website at `http://localhost:5001`
2. Submit a test inquiry through the contact form
3. Use the admin panel to view and manage inquiries
4. Customize the services and portfolio data as needed
