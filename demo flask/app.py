from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        marital_status = request.form['marital_status']
        education = request.form['education']

        return render_template('success.html', name=name, email=email, address=address, phone=phone,
                               marital_status=marital_status, education=education)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
