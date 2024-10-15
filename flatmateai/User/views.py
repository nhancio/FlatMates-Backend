from rest_framework import status, viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile, RoomDetails
from .serializers import UserProfileSerializer, RoomDetailsSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
#from faster_whisper import WhisperModel
#from transformers import BertTokenizer, BertForSequenceClassification
#import torch
import json


model_size = "large-v3"
# Run on GPU with FP16  
#whisper_model = WhisperModel(model_size, compute_type="float16")

"""# Load the personality analysis model
tokenizer = BertTokenizer.from_pretrained("Minej/bert-base-personality")
personality_model = BertForSequenceClassification.from_pretrained("Minej/bert-base-personality")"""


@api_view(['GET'])
def recommend_profiles(request):
    profiles = UserProfile.objects.all()
    serializer = UserProfileSerializer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def recommend_rooms(request):
    profiles = UserProfile.objects.all()
    serializer = UserProfileSerializer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_profile(request, phone_number):
    try:
        profile = UserProfile.objects.get(phone_number=phone_number)
        serializer = UserProfileSerializer(profile)
        return Response({"exists":True}, status = 200)
    except UserProfile.DoesNotExist:
        return Response({"exists":False}, status = 200)

@api_view(['POST'])
def create_user_profile(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_room_details(request):
    serializer = RoomDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_room_details(request, phone_number):
    try:
        profile = RoomDetails.objects.get(user__phone_number=phone_number)
        serializer = RoomDetailsSerializer(profile)
        return Response(serializer.data)
    except UserProfile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_user_profile(request, phone_number):
    try:
        profile = UserProfile.objects.get(phone_number=phone_number)
    except UserProfile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserProfileSerializer(profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def AI_module_voice(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        audio_file = request.FILES['file']
        file_path = default_storage.save(audio_file.name, audio_file)

        try:
            # Perform transcription
            """transcription_result = whisper_model.transcribe(file_path)
            transcribed_text = transcription_result['text']

            # Tokenize and analyze personality
            inputs = tokenizer(transcribed_text, return_tensors="pt")
            outputs = personality_model(**inputs)
            predictions = torch.argmax(outputs.logits, dim=-1)
            personality = predictions.item()"""

            return JsonResponse({
                'transcription': "transcribed_text",
                'personality': "personality"
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        finally:
            # Clean up the saved file
            default_storage.delete(file_path)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def AI_module_text(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            text = data.get('text', '')

            if not text:
                return JsonResponse({'error': 'No text provided'}, status=400)

            # Tokenize and analyze personality
            """inputs = tokenizer(text, return_tensors="pt")
            outputs = personality_model(**inputs)
            predictions = torch.argmax(outputs.logits, dim=-1)
            personality = predictions.item()"""

            return JsonResponse({'text': text, 'personality': "personality"})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)