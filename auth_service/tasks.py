from celery import shared_task

@shared_task
def send_auth_confirmation_email(user_email, token):
    try:
        # Simulate sending an authentication confirmation email
        print(f"Sending authentication confirmation email to {user_email} with token {token}")
        return {"status": "email sent"}
    except Exception as e:
        return {"status": "error", "message": str(e)}