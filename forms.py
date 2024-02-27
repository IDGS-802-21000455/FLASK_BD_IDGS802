from wtforms import Form
from wtforms import StringField, TextAreaField,SelectField, RadioField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    nombre=StringField("nombre",[
        validators.DataRequired(message='el campo es reuqerido'),
        validators.length(min=4,max=10,message='ingrese nombre válido')
        ])
    apaterno=StringField("apaterno")
    amaterno=StringField("amaterno")
    edad=IntegerField('edad',[
        validators.number_range(min=1,max=20,message='valor no válido')
    ])
    correo=EmailField("correo",[
        validators.Email(message='Ingrese un correo válido')
    ])
    #materias=SelectField(choices=[('Español','Esp'),('Mat', 'Matematicas'),('Ingles','IN')])
    #radios=RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')])
    
class UserForm2(Form):
    id=IntegerField('id')
    nombre=StringField("nombre",[
        validators.DataRequired(message='el campo es reuqerido'),
        validators.length(min=4,max=10,message='ingrese nombre válido')
        ])
    apaterno=StringField("apaterno")
    email=EmailField("correo",[
        validators.Email(message='Ingrese un correo válido')
    ])