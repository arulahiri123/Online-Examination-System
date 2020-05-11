from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns =[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('courses',views.courses,name='courses'),
    path('',views.ExamViewList.as_view(),name ='list'),
    path('<int:pk>/',views.ExamDetailView.as_view(),name='detail'),
    path('about/',views.about,name = 'about')
]
