from django.urls import path,include
from accounts import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('accounts/', views.EmployeeList.as_view()),
    path('accounts/<int:pk>/', views.EmployeeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
