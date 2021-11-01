from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import serializers, status
from rest_framework.response import Response
from .serializers import (
    ProfileSerializer,
    LogInSerializer,
    UserSerializer,
)
from users.models import Profile
from django.contrib.auth.models import User

# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.views import APIView
# from django.http import JsonResponse
# from django.contrib.auth import authenticate


@api_view(["GET"])
def profiles_api(request):

    profiles = Profile.objects.all()
    profieles_serizlied = ProfileSerializer(profiles, many=True)
    return Response(profieles_serizlied.data)


@api_view(["GET"])
def profile_api(request, username):

    profiles = Profile.objects.get(user__username=username)
    profiele_serizlied = ProfileSerializer(profiles)
    return Response(profiele_serizlied.data)


# class Register(CreateAPIView):
#     profiles = Profile.objects.all()
#     serializerd_profile = ProfileSerializer
#     permission_classes = (AllowAny,)


class ProfileAPI(APIView):
    """
    A class based view for creating and fetching student records
    """

    def get(self, request):
        """
        Get all the student records
        :param format: Format of the student records to return to
        :return: Returns a list of student records
        """
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a student record
        :param format: Format of the student records to return to
        :param request: Request object for creating student
        :return: Returns a student record
        """
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


# class logIn(APIView):
#     permission_classes = ()
#     authentication_classes = ()

#     def post(self, request):
#         received_json_data = request.data
#         serializer = LogInSerializer(data=received_json_data)

#         if serializer.is_valid():
#             user = authenticate(
#                 request,
#                 username=received_json_data["username"],
#                 password=received_json_data["password"],
#             )
#             if user is not None:
#                 refresh = RefreshToken.for_user(user)
#                 return JsonResponse(
#                     {
#                         "refresh": str(refresh),
#                         "access": str(refresh.access_token),
#                     },
#                     status=201,
#                 )
#             else:
#                 return JsonResponse(
#                     {
#                         "message": "invalid username or password",
#                     },
#                     status=403,
#                 )
#         else:
#             return JsonResponse({"message": serializer.errors}, status=400)
