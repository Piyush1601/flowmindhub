#!/usr/bin/env python3
"""
FlowMindHub - Admin Script (PostgreSQL Version)
View and manage client inquiries
"""

import psycopg
from datetime import datetime
from config import Config

config = Config()

def get_db_connection():
    """Get database connection"""
    try:
        conn = psycopg.connect(config.DATABASE_URL)
        return conn
    except psycopg.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def view_inquiries():
    """View all client inquiries"""
    conn = get_db_connection()
    if not conn:
        print("❌ Failed to connect to database")
        return
    
    with conn.cursor() as cursor:
        cursor.execute('''
            SELECT id, name, email, company, phone, service_type, message, status, created_at
            FROM inquiries
            ORDER BY created_at DESC
        ''')
        
        inquiries = cursor.fetchall()
        
        if not inquiries:
            print("📭 No inquiries found.")
            return
        
        print("📋 FlowMindHub Client Inquiries")
        print("=" * 80)
        
        for inquiry in inquiries:
            print(f"\n🔍 Inquiry ID: {inquiry[0]}")
            print(f"👤 Name: {inquiry[1]}")
            print(f"📧 Email: {inquiry[2]}")
            print(f"🏢 Company: {inquiry[3] or 'Not provided'}")
            print(f"📞 Phone: {inquiry[4] or 'Not provided'}")
            print(f"🎯 Service: {inquiry[5]}")
            print(f"📝 Message: {inquiry[6]}")
            print(f"📊 Status: {inquiry[7]}")
            print(f"📅 Date: {inquiry[8]}")
            print("-" * 80)
    
    conn.close()

def update_inquiry_status(inquiry_id, new_status):
    """Update inquiry status"""
    conn = get_db_connection()
    if not conn:
        print("❌ Failed to connect to database")
        return
    
    with conn.cursor() as cursor:
        cursor.execute('''
            UPDATE inquiries
            SET status = %s
            WHERE id = %s
        ''', (new_status, inquiry_id))
        
        conn.commit()
    conn.close()
    
    print(f"✅ Inquiry {inquiry_id} status updated to '{new_status}'")

def view_portfolio_stats():
    """View portfolio statistics"""
    conn = get_db_connection()
    if not conn:
        print("❌ Failed to connect to database")
        return
    
    with conn.cursor() as cursor:
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
    
    conn.close()

def view_services():
    """View all services"""
    conn = get_db_connection()
    if not conn:
        print("❌ Failed to connect to database")
        return
    
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM services ORDER BY id')
        services = cursor.fetchall()
        
        if not services:
            print("📭 No services found.")
            return
        
        print("🛠️ FlowMindHub Services")
        print("=" * 60)
        
        for service in services:
            print(f"\n🔧 Service ID: {service[0]}")
            print(f"📝 Name: {service[1]}")
            print(f"📄 Description: {service[2]}")
            print(f"🎨 Icon: {service[3]}")
            print(f"💰 Price Range: {service[4]}")
            print(f"✨ Features: {service[5]}")
            print("-" * 60)
    
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
