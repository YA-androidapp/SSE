#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

from flask import Flask, render_template, Response
import time

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/progress')
def progress():
    def generate():
        x = 0
        while x < 100:
            # something to run
            print(x)
            # something to run

            x = x + 1
            time.sleep(0.01)
            yield "data:" + str(x) + "\n\n"
        yield ""
    return Response(generate(), mimetype= 'text/event-stream')

if __name__ == "__main__":
        app.run()