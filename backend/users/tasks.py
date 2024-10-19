from django.core.mail import send_mail
from config.celery_config import app


@app.task
def send_code(user_email, code):
    send_mail(
        "Subject here",
        code,
        "from@example.com",
        [user_email],
        fail_silently=False,
    )
