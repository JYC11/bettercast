from rest_framework import generics
from .models import Test
from .serializers import TestSerializer
# Create your views here.

class TestAPIView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer