from django.urls import path

from . import views


urlpatterns = [
    path("police-orders/", views.PoliceOrdersListView.as_view(), name="api-police-orders-list"),
]