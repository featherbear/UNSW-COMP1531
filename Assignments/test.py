from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

site = Blueprint('simple_page', __name__, template_folder='templates')

@site.route('/', defaults={'page': 'index'})
@site.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)