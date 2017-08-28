from __future__ import unicode_literals
from __future__ import absolute_import
from rest_framework import routers
from django.conf.urls import url, include

from todo.views import TodoViewSet

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]