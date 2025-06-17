from flask import Blueprint, render_template


index_bp = Blueprint('inicio', __name__, url_prefix='/inicio')

@index_bp.route('/')

def index():
    return render_template('index.html')