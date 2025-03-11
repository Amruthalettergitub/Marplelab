from flask import Flask
import os
import datetime
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getenv('USER', 'default-user')
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = subprocess.getoutput("top -b -n 1 | head -20")

    return f"""
    <h2>Name: {name}</h2>
    <h3>Username: {username}</h3>
    <h4>Server Time (IST): {server_time}</h4>
    <pre>{top_output}</pre>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)