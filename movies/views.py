from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieListDetailSerializer
from reviews.models import Review


class MovieCreatListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)  # para uso da api, deve estar autenticado com jason web token
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)  # para uso da api, deve estar autenticado com jason web token
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()  # contagem de filmes
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))  # filmes por genero
        total_reviews = Review.objects.count()  # quantidade total de avaliações
        avarage_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']  # media de estrelas

        return response.Response(data={
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'avarage_stars': round(avarage_stars, 1) if avarage_stars else 0,
        }, status=status.HTTP_200_OK,

        )
