from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Jenkins Python Demo running successfully!"

def add(a, b):
    return a + b

if __name__ == "__main__":
    result = add(10, 20)
    print(f"The result is: {result}")
    app.run(host="0.0.0.0", port=5000)

