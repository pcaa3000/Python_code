from flask import request, make_response, redirect,render_template,session,url_for,flash

from app import create_app
from app.forms import LoginForm

app=create_app()

@app.route('/')
def index():
    user_ip=request.remote_addr
    response=make_response(redirect('/hello'))
    session['user_ip']=user_ip
    return response

@app.route('/hello',methods=['GET','POST'])
def hello():
    user_ip=session.get('user_ip')
    login_form=LoginForm()
    username=session.get('username')
    context={
        'user_ip':user_ip,
        'username':username,
        'login_form':login_form        
    }
    if login_form.validate_on_submit:
        username=login_form.username.data
        session['username']=username
        flash('Usuario registrado correctamente')
        return redirect(url_for('index'))
    
    return render_template('hello.html',**context)