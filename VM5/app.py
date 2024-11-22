from flask import Flask, render_template, request, send_file, redirect, url_for, session
import os, psutil, json, time, subprocess, sys
import socket
app = Flask (__name__)

@app.route("/")

def hello():

    html = "<h3>Hello {name}!</h3> <b>Hostname:</b> {hostname} <h3> This is from VM5 </h3> <br/>"

    return html.format(name=os.getenv("NAME", "Kurt"), hostname=socket.gethostname())

@app.route("/load")

def load():

    load=psutil.cpu_percent()

    return str(load)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8080)
