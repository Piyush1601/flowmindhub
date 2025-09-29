#!/usr/bin/env python3
"""
FlowMindHub - Startup Script
Run this script to start the FlowMindHub website
"""

import os
import sys
from app import app, init_db, insert_sample_data

def main():
    """Main function to start the Flask application"""
    print("🚀 Starting FlowMindHub Website...")
    print("=" * 50)
    
    # Initialize database
    print("📊 Initializing database...")
    init_db()
    
    # Insert sample data
    print("📝 Inserting sample data...")
    insert_sample_data()
    
    print("✅ Database setup complete!")
    print("🌐 Starting web server...")
    print("=" * 50)
    print("📍 Website will be available at: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
