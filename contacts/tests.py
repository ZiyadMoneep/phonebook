from django.test import TestCase
from django.urls import reverse
from .models import Contact, PhoneNumber


class ContactViewTests(TestCase):
    def test_contact_create_view(self):
        url = reverse('phonebook:add_contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_contact.html')

    def test_contact_create_form_submission(self):
        url = reverse('phonebook:add_contact')
        data = {
            'name': 'Gamall',
            'phone_number_set-TOTAL_FORMS': '2',
            'phone_number_set-INITIAL_FORMS': '0',
            'phone_number_set-MIN_NUM_FORMS': '0',
            'phone_number_set-MAX_NUM_FORMS': '1000',
            'phone_number_set-0-number': '+123-456-7890',
            'phone_number_set-1-number': '+987-654-3210',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Check if the contact and phone numbers were created in the database
        contact = Contact.objects.get(name='Gamal')
        self.assertEqual(contact.phone_numbers.count(), 2)

    def test_contact_list_view(self):
        url = reverse('phonebook:contact_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_list.html')

    def test_contact_detail_view(self):
        contact = Contact.objects.create(name='Ziyad')
        phone_number = PhoneNumber.objects.create(contact=contact, number='555-123-4567')
        url = reverse('phonebook:contact_detail', args=[contact.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ziyad')
        self.assertContains(response, '555-123-4567')
