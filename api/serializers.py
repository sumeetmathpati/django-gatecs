from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User


# class UserSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(write_only=True)

#     def create(self, validated_data):

#         user = User.objects.create_user(
#             username=validated_data["username"],
#             password=validated_data["password"],
#         )

#         profile = Profile.objects.create_profile(user=user)

#         return user

#     class Meta:
#         model = User
#         fields = ["id", "username", "first_name", "email", "password"]


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password")


class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ("user", "bio", 'dob', 'gender')

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop("user")
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(
            user=user, 
            bio=validated_data.pop("bio")
        )
        return profile


class LogInSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True, write_only=True)
