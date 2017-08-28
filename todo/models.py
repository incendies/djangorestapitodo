from __future__ import unicode_literals
from __future__ import absolute_import
from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Todo(models.Model):
    title = models.CharField(max_length=30)
    comment = models.TextField()
    created_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'todo'

    def __str__(self):
        return self.title
