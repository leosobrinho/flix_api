from django.db.models import Avg
from rest_framework import serializers
from actors.serializers import ActorSerializer
from movies.models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer
from actors.models import Actor



class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

        #reviews = obj.reviews.all()

        #if reviews:
          #  sum_reviews = 0

          #  for review in reviews:
          #      sum_reviews += review.stars

          #  reviews_count = reviews.count()

          #  return round(sum_reviews / reviews_count , 1)


      #  return "Esse filme ainda não possui avaliações"


    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data do lancamento do filme nao pode ser anterior a 1990')
        return value
    
    def validate_resume(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError('Resumo nao pode eceder mais do que 200 caracteres')
        return value

class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True) # campo calculado

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']    

    def get_rate(self, obj): # metodo para calcular
        
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg'] 

        if rate:
            return round(rate, 1)

        return None