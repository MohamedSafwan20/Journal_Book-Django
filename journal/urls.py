from django.urls import path
from .views import journal_detail_view

urlpatterns = [
    path('<int:id>', journal_detail_view)
]
