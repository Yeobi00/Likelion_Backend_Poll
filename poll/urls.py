from django.urls import path
from . import views

urlpatterns = [
    path('poll/', views.poll_list, name='poll_list'),
    path('poll/<int:id>/', views.poll_detail, name='poll_detail'),
    path('poll/<int:id>/agree/', views.poll_agree, name='poll_agree'),
    path('poll/<int:id>/disagree/', views.poll_disagree, name='poll_disagree'),
]