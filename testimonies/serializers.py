from django.core.serializers.json import Serializer
from .models import *

class TestimonySerializer(Serializer):
   def get_dump_object(self, obj: Testimony):
        mapped_object = {
            'username': obj.user.username,
            'title': obj.title,
            'testimony': obj.testimony
        }
        return mapped_object