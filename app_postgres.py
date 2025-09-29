from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import psycopg2
import psycopg2.extras
import os
from datetime import datetime
from config import Config

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Database configuration
config = Config()

# Database connection helper
def get_db_connection():
    try:
        conn = psycopg2.connect(config.DATABASE_URL)
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

# Database setup
def init_db():
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to database")
        return
    
    cursor = conn.cursor()
    
    # Create portfolio table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS portfolio (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            image_url VARCHAR(500),
            category VARCHAR(100) NOT NULL,
            client_name VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create contact inquiries table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inquiries (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            company VARCHAR(255),
            phone VARCHAR(50),
            service_type VARCHAR(100) NOT NULL,
            message TEXT NOT NULL,
            status VARCHAR(50) DEFAULT 'new',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create services table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            icon VARCHAR(100),
            price_range VARCHAR(100),
            features TEXT
        )
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()

# Insert sample data
def insert_sample_data():
    conn = get_db_connection()
    if not conn:
        return
    
    cursor = conn.cursor()
    
    # Check if data already exists
    cursor.execute('SELECT COUNT(*) FROM services')
    if cursor.fetchone()[0] == 0:
        # Sample services
        services = [
            ('Website Development', 'Custom websites for NGOs, businesses, and organizations with modern design and functionality', 'fas fa-laptop-code', '$500 - $5000', 'Responsive Design, CMS Integration, SEO Optimization, Mobile-First Approach, Fast Loading, Security Features'),
            ('Automation Solutions', 'N8N workflows and automation tools to streamline business processes and reduce manual work', 'fas fa-robot', '$300 - $3000', 'N8N Workflows, API Integrations, Data Processing, Email Automation, Task Scheduling, Error Handling'),
            ('AI Video Creation', 'AI-powered video ads and UGC content creation using static catalog images', 'fas fa-video', '$200 - $1500', 'AI Video Generation, Static Image Processing, UGC Content, Social Media Optimization, Multiple Formats, Brand Consistency'),
            ('Bill Management Systems', 'Automated billing and inventory tracking systems like EasyBillGen', 'fas fa-file-invoice-dollar', '$400 - $4000', 'Automated Billing, Inventory Tracking, Payment Processing, Report Generation, Multi-User Support, Data Analytics')
        ]
        
        cursor.executemany('INSERT INTO services (name, description, icon, price_range, features) VALUES (%s, %s, %s, %s, %s)', services)
    
    # Check if portfolio data already exists
    cursor.execute('SELECT COUNT(*) FROM portfolio')
    if cursor.fetchone()[0] == 0:
        # Sample portfolio items
        portfolio_items = [
            ('NGO Website', 'Complete website solution for Green Earth Foundation with donation system, event management, volunteer registration, and impact tracking. Features include online payment integration, multi-language support, and mobile-responsive design.', '/static/images/ngo-website.jpg', 'Website Development', 'Green Earth Foundation'),
            ('EasyBillGen', 'Revolutionary automated billing and inventory tracking system for TechStart Inc. Automatically generates invoices, tracks inventory levels, sends payment reminders, and provides detailed analytics dashboard for business insights.', '/static/images/easybillgen.jpg', 'Automation Solutions', 'TechStart Inc'),
            ('Coding Platform', 'Interactive online learning platform for CodeAcademy Pro with real-time coding environment, progress tracking, certification system, and AI-powered code review. Supports multiple programming languages and collaborative coding features.', '/static/images/coding-platform.jpg', 'Website Development', 'CodeAcademy Pro'),
            ('AI Product Ads', 'AI-powered video advertisement system for Fashion Store that transforms static product images into engaging video content. Creates personalized ads for different platforms including social media, e-commerce, and display advertising.', '/static/images/ai-ads.jpg', 'AI Video Creation', 'Fashion Store'),
            ('Smart Inventory System', 'Advanced inventory management system with IoT integration, predictive analytics, and automated reordering. Reduces stockouts by 40% and improves efficiency by 60% for retail businesses.', '/static/images/inventory-system.jpg', 'Automation Solutions', 'Retail Plus'),
            ('E-Learning Portal', 'Comprehensive educational platform with video streaming, quiz system, progress tracking, and certification management. Supports thousands of concurrent users with seamless performance.', '/static/images/elearning.jpg', 'Website Development', 'EduTech Solutions')
        ]
        
        cursor.executemany('INSERT INTO portfolio (title, description, image_url, category, client_name) VALUES (%s, %s, %s, %s, %s)', portfolio_items)
    
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def home():
    conn = get_db_connection()
    if not conn:
        flash('Database connection error', 'error')
        return render_template('index.html', services=[], portfolio=[])
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
    # Get featured services
    cursor.execute('SELECT * FROM services LIMIT 4')
    services = cursor.fetchall()
    
    # Get all portfolio items for slideshow
    cursor.execute('SELECT * FROM portfolio ORDER BY created_at DESC')
    portfolio = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('index.html', services=services, portfolio=portfolio)

@app.route('/services')
def services():
    conn = get_db_connection()
    if not conn:
        flash('Database connection error', 'error')
        return render_template('services.html', services=[])
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute('SELECT * FROM services')
    services = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('services.html', services=services)

@app.route('/portfolio')
def portfolio():
    conn = get_db_connection()
    if not conn:
        flash('Database connection error', 'error')
        return render_template('portfolio.html', portfolio=[])
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute('SELECT * FROM portfolio ORDER BY created_at DESC')
    portfolio = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('portfolio.html', portfolio=portfolio)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        company = request.form.get('company', '')
        phone = request.form.get('phone', '')
        service_type = request.form['service']
        message = request.form['message']
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO inquiries (name, email, company, phone, service_type, message)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (name, email, company, phone, service_type, message))
            conn.commit()
            cursor.close()
            conn.close()
            
            flash('Thank you for your inquiry! We will get back to you soon.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Error submitting inquiry. Please try again.', 'error')
    
    return render_template('contact.html')

@app.route('/simple')
def simple():
    return render_template('index_simple.html')

if __name__ == '__main__':
    # Initialize database and insert sample data
    init_db()
    insert_sample_data()
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5001)
