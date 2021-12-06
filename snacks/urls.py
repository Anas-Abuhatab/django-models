from django.urls import path
from .views import ThingsListView, DetilListView, DetailView
urlpatterns = [
    path("", ThingsListView.as_view(), name="snack_list"),
    path("<int:pk>", DetilListView.as_view(), name="snack_detail"),
    path("detail", DetailView.as_view(), name="detail"),
]