#!/usr/bin/env python3
"""
FlowMindHub - Admin Script (PostgreSQL Version)
View and manage client inquiries
"""

import psycopg2
import psycopg2.extras
from datetime import datetime
from config import Config

config = Config()

def get_db_connection():
    """Get database connection"""
    try:
        conn = psycopg2.connect(config.DATABASE_URL)
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def view_inquiries():
    """View all client inquiries"""
    conn = get_db_connection()
    if not conn:
        print("❌ Failed to connect to database")
        return
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
    cursor.execute('''
        SELECT id, name, email, company, phone, service_type, message, status, created_at
        FROM inquiries
        ORDER BY created_at DESC
    ''')
    
    inquiries = cursor.fetchall()
    
    if not inquiries:
        print("📭 No inquiries found.")
        cursor.close()
        conn.close()
        return
    
    print("📋 FlowMindHub Client Inquiries")
    print("=" * 80)
    
    for inquiry in inquiries:
        print(f"\n🔍 Inquiry ID: {inquiry['id']}")
        print(f"👤 Name: {inquiry['name']}")
        print(f"📧 Email: {inquiry['email']}")
        print(f"🏢 Company: {inquiry['company'] or 'Not provided'}")
        print(f"📞 Phone: {inquiry['phone'] or 'Not provided'}")
        print(f"🎯 Service: {inquiry['service_type']}")
        print(f"📝 Message: {inquiry['message']}")
        print(f"📊 Status: {inquiry['status']}")
        print(f"📅 Date: {inquiry['created_at']}")
        print("-" * 80)
    
    cursor.close()
    conn.close()

def update_inquiry_status(inquiry_id, new_status):
    """Update inquiry status"""
    conn = get_db_connection()
    if not conn:
        print("❌ Failed to connect to database")
        return
    
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE inquiries
        SET status = %s
        WHERE id = %s
    ''', (new_status, inquiry_id))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    print(f"✅ Inquiry {inquiry_id} status updated to '{new_status}'")

def view_portfolio_stats():
    """View portfolio statistics"""
    conn = get_db_connection()
    if not conn:
        print("❌ Failed to connect to database")
        return
    
    cursor = conn.cursor()
    
    # Count total portfolio items
    cursor.execute('SELECT COUNT(*) FROM portfolio')
    total_items = cursor.fetchone()[0]
    
    # Count by category
    cursor.execute('''
        SELECT category, COUNT(*) 
        FROM portfolio 
        GROUP BY category
    ''')
    categories = cursor.fetchall()
    
    print("📊 Portfolio Statistics")
    print("=" * 40)
    print(f"Total Projects: {total_items}")
    print("\nBy Category:")
    for category, count in categories:
        print(f"  • {category}: {count}")
    
    cursor.close()
    conn.close()

def view_services():
    """View all services"""
    conn = get_db_connection()
    if not conn:
        print("❌ Failed to connect to database")
        return
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
    cursor.execute('SELECT * FROM services ORDER BY id')
    services = cursor.fetchall()
    
    if not services:
        print("📭 No services found.")
        cursor.close()
        conn.close()
        return
    
    print("🛠️ FlowMindHub Services")
    print("=" * 60)
    
    for service in services:
        print(f"\n🔧 Service ID: {service['id']}")
        print(f"📝 Name: {service['name']}")
        print(f"📄 Description: {service['description']}")
        print(f"🎨 Icon: {service['icon']}")
        print(f"💰 Price Range: {service['price_range']}")
        print(f"✨ Features: {service['features']}")
        print("-" * 60)
    
    cursor.close()
    conn.close()

def main():
    """Main admin function"""
    while True:
        print("\n🔧 FlowMindHub Admin Panel (PostgreSQL)")
        print("=" * 40)
        print("1. View all inquiries")
        print("2. Update inquiry status")
        print("3. View portfolio stats")
        print("4. View all services")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == '1':
            view_inquiries()
        elif choice == '2':
            inquiry_id = input("Enter inquiry ID: ").strip()
            status = input("Enter new status (new, contacted, in_progress, completed): ").strip()
            update_inquiry_status(inquiry_id, status)
        elif choice == '3':
            view_portfolio_stats()
        elif choice == '4':
            view_services()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == '__main__':
    main()
