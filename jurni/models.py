from django.db import models

from django.conf import settings
from .choices import Gender, Role
from .managers import MessageManager

# Create your models here.

class Reader(models.Model):
    """A reader is the name of a child or other user who will be reading the stories on their account."""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=Gender.choices, null=True, blank=True)
    favorite_color = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='readers')

    def __str__(self):
        return self.first_name

    def clean(self):
        """When a reader is set to active, disable all other readers."""
        if self.active:
            Reader.objects.exclude(pk=self.pk).update(active=False)

    def save(self, *args, **kwargs):
        """When a reader is set to active, disable all other readers."""
        self.full_clean()
        return super().save(*args, **kwargs)


class Story(models.Model):
    """A story is a collection of pages."""
    title = models.CharField(max_length=100, null=True, blank=True)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='stories')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or super().__str__()

    class Meta:
        ordering = ['-created_at']




class Message(models.Model):
    """A response is the bots or the reader's response to the story."""
    content = models.TextField()
    role = models.CharField(choices=Role.choices, max_length=10)
    sent_at = models.DateTimeField(auto_now_add=True)

    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='messages')
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='messages')

    objects = MessageManager()

    class Meta:
        ordering = ['sent_at']

    def to_gpt_message(self) -> dict:
        """Convert the message to the format required by OpenAI."""
        return {'role': self.role, 'content': self.content}

