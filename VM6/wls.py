from flask import Flask, render_template, request
import requests

app = Flask(__name__)

ip_server1 = "74.234.82.83:8080"  # Replace with your server 1 IP and port
ip_server2 = "20.238.114.112:8080"  # Replace with your server 2 IP and port

@app.route('/')
def index():
        return render_template('index1.html')

@app.route('/weight')
def output():
    load_server1 = float(requests.get("http://" + ip_server1 + "/load").content)
    load_server2 = float(requests.get("http://" + ip_server2 + "/load").content)

    if load_server1 <= load_server2:
        load_result = requests.get("http://" + ip_server1 + "/")
        chosen_server = "Server 1"
    else:
        load_result = requests.get("http://" + ip_server2 + "/")
        chosen_server = "Server 2"
    return render_template('result.html', content=load_result.content, load_server1=load_server1, load_server2=load_server2, chosen_server=chosen_server)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
