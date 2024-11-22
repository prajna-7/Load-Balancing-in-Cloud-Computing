from flask import Flask, render_template
import requests

app = Flask(__name__)

# Servers' configurations (as per your original code)
servers = [
            {"host": "74.234.82.83:8080", "identifier": "Alpha", "load_factor": 7},
                {"host": "20.238.114.112:8080", "identifier": "Beta", "load_factor": 8}
                ]

# List for managing server rotation (as per your original code)
rotation_list = []
for index, server in enumerate(servers):
        rotation_list += [index] * server["load_factor"]

        rotation_counter = 0

@app.route('/')
def balance_load():
    global rotation_counter
    chosen_server = rotation_list[rotation_counter]
    rotation_counter = (rotation_counter + 1) % len(rotation_list)
    content = get_content(servers[chosen_server]["host"])
    return render_template('index.html', chosen_server=servers[chosen_server]["identifier"], content_from_server=content)

def get_content(host):
    try:
        resp = requests.get(f"http://{host}")
        resp.raise_for_status()
        return resp.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {host} unreachable. Details: {e}")
        return f"Error: {host} unreachable"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

