from django.urls import path
from . views import RegistrationView ,LoginView, StandardView, DivisionView, StandardApi,DivisionApi,StaffView, StaffApi

urlpatterns = [
    path('', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='register'),
    path('standard/',StandardView.as_view(),name='standard'),
    path('division/',DivisionView.as_view(), name='division'),
    path('standard/<int:id>/',StandardApi.as_view(),name='standardapi'),
    path('division/<int:id>/',DivisionApi.as_view(),name='divisionupdate'),
    path('staff/', StaffView.as_view(), name='staff'),
    path('staff/<int:id>/',StaffApi.as_view(),name='staffapi'),
]
