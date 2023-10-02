from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import get_object_or_404

from django.db.models.query import QuerySet

from .models import Reader, Story, Message
from . import serializers
from . import openai


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = serializers.ReaderSerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = serializers.StorySerializer



INITIAL_STORY_PROMPT = 'You are a bedtime story teller for a child named {reader.name} who is {reader.age} year old {reader.gender} and their favorite color is {reader.favorite_color}.'


@api_view(['POST'])
def tell_story(request: Request):
    # Get the story from the request
    story = get_object_or_404(Story, pk=request.data.get('story_id'))

    # Get any messages of they already exist
    messages: QuerySet[Message] = story.messages.all()

    # If no messages exist, start the story.
    if not messages.exists():
        initial_message = Message.objects.create_from_gpt_message(
            story=story,
            gpt_message={
                'content': INITIAL_STORY_PROMPT.format(reader=story.reader),
                'role': 'system',
            },        
        )
        messages = [initial_message]

    gpt_messages = [message.to_gpt_message() for message in messages]
    message = openai.get_message(gpt_messages)
    Message.objects.create()



