from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        print(request.data)
        serializer = ArticleSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)