from django.urls import path

from crud import views

app_name = 'crud'

urlpatterns = [
    path('',views.UserList.as_view(), name='list'),
    path('create/',views.CreateUser.as_view(),name='create'),
    path('update/<pk>/',views.UserUpdate.as_view(),name='update'),
    path('detail/<pk>/',views.UserDetail.as_view(),name='detail'),
    path('delete/<pk>/',views.UserDelete.as_view(),name='delete')
]