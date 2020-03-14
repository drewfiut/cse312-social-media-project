# Flask Report

## Overview
Flask is a lightweight, python microframework that helps setup web applications and run them.  Flask has an easy to use development server to test the webapp and a simple database api to tie into databases.  For phase 1, the features that we used inlcuded a server, routing, and templating.  This made it very easy for us to start developing our front end, instead of working on developing a server.  In addition, Flask helped us with linking in the HTML files.  This is the only part of templating that we used.  In the future, we plan to make a base HTML file and use that as a base for our web app style and using templating to put real data on the website.  

## How

#### Server
To start, our app creates an instanse of Flask, (code [here](https://github.com/pallets/flask/blob/master/src/flask/app.py#L401 "Flask app.py")). The Flask Framework sets up a TCP socket server to handle sending the data of the webapp over the internet.

#### Routing
Flask uses the [werkzeug routing system](https://werkzeug.palletsprojects.com/en/1.0.x/routing/) to route requests.  To point a path to a specific place in an app, a decorator must be used in the form `@app.route('/')`. This will route the `/` path to the following function.  In a simple example, if plain text is returned from the following fuction, then the webpage will serve plain text. For example:
```python
@app.route('/')
def home():
    page = 'hello world!'
    return page
```
This code will display `hello world!` on the page.

#### Templating 
Flask comes out of the box with Jinja2 ready to use.  Jinja is a templating engine that is similar to use as most other templating engines.  Using the templating engine is straight forward.  Use `{{  }}` to insert variables and other things, and `{%  %}` for for-loops, if statements, and extending other pages. The way that Flask sets up Jinja2 can be found [here](https://github.com/pallets/flask/blob/1351d0a56580df36872b466eb245e7634c20dab5/src/flask/templating.py "Templating"). Jinja2 source code can be found [here](https://github.com/pallets/jinja/tree/master/src/jinja2 "Jinja2").

## License
The flask license can be found [here](https://github.com/pallets/flask/blob/master/LICENSE.rst "Flask License").

The license is as follows:

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
  1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
  3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

The Disclaimer Statement is:

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Considering this license, are project is free to use this software in almost any way that we want, and any way that we want in the scope of the project.  As long as we accept liability, we are free to use this framework.  We will not be redistributing this source code, so we don't have to worry about point 1 or 2.