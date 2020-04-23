# Flast_SocketIO Report

# Overview
Flask-SocketIO gives Flask applications access to low latency bi-directional communications between the clients and the server (https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/README.md). The documentation is located here https://flask-socketio.readthedocs.io/en/latest/

# SocketIO
We utilize the SocketIO class in the __init__.py file located here https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/flask_socketio/__init__.py Line 56

SocketIO allows us to maintain an open connection with the server whcih gives us ajax functionality. SocketIO utilizes long pulling to maintain the open connection and retrieve data

# Emit 
Emit is a more complex version of send that is used to send events outside of message such as 'update' 'comment' and 'like'. Anything emited to those events with broadcast=true will get that transmission
https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/flask_socketio/__init__.py Line 366

# Send
Send is used to send messages using the predefined message event. The messages can be a string or a JSON blob. It is a simplerversion of emit
https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/flask_socketio/__init__.py Line 428

# License
flask_socketio uses the MIT License found here https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/LICENSE

The MIT License (MIT)

Copyright (c) 2014 Miguel Grinberg

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.