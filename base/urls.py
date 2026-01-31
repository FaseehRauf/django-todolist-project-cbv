from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
path('register/', RegisterPage.as_view(), name='user-register' ),
path('user-login/', CustomLoginView.as_view(), name='user-login' ),  
path('user-logout/', LogoutView.as_view(next_page='user-login'), name ='user-logout'),
path('', TaskList.as_view(), name='task-list'),
path('task-detail/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
path('task-create/', TaskCreate.as_view(), name='task-create'),
path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),

]
    
