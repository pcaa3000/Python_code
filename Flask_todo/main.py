from flask import request, make_response, redirect,render_template,session,url_for
import unittest

from flask.helpers import flash

from app import create_app
from app.forms import TodoForm,DeleteTodoForm, UpdateTodoForm
from app.firestore_service import get_todos, put_todo, delete_todo, update_todo
from flask_login import login_required,current_user

app=create_app()

todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar video a productor ']


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.cli.command()
def test():
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.route('/')
def index():
    user_ip=request.remote_addr
    response=make_response(redirect('/hello'))
    session['user_ip']=user_ip
    return response

@app.route('/hello', methods=['GET','POST'])
@login_required
def hello():
    user_ip=session.get('user_ip')    
    username=current_user.id
    todo_form=TodoForm()
    delete_todo_form=DeleteTodoForm()
    update_todo_form=UpdateTodoForm()
    context={
        'user_ip':user_ip,
        'username':username,
        'todos': get_todos(username),
        'todo_form':todo_form,
        'delete_todo_form':delete_todo_form,
        'update_todo_form': update_todo_form
    }
    if todo_form.validate_on_submit():
        put_todo(user_id=username,description=todo_form.description.data)
        flash('Tarea agregada...')
        return redirect(url_for('hello'))
        
    return render_template('hello.html',**context)

@app.route('/todos/deletetodo/<todo_id>',methods=['POST'])
def deletetodo(todo_id):    
    user_id=current_user.id
    delete_todo(user_id,todo_id)
    flash('Tarea eliminada...')
    return redirect(url_for('hello'))

@app.route('/todos/updatetodo/<todo_id>/<int:done>',methods=['POST'])
def updatetodo(todo_id,done):
    user_id=current_user.id
    update_todo(user_id,todo_id,done)
    flash('Tarea actualizada...')
    return redirect(url_for('hello'))