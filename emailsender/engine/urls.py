from django.urls import path
from .views import *

urlpatterns = [
    path('post/', CreateMessage.as_view(), name="create"),
    path('list/', ListMessage.as_view(), name="list"),
]
