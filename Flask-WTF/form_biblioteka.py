# -*- coding: utf-8 -*
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class LibraryForm(FlaskForm):
    title = StringField("Tytuł", validators=[DataRequired()])
    author = StringField("Autor", validators=[DataRequired()])
    genre = StringField("Gatunek", validators=[DataRequired()])
    pages = IntegerField("Liczba stron", validators=[DataRequired()])
    read = BooleanField("Przeczytane")