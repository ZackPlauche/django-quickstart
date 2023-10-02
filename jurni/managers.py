from django.db.models import Manager


class MessageManager(Manager):
    def create_from_gpt_message(self, story, gpt_message):
        self.create(
            content=gpt_message['content'],
            role=gpt_message['role'],
            story=story,
            reader=story.reader,
        )
