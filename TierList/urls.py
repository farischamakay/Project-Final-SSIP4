from Genshin.urls import path
from . import views
from TierList.controllers import registration_controller


urlpatterns = [
    path('', views.index, name='index'),
   
    path('characters/', views.list_characters, name='characters'),
    path('character/add', views.add_character, name='add_character'),
    path('character/edit/<int:character_id>', views.edit_character, name='edit_character'),
    path('character/delete/<int:character_id>', views.delete_character, name='delete_character'),
   
    path('raritys/', views.list_raritys, name='raritys'),
    path('rarity/add', views.add_rarity, name='add_rarity'),
    path('rarity/edit/<int:rarity_id>', views.edit_rarity, name='edit_rarity'),
    path('rarity/delete/<int:rarity_id>', views.delete_rarity, name='delete_rarity'),

    path('register', registration_controller.index, name='register'),
]
