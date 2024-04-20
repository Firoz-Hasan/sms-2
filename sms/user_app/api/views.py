from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user_app.api.serializers import RegistrationSerializer


@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email

            refresh = RefreshToken.for_user(account)
            data['token'] = {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                            }
       
        else:
            data = serializer.errors
        
        return Response(data, status=status.HTTP_201_CREATED)
    
    
@api_view(['POST',])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            #user = serializer.validated_data['username']
            token = serializer.validated_data.get('access')
            refresh_token = serializer.validated_data.get('refresh')
            # You can perform additional actions here if needed, like logging user activity
            return Response({
                'username': username,
                'access': str(token),
                'refresh': str(refresh_token),
                
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)