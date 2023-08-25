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
    path('inde/', views.inde, name='index'),
    path('new_note', views.new_note, name='new'),
         path('note/<str:pk>', views.note_detail, name='note'),
         path('delete_note/<str:pk>', views.delete_note, name='delete'),
         
         path('dossier/', views.dossier, name='dossier'),
         path('ajouterdossier/', views.patients_without_info_view, name='ajouterdossier'),
         path('add_dossier/', views.patients_with_info_view, name='add_dossier'),
         path('add_info/<int:patient_id>/', views.add_info, name='add_info'),
         path('menu1/', views.menu1_view, name='menu1'),
         path('menu3/', views.menu3_view, name='menu3'),
       #################VMR######################################"
         path('Vmr/', views.reprise_list, name='Vmr'),
         path('ajouter_visite_reprise/<int:patient_id>/', views.visite_reprise, name='ajouter_visite_reprise'),
         path('list_visite_reprise/<int:patient_id>', views.liste_visites_par_patient, name='list_reprise'),
         path('detail_visite_reprise/<int:patient_id>/<str:date_visite>/', views.detail_visite_reprise, name='detail_visite_reprise'),

    ###################VMS###########################################
         path('Vms', views.sys_list, name='Vms'),
         path('liste_visite_par_patient/<int:patient_id>', views.liste_visite_par_patient, name='liste_visite_par_patient'),
         path('ajouter_vms/<int:patient_id>', views.ajouter_vms, name='ajouter_vms'),
         path('liste_analyses/', views.liste_analyses, name='liste_analyses'),
         path('detail_vms/<int:patient_id>/<str:date_visite>/', views.detail_vms, name='detail_vms'),
         path('delete_vms/<int:pk>/<str:date_visite>/', views.delete_vms, name='delete_vms'),
    ####################surveillance######################################
         path('fiche_médicale', views.surveillance_list, name='fiche_médicale'),
         path('add_surveillance/<int:patient_id>/',views.add_surveillance, name='ajouter_surveillance'),
         path('detail_surveillance/<int:patient_id>/<str:date_visite>/', views.detail_surveillance, name='detail_surveillance'),
         path('liste_surveillance_par_patient/<int:patient_id>/', views.liste_surveillance_par_patient, name='liste_surveillance_par_patient'),
         path('patients_sans_laboratoire', views.patients_sans_laboratoire, name='liste_labo'),
         path('scanner_view/<int:visite_id>/<int:analyse_id>/', views.scanner_view, name='scanner_view'),
         path('upload_laboratoire/<int:visite_id>/', views.upload_laboratoire, name='upload_laboratoire'),

    #######################dossier########################################
         path('view_patient_dossier/<int:pk>/', views.view_patient_dossier, name='view_patient_dossier'),
         path('liste_vms_par_patient/<int:pk>/', views.liste_vms_par_patient, name='liste_vms_par_patient'),
         path('detail_of_vms/<int:patient_id>/<str:date_visite>/', views.detail_of_vms, name='detail_of_vms'),
         path('detail_vmr/<int:patient_id>/<str:date_visite>/', views.detail_vmr, name='detail_vmr'),
         path('liste_vmr_par_patient/<int:pk>/', views.liste_vmr_par_patient, name='liste_vmr_par_patient'),
         path('liste_surv_par_patient/<int:pk>/', views.liste_surv_par_patient, name='liste_surv_par_patient'),
         path('detail_sur/<int:patient_id>/<str:date_visite>/', views.detail_surv, name='detail_surv'),
         path('view_info/<int:pk>/', views.view_info, name='view_info'),



    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

