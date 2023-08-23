from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import medicine_list,  ambulance_item_list ,expired_medicines_notification,create_medicine, update_medicine, delete_medicine,view_medicine ,home, create_ambulance_item, update_ambulance_item, delete_ambulance_item, view_ambulance_item,patient_list,update_patient, create_patient, \
    delete_patient, view_patient,ambulance_medicine_list,update_ambulance_medicine, create_ambulance_medicine, delete_ambulance_medicine, view_ambulance_medicine,create_spontaneous_visit,visites_medicales_spontanees,view_visit
urlpatterns = [
    path('medicine/',medicine_list,name='medicines'),
    path('infirmier/', views.dashboard_inf, name='infirmier'),
    path('medecin/', views.dashboard_med, name='medecin'),
    path('home/', home, name='home'),
    path('', views.login_view, name='login'),
    path('admin/', views.admin, name='admin'),
    path('index/', views.index, name='index'),
    path('', views.logout, name='logout'),
    path('patients/', patient_list, name='patients'),
    path('create_patient/', create_patient, name='create_patient'),
    path('update_patient/<int:pk>/', update_patient, name='update_patient'),
    path('delete_patient/<int:pk>/', delete_patient, name='delete_patient'),
    path('view_patient/<int:pk>/', view_patient, name='view_patient'),
    path('create_medicine/',create_medicine,name='create_medicine'),
    path('download_medicine/<str:format>/', views.download_medicines, name='download_medicines'),
    path('update_medicine/<int:pk>/',update_medicine,name='update_medicine'),
    path('delete_medicine/<int:pk>/',delete_medicine,name='delete_medicine'),
    path('view_medicine/<int:pk>/', view_medicine, name='view_medicine'),
    path('ambulance_items/', ambulance_item_list, name='ambulance_items'),
    path('create_ambulance_Item/',create_ambulance_item,name='create_ambulance_Item'),
    path('update_ambulance_Item/<int:pk>/',update_ambulance_item,name='update_ambulance_Item'),
    path('delete_ambulance_Item/<int:pk>/',delete_ambulance_item,name='delete_ambulance_Item'),
    path('view_ambulance_Item/<int:pk>/', view_ambulance_item, name='view_ambulance_Item'),
    path('search_Patient/', views.search_Patient, name='search_Patient'),
    path('search_Medicine/', views.search_Medicine, name='search_Medicine'),
    path('search_AmbulanceItem/', views.search_AmbulanceItem, name='search_AmbulanceItem'),
    path('search_AmbulanceMedicine/', views.search_AmbulanceMedicine, name='search_AmbulanceMedicine'),
    path('liste_controle/', views.liste_controle, name='liste_controle'),
    path('enregistrer_liste_controle/', views.enregistrer_liste_controle, name='enregistrer_liste_controle'),
    path('create_visit/', create_spontaneous_visit, name='create_visit'),
    path('visits/', visites_medicales_spontanees, name='visits'),
    path('view_visit/<int:pk>/', view_visit, name='view_visit'),
    path('historique_visites/<int:pk>/', views.view_histoire_visite, name='view_histoire_visite'),
    path('ambulance_medicine/', ambulance_medicine_list, name='ambulance_medicines'),
    path('create_ambulance_medicine/', create_ambulance_medicine, name='create_ambulance_medicine'),
    path('update_ambulance_medicine/<int:pk>/', update_ambulance_medicine, name='update_ambulance_medicine'),
    path('delete_ambulance_medicine/<int:pk>/', delete_ambulance_medicine, name='delete_ambulance_medicine'),
    path('view_ambulance_medicine/<int:pk>/', view_ambulance_medicine, name='view_ambulance_medicine'),
    path('expired_medicines_notification/', expired_medicines_notification, name='expired_medicines_notification'),
    path('enregistrer_liste_controle/', views.enregistrer_liste_controle, name='enregistrer_liste_controle'),
    path('historique_sauvegardes/', views.historique_sauvegardes, name='historique_sauvegardes'),
    #path('view_check_in_list/<int:pk>/',views.view_check_in_list, name='view_check_in_list'),
    path('enregistrer_fichier/<int:pk>/', views.enregistrer_fichier, name='enregistrer_fichier'),
    path('create_OutStockMedicine/', views.create_OutStockMedicine, name='create_OutStockMedicine'),
    path('outMedicines/', views.outStockMedicine, name='outMedicines'),
    path('search_OutStockMedicine/', views.search_OutStockMedicine, name='search_OutStockMedicine'),
    path('movement_list/', views.movement_list, name='movements'),
    

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

