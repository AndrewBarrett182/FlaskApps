from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DecimalField, IntegerField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit_name = SubmitField('Add Name')
    date = DateField('Date (YYYY-MM-DD)')
    submit_date = SubmitField('Add Date')
    integer = IntegerField('Integer')
    submit_integer = SubmitField('Add Integer')
    decimal = DecimalField('Decimal')
    submit_decimal = SubmitField('Add Decimal')
    select = SelectField('Choices', choices = [('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    submit_choice = SubmitField('Add Choice')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        submit_name = form.submit_name.data
        date = form.date.data
        submit_date = form.submit_date.data
        integer = form.integer.data
        submit_integer = form.submit_integer.data
        decimal = form.decimal.data
        submit_decimal = form.submit_decimal.data
        select = form.select.data
        submit_choice = form.submit_choice.data

        if submit_name == True:
            if len(first_name) == 0 or len(last_name) == 0:
                error = "Please supply both first and last name"
            else:
                return f"Thank you {first_name} {last_name}!"
        if submit_date == True:
            if date == None:
                error = "Please enter in correct format"
            else:
                return f"Here's the date: {date}"
        if submit_integer == True:
            return f"This is your number: {integer}"
        if submit_decimal == True:
            return f"This is your decimal: {decimal}"
        if submit_choice == True:
            return f"This is your choice: {select}"

    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')