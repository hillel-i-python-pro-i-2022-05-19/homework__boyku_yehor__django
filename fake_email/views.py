from django.http import HttpResponse

from fake_email.utils import list_fake_users_and_emails


def name_and_email_generated(request, number: int = 100):
    list_with_fake_data = list_fake_users_and_emails(number=number)
    return HttpResponse(f'{list_with_fake_data}')
