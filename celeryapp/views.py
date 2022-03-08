from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
# from send_mail_app.tasks import send_mail_func
from send_mail_app.forms import ContactFormEmail
from .tasks import test_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")

# def send_mail_to_all(request):
#     send_mail_func.delay()
#     return HttpResponse("Sent")
#
class SendEmail(FormView):
    template_name = "send_mail/contact.html"
    form_class = ContactFormEmail

    def form_valid(self, form):
        form.send_email()
        return HttpResponse("thanks for sending email")


# def schedule_mail(request):
#     schedule, created = CrontabSchedule.objects.get_or_create(hour = 1, minute = 34)
#     task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"5", task='send_mail_app.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
#     return HttpResponse("Done")