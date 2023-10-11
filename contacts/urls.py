from django.urls import path
from . import views

app_name = 'phonebook'

urlpatterns = [
    path('add-contact/', views.ContactCreateView.as_view(), name='add_contact'),
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('contact-detail/<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),

]
