from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "to_do"
urlpatterns = [
    path("",views.index,name='index'),
    path("register/",views.register,name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('login/',LoginView.as_view(template_name='to_do/login.html'),name='login'),
    path('add_task/',views.add_task,name='add_task'),
    path('details/<int:id>/',views.details,name='details'),
    path('edit/<int:id>/',views.edit,name='edit'),
]