from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateMessage.as_view(), name="create"),
    path('', ListMessage.as_view(), name="list"),
]
