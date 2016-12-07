from wtforms import Form, BooleanField, StringField, PasswordField, validators

class AddressForm(Form):
	city = StringField('City', [validators.Length(min=4, max=25), validators.DataRequired()])
	state= StringField('State', [validators.Length(min=6, max=35),validators.DataRequired()])
	zipcode = StringField('Zipcode', [validators.Length(min=5, max=5), validators.DataRequired])

