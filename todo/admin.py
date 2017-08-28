from __future__ import absolute_import
from __future__ import unicode_literals
from django.contrib import admin

from todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Todo, TodoAdmin)
