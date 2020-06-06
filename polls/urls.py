from django.urls import path
from .views import index, detail, results

app_name = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/detail', detail, name="detail"),
    path('<int:question_id>/results', results, name="results"),
]
