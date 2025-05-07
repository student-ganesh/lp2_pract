from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        months = age * 12
        days = age * 365
        return f"<h2>{name}'s age is {age} years or {months} months or {days} days</h2>"

    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Age: <input type="number" name="age"><br>
            <input type="submit" value="Calculate">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
