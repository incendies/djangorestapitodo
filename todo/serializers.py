from __future__ import unicode_literals
from __future__ import absolute_import
from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'created_at', 'comment', 'completed_at')
