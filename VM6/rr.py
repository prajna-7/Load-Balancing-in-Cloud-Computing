from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Define the IP addresses and ports of servers to be load balanced
server_configs = [
    {"ip": "74.234.82.83:8080", "name": "Server 4"},
    {"ip": "20.238.114.112:8080", "name": "Server 5"}
]

current_server_index = 0

@app.route('/')
def load_balance():
    global current_server_index

    # Get the current server configuration
    current_server = server_configs[current_server_index]

    # Increment the index for the next request (round-robin)
    current_server_index = (current_server_index + 1) % len(server_configs)

    # Get the content from the selected server
    selected_server_content = get_server_content(current_server["ip"])

    # Prepare response
    response = {
        'selected_server': current_server["name"],
        'selected_server_content': selected_server_content
    }

    return selected_server_content  # Return the entire HTML content

def get_server_content(server_ip):
    try:
        response = requests.get(f"http://{server_ip}")
        return response.content.decode('utf-8')
    except requests.exceptions.RequestException as e:
        # Handle the case where a server is unreachable
        print(f"Warning: Unable to retrieve content from {server_ip}. Error: {e}")
        return f"Unable to retrieve content from {server_ip}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080) 

