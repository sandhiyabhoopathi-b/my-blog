
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home_fun, name="home"),
    path("result/",views.result_fun, name="result"),
    path("update/<int:post_id>/",views.update_fun, name="update"),
    path("delete/<int:post_id>/",views.delete_fun, name="delete"),
]