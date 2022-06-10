import os
from typing import Dict

from flask import send_from_directory, render_template, request, redirect

from app import app
from app.forms import LoginForm
from app.report import send_message_to_admin
from app.tools import default_actions

methods = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']


@app.route('/favicon.ico')
async def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/admin', methods=['GET', 'POST'])
async def admin():
    form = LoginForm()
    if form.validate_on_submit():
        await send_message_to_admin(form.data)
        return redirect('/')
    return render_template('login.html', form=form)


@app.route('/', defaults={'path': ''}, methods=methods)
@app.route('/<path:path>', methods=methods)
async def all_routes(path):
    d: Dict = default_actions(request)
    await send_message_to_admin(d)
    return render_template('base.html')
