from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from .model import User, Note
from flask import jsonify
from . import db



views = Blueprint('views', __name__)


#fix the way we call the notes from the database
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('note is too short!', category='error')
        else:
            flash('note added!', category='success')
            new_note = Note(data=note, user_id=current_user.id)
            from . import db
            db.session.add(new_note)
            db.session.commit()
            all_notes = Note.query.filter_by(user_id=current_user.id).all()
            return render_template('home.html', user=current_user, notes=all_notes)
    all_notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template('home.html', user=current_user, notes=all_notes)
    



@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    data = request.get_json()
    note_id = data.get('noteId')
    note = Note.query.get(note_id)

    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
        return jsonify({})
    
    return jsonify({'error': 'Note not found or unauthorized'}), 400