from django.shortcuts import render
from django.http import HttpResponse
import os
import time

def system_info(request):
    username = os.getenv("USER", "unknown")
    server_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    top_output = os.popen("top -bn1 | head -20").read()

    return HttpResponse(f"""
    <h1>Name: Your Full Name</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """)

# Create your views here.
