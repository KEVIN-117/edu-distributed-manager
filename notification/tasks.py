from celery import shared_task

@shared_task
def send_notification(user_id, message):
    try:
        # Simulate sending a notification
        print(f"Sending notification to user {user_id}: {message}")
        return {"status": "notification sent"}
    except Exception as e:
        return {"status": "error", "message": str(e)}