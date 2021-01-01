from Genshin.urls import path
from . import views
from TierList.controllers import registration_controller, character_controller, rarity_controller, element_controller, gender_controller, nation_controller, weapon_controller

urlpatterns = [
    path('', views.index, name='index'),
   
    path('character', character_controller.list_characters, name='character'),
    path('character/add', character_controller.add_character, name='add_character'),
    path('character/edit/<int:character_id>', character_controller.edit_character, name='edit_character'),
    path('character/delete/<int:character_id>', character_controller.delete_character, name='delete_character'),
   
    path('raritys/', rarity_controller.list_raritys, name='raritys'),
    path('rarity/add', rarity_controller.add_rarity, name='add_rarity'),
    path('rarity/edit/<int:rarity_id>', rarity_controller.edit_rarity, name='edit_rarity'),
    path('rarity/delete/<int:rarity_id>', rarity_controller.delete_rarity, name='delete_rarity'),

    path('register', registration_controller.index, name='register'),
]
