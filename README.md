[![Build Status](https://travis-ci.org/PromasterGuru/Fast-Food-API-Endpoints.svg?branch=develop)](https://travis-ci.org/PromasterGuru/Fast-Food-API-Endpoints)  [![Coverage Status](https://coveralls.io/repos/github/PromasterGuru/Fast-Food-API-Endpoints/badge.svg?branch=develop)](https://coveralls.io/github/PromasterGuru/Fast-Food-API-Endpoints?branch=develop)   [![Maintainability](https://api.codeclimate.com/v1/badges/ff5c6bdd4123ad07cfc8/maintainability)](https://codeclimate.com/github/PromasterGuru/Fast-Food-API-Endpoints/maintainability)

# Fast Food API-Endpoints
Creates a set of API endpoints already defined below and use data structures to store data in memory.
<h2>Tools</h2>
1. Server-Side Framework: <a href ="http://flask.pocoo.org/">Flask Python Framework</a><br>
2. Linting Library: <a href ="https://www.pylint.org/">Pylint, a Python Linting Library</a><br>
3. Style Guide: <a href ="https://www.python.org/dev/peps/pep-0008/">PEP8 Style Guide</a><br>
4. Testing Framework: <a href ="https://docs.pytest.org/en/latest/">PyTest, a Python Testing Framework</a><br>

<h2>Endpoints</h2>
<table>
  <tr>
    <th>Functionality</th>
    <th>Method</th>
    <th>Endpoint</th>
  </tr>
  <tr>
    <td>Get all the orders</td>
    <td>GET</td>
    <td>/api/v1/orders</td>
  </tr>
  </tr>
  <tr>
    <td>Fetch a specific order</td>
    <td>GET</td>
    <td>/api/v1/orders/orderId<orderId></td>
  </tr>
  <tr>
    <td>Place a new order</td>
    <td>POST</td>
    <td>/api/v1/orders</td>
  </tr>
  <tr>
    <td>Update the status of an order</td>
    <td>PUT</td>
    <td>/api/v1/orders/orderId</td>
  </tr>
  <tr>
    <td>Delete a specific order</td>
    <td>DELETE</td>
    <td>/api/v1/orders/orderId</td>
  </tr>
</table>

<h2> How to compile and run locally </h2>
<h4> Set up Python3 and Virtualenv in your machine</h4>
1. Install Python 3: <i>sudo install python3</i><br>
2. Install virual environment: <i>pip install virtualenv</i><br><br>
3. Install virtual environement wrapper: <i>pip install virtualenvwrapper<i><br>
4. Create and activate virtual environment
<ul>
<li>export WORKON_HOME=~/Envs</li>
<li>source /usr/local/bin/virtualenvwrapper.sh</li>
<li>mkvirtualenv <name or virtualenv></li>
<li>workon <name or virtualenv></li>
</ul>
5. Clone the project: <i>git clone <a href ="https://github.com/PromasterGuru/Fast-Food-API-Endpoints.git"></a></i><br>
6. Change to project directory: <i>cd Fast-Food-API-Endpoints/</i><br>
7. Install Flask: <i>pip install Flask</i><br>
7. Install modules : <i>pip install -r requirements.txt</i><br>
8. Install coverall: <i>pip install coveralls</i>
<h5>Start Flask server on terminal</h5>
1. export FLASK_APP=run.py<br>
2. export FLASK_ENV=development<br>
3. flask run

<h4>Test the program on <a href ="https://www.getpostman.com/">postman</a></h4>
