from django.http import HttpResponse


def name_and_email_generated(request, people_amount: int = 100):
    return HttpResponse('hello')
