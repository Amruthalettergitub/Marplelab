from flask import Flask
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get your name
    full_name = "Amrutha G M"

    # Get system username
    system_user = os.getenv("USER") or os.getenv("USERNAME") or "codespace"

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z%z")

    # Run 'top' command and get output
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        top_output = f"Error fetching top output: {e}"

    # HTML Output
    return f"""
    <h2>Name: {full_name}</h2>
    <h3>User: {system_user}</h3>
    <h3>Server Time (IST): {server_time}</h3>
    <h3>TOP Output:</h3>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

