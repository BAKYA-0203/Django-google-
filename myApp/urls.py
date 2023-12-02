from.import views
from django.urls import path

urlpatterns=[
    path('',views.google,name="google"),
    path('success/',views.success,name="success"),

]