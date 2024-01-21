from flask import Flask, render_template, request, redirect, url_for, flash, make_response

app = Flask(__name__)

@app.route('/')
def base_page():
    return render_template('base.html')

@app.get('/number/')
def number_page():
    return render_template('number.html')

@app.post('/number/')
def calc():
    if request.method == 'POST':
        num = int(request.form.get('number'))
        print(num)
    res = f'Квадрат числа {num} равен {num*num}'
    print(res)
    return res


@app.get('/name/')
def name_page():
    return render_template('name.html')

@app.post('/name/')
def hi():
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        response = make_response(render_template('hi_name.html', name=user_name))
        response.set_cookie('name', user_name)
        response.set_cookie('email', user_email)
        return response

@app.route('/delete_cookie/')
def delete_cookie():
    print('DELETE')
    res = make_response("Cookie Removed")
    name = request.form.get('name')
    email = request.form.get('email')
    print(name, email)
    res.set_cookie('name', 'SFSDs', max_age=0)
    res.set_cookie('email', email, max_age=0)
    
    return res



if __name__ == '__main__':
    app.run(debug=True)