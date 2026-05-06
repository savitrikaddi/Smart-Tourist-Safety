from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.models import User
from .models import SOSAlert, TouristProfile
from .serializers import (
    UserSerializer,
    RegisterSerializer,
    TouristProfileSerializer
)
from django.shortcuts import render
from .models import SOSAlert

def dashboard_view(request):
    sos_alerts = SOSAlert.objects.select_related('user').order_by('-timestamp')
    return render(request, 'dashboard/sos_list.html', {'sos_alerts': sos_alerts})




# ---------------- REGISTER NEW USER ----------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# ---------------- LIST ALL TOURISTS (Admin/Test) ----------------
class TouristListView(generics.ListAPIView):
    queryset = TouristProfile.objects.all()
    serializer_class = TouristProfileSerializer
    permission_classes = [IsAuthenticated]



# ---------------- CREATE SOS ALERT ----------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_sos(request):
    user = request.user
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')
    message = request.data.get('message', '')

    if not latitude or not longitude:
        return Response({'error': 'Location data required'}, status=status.HTTP_400_BAD_REQUEST)

    SOSAlert.objects.create(
        user=user,
        latitude=latitude,
        longitude=longitude,
        message=message
    )

    return Response({'message': 'SOS alert created successfully!'}, status=status.HTTP_201_CREATED)
