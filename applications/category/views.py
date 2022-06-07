from rest_framework import generic
from .models import Category
from .serializers import CategorySerializer


class CategoryListView(generic.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer