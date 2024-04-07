# -*- coding: utf-8 -*
from flask import Flask, request, render_template, redirect, url_for
from form_biblioteka import LibraryForm
from models_biblioteka import library

app = Flask(__name__)
app.config["SECRET_KEY"] = "hatemondays"

@app.route("/library/", methods=["GET", "POST"])
def library_list():
    form = LibraryForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            library.create(form.data)
            library.save_all()
        return redirect(url_for("library_list"))
    return render_template("library.html", form=form, library=library.all(), error=error)

@app.route("/library/<int:lib_id>/", methods=["GET", "POST"])
def library_details(lib_id):
    lib_details = library.get(lib_id - 1)
    form = LibraryForm(data=lib_details)

    if request.method == "POST":
        if form.validate_on_submit():
            library.update(lib_id - 1, form.data)
        return redirect(url_for("library_list"))
    return render_template("library_det.html", form=form, lib_id=lib_id)

if __name__ == "__main__":
    app.run(debug=True)