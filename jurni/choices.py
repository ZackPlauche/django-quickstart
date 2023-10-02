from django.db.models import TextChoices


class Gender(TextChoices):
    BOY = 'boy'
    GIRL = 'girl'


class Role(TextChoices):
    BOT = 'bot'
    READER = 'reader'