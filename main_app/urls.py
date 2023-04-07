from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('guitars/', views.guitars_index, name='index'),
    path('guitars/<int:guitar_id>/', views.guitars_detail, name='detail'),
    path('guitars/create/', views.GuitarCreate.as_view(), name='guitars_create'),
    path('guitars/<int:pk>/update/', views.GuitarUpdate.as_view(), name='guitars_update'),
    path('guitars/<int:pk>/delete/', views.GuitarDelete.as_view(), name='guitars_delete'),
    path('guitars/<int:guitar_id>/add_updates/', views.add_updates, name='add_updates'),
    path('upgrade/', views.UpgradeList.as_view(), name='upgrade_index'),
    path('upgrade/<int:pk>/', views.UpgradeDetail.as_view(), name='upgrade_detail'),
    path('upgrade/create/', views.UpgradeCreate.as_view(), name='upgrade_create'),
    path('upgrade/<int:pk>/update/', views.UpgradeUpdate.as_view(), name='upgrade_update'),
    path('upgrade/<int:pk>/delete/', views.UpgradeDelete.as_view(), name='upgrade_delete'),
    path('guitars/<int:guitar_id>/assoc_upgrade/<int:upgrade_id>/', views.assoc_upgrade, name='assoc_upgrade'),
    path('guitars/<int:guitar_id>/delete_upgrade/<int:upgrade_id>/', views.delete_upgrade, name='delete_upgrade'),
]