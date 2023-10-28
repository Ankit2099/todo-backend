from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *




@api_view(["POST"])
def test_api(request):
    data = request.data
    serializer = taskSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
