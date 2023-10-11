from .forms import ContactForm, PhoneNumberFormSet
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Contact, PhoneNumber
from django.views.generic import ListView, DetailView


class ContactCreateView(CreateView):
    model = Contact
    context_object_name = 'contact'
    form_class = ContactForm
    template_name = 'add_contact.html'
    success_url = reverse_lazy('phonebook:contact_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['phone_number_formset'] = PhoneNumberFormSet(self.request.POST, prefix='phone_number')
        else:
            data['phone_number_formset'] = PhoneNumberFormSet(prefix='phone_number')
        print(data)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        phone_number_formset = context['phone_number_formset']
        if phone_number_formset.is_valid():
            self.object = form.save()
            phone_number_formset.instance = self.object
            phone_number_formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    # Add this method to generate extra empty phone number forms
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        phone_number_formset = PhoneNumberFormSet(prefix='phone_number')
        return self.render_to_response(self.get_context_data(form=form, phone_number_formset=phone_number_formset))


class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'contact_list.html'


class ContactDetailView(DetailView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'contact_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact = context['contact']

        # Get the associated phone numbers for the contact
        phone_numbers = PhoneNumber.objects.filter(contact=contact)

        # Pass the phone numbers to the template
        context['phone_numbers'] = phone_numbers
        return context
