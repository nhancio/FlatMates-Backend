from rest_framework import serializers
from .models import UserProfile, RoomDetails

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class RoomDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomDetails
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    room_details = RoomDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['phone_number', 'name', 'gender', 'age', 'location', 'food_choice', 'drinking', 'smoking', 'pet', 'room_details']