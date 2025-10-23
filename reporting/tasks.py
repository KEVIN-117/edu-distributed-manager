from celery import shared_task

@shared_task
def generate_report(report_type):
    # Simulate report generation
    return f"Report of type {report_type} generated."