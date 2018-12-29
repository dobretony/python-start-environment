from flask_mail import Message
from app import mail
from flask import render_template
from app import new_flask_app
from threading import Thread

def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(new_flask_app, msg)).start()

def send_password_reset_email(user):
    token=user.get_reset_password_token()
    project_name = new_flask_app.config['PROJECT_NAME']
    send_email('[' + str(project_name) + '] Reset your password',
                sender=new_flask_app.config['ADMINS'][0],
                recipients=[user.email],
                text_body=render_template('email/reset_password.txt.j2',
                                         user=user, token=token, project_name=project_name),
                html_body=render_template('email/reset_password.html.j2',
                                         user=user, token=token, project_name=project_name))
