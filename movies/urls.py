from django.urls import path
from . import views


urlpatterns = [

    path('movies/', views.MovieCreatListView.as_view(), name='movie-create-list-view'),
    path('movies/<int:pk>', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie-details-view'),
    path('movies/stats/', views.MovieStatsView.as_view(), name='movie-stats-view'),
]
