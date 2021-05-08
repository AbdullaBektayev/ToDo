from django.core.mail import send_mail
from celery import shared_task


@shared_task(name='Send_mail_of_done')
def send_mail_of_done(email, task_name):
    try:
        send_mail(
            subject='ToDo app',
            message=f'Congratulations you have done your task '
                    f'( {task_name} )! ^_^',
            recipient_list=[email],
            from_email='uchet.django@gmail.com',
            fail_silently=False,
        )
        return {'success': 'your message was sent correctly'}
    except Exception as exc:
        return {'error': f" Can't sand a message ({exc})"}
