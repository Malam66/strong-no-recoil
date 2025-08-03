#!/usr/bin/env python3
"""
Simple script to view the website locally
"""

import webbrowser
import os
import http.server
import socketserver
import threading
import time

def start_server():
    """Start a simple HTTP server"""
    PORT = 8000
    
    # Change to the directory containing index.html
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🌐 Server started at http://localhost:{PORT}")
        print("📱 Opening website in browser...")
        webbrowser.open(f'http://localhost:{PORT}')
        print("✅ Website opened!")
        print("\n💡 To stop the server, press Ctrl+C")
        httpd.serve_forever()

if __name__ == "__main__":
    print("🎯 Strong No Recoil - Website Viewer")
    print("=" * 40)
    
    # Check if index.html exists
    if not os.path.exists('index.html'):
        print("❌ index.html not found!")
        print("Please make sure index.html is in the same directory")
        input("Press Enter to exit...")
        exit(1)
    
    print("✅ index.html found")
    print("🚀 Starting local server...")
    
    try:
        start_server()
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        input("Press Enter to exit...") 