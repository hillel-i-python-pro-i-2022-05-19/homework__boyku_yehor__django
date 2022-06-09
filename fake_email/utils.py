from faker import Faker
from random import choice
from typing import NamedTuple, Iterator

fake = Faker()


class GenerateUserAndEmail(NamedTuple):
    user: str
    email: str


def create_fake_user_and_email() -> GenerateUserAndEmail:
    domain_name: list = ['gmail', 'yahoo', 'ukr', 'outlook']
    numbers_in_email = range(1000)
    name = fake.first_name()
    email = f'{name}_{choice(numbers_in_email)}@{choice(domain_name)}.com'
    return GenerateUserAndEmail(user=name, email=email)


def create_fake_uses_and_emails(number: int) -> Iterator[GenerateUserAndEmail]:
    for _ in range(number):
        yield create_fake_user_and_email()


def list_fake_users_and_emails(number) -> str:
    return ''.join(
        f'<p>{each_user.user} - {each_user.email}<p>' for each_user in create_fake_uses_and_emails(number=number))
