# Create your tasks here

from .models import Widget, UserProfile

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Widget.objects.count()

@shared_task
def send_email(user_pk):
    try:
        user = UserProfile.objects.get(pk=user_pk)
        # Simulate sending an email
        print(f"Sending email to {user.user_id}")
        return {"status": "email sent"}
    except UserProfile.DoesNotExist:
        return {"status": "user not found"}
