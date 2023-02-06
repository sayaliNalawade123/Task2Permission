from django.urls import path 
from .views import PostAPIview,PostDetailGenericView


urlpatterns=[
    path('post/',PostAPIview.as_view()),
    path('post<int:pk>/',PostDetailGenericView.as_view()),
]