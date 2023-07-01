from django.urls import path
from chatgpt import views


urlpatterns = [
    path('fortune-teller/', views.FortuneTeller.as_view(), name=('사주보기')),
    path('tarot/', views.Tarot.as_view(), name="타로보기"),
    path('recommend_name/', views.RecommendName.as_view(), name="이름추천"),
    
]
