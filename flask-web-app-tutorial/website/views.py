# Import necessary modules
from flask import Blueprint, render_template, flash, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db

# Create a blueprint for views
views = Blueprint('views', __name__)

# Define home route
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # Check if the user is authenticated
    if current_user.is_authenticated:
        # Handle POST request for adding a note
        if request.method == 'POST':
            note = request.form.get('note')
            if len(note) < 1:
                flash("Note is too short", category='error')
            else:
                new_note = Note(data=note, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash("Note Added", category='success')
                return redirect(url_for('views.home'))
        # Render home template
        return render_template('home.html', user=current_user)
    else:
        # Redirect to sign up page if user is not logged in
        return render_template("sign_up.html")

# Define delete-note route
@views.route('/delete-note', methods=['POST'])
def delete_note():
    try:
        # Parse JSON data from request
        data = request.json
        note_id = data.get('noteId')
        
        # Query the note with given ID
        note = Note.query.get(note_id)
        
        # Check if the note exists and belongs to the current user
        if note:
            if note.user_id == current_user.id:
                db.session.delete(note)
                db.session.commit()
                flash("Note deleted successfully", category="success")
                return jsonify({"reload": True}), 200
            else:
                flash("You don't have permission to delete this note", category="error")
        else:
            flash("Note not found", category="error")
    except Exception as e:
        flash("An error occurred while deleting the note", category="error")
        print(f"Error deleting note: {e}")
    return jsonify({})  # Return an empty JSON response or redirect as needed
