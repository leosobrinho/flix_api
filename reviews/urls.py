from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(), name='review-create-list-view'),
    path('reviews/<int:pk>', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-details-view'),
]
