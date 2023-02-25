from flask import Blueprint, redirect, render_template, request, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def index():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)


@contacts.route("/new", methods=["POST"])
def add_contact():
    data = request.form

    try:
        # Create Contact instance and add data
        new_contact = Contact(data['fullname'], data['email'], data['phone'])
        db.session.add(new_contact)

        # Commit the changes to the database
        db.session.commit()
        flash("Contact created successfuly")
        return redirect("/")
    except Exception as err:
        print(err)
        flash("A problem occurred when creating user")
        return redirect("/")


@contacts.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    contact = Contact.query.get(id)
    if request.method == "POST":
        contact.fullname = request.form.get("fullname")
        contact.email = request.form.get("email")
        contact.phone = request.form.get("phone")
        db.session.commit()
        flash("Contact updated successfuly")
        return redirect(url_for("contacts.index"))

    if request.method == "GET":
        return render_template("update.html", contact=contact)
    return "Method not allowed"


@contacts.route("/delete/<id>")
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash("Contact deleted successfuly")
    return redirect(url_for("contacts.index"))
