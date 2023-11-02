from flask import Flask
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return '<title>insecure-devops</title><p>Welcome to insecure-devops class</p><p>Poor-man CI/CD from: https://github.com/insecurecorp31337/insecure-devops.git</p><p>Test Workflow 1337</p>'
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=False,port=31337,host="0.0.0.0")