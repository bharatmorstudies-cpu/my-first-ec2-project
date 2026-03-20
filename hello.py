from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello! Your Python app is now live on AWS EC2!</h1>"

if __name__ == '__main__':
    # host='0.0.0.0' makes it accessible externally
    app.run(host='0.0.0.0', port=80) 

