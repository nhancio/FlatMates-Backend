

from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:phone_number>/', views.get_user_profile, name='get_user_profile'),
    path('profile/', views.create_user_profile, name='create_user_profile'),
    path('profile_edit/<int:phone_number>/', views.update_user_profile, name='update_user_profile'),
    path('recommendations_flatmates/', views.recommend_profiles, name='recommend_profiles'),
    path('recommendations_rooms/', views.recommend_rooms, name='recommend_rooms'),
    path('AI_module_voice/', views.AI_module_voice, name='AI_module_voice'),
    path('AI_module_text/', views.AI_module_text, name='AI_module_text'),
    path('create_room_details/', views.create_room_details, name='create_room_details'),
    path('get_room_details/<int:phone_number>/',views.get_room_details, name='get_room_details')

]

