from rest_framework.response import Response
from rest_framework import generics 
from . models import Trips
from . serializers import TripsSerializer
from rest_framework.permissions import IsAuthenticated #ISAuthenticatedOrReadOnly

class TripsView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Trips.objects.all()

    def get(self, requests, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TripsSerializer(queryset, many=True)
        return Response(serializer.data)
        