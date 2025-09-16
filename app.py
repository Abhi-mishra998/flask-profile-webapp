from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Replace with your details
    details = {
        "name": "Abhishek Mishra",
        "email": "abhishekmishraji@gmail.com",
        "role": "DevOps / DevSecOps Enthusiast",
        "location": "India"
    }
    return render_template('index.html', details=details)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

