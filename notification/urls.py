from django.urls import path, include

from notification.views import ListCreateClient, RetrieveUpdateDestroyClient, ListCreateOrder, \
    RetrieveUpdateDestroyMessage, retrieve_report, consolidated_report

urlpatterns = [
    path('clients/', ListCreateClient.as_view()),
    path('client/<int:pk>/', RetrieveUpdateDestroyClient.as_view()),
    path('orders/', ListCreateOrder.as_view()),
    path('message/<int:pk>/', RetrieveUpdateDestroyMessage.as_view()),
    path('report/', consolidated_report),
    path('report/<int:pk>/', retrieve_report),

]