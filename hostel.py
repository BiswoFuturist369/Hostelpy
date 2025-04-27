from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    field = request.form['field']
    previous_stay = request.form['previous_stay']
    local_relatives = request.form['local_relatives']
    room_type = request.form['room_type']
    ac = request.form['ac']

    prices = {
        'single': {'ac': 120000, 'non_ac': 100000},
        'double': {'ac': 110000, 'non_ac': 90000},
        'triple': {'ac': 100000, 'non_ac': 80000}
    }
    total_price = prices[room_type]['ac' if ac == 'yes' else 'non_ac']

    return render_template('confirmation.html', name=name, age=age, field=field, previous_stay=previous_stay, 
                           local_relatives=local_relatives, room_type=room_type, ac=ac, total_price=total_price)

if __name__ == '__main__':
    app.run(debug=True)
