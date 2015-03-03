from django.shortcuts               import render
from django.views.generic           import ListView
from django.core.urlresolvers       import reverse
from django.views.generic           import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators        import method_decorator
from contacts.models                import Contact
from contacts                       import forms

# Create your views here.
class LoggedInMixin(object):

    @method_decorator( login_required )
    def dispatch( self, *args, **kwargs ):
        return super( LoggedInMixin, self ).dispatch( *args, **kwargs )

class ListContactView( LoggedInMixin, ListView ):
    
    model = Contact
    template_name = 'contact_list.html'
    
    def get_queryset( self ):

        return Contact.objects.filter( owner=self.request.user )
    
class CreateContactView( CreateView ):
    
    model = Contact
    template_name = 'edit_contact.html'
    form_class = forms.ContactForm
    
    def get_success_url( self ):
        return reverse( 'contacts-list' )
        
    def get_context_data(self, **kwargs):

        context = super( CreateContactView, self ).get_context_data( **kwargs )
        context[ 'action' ] = reverse( 'contacts-new' )

        return context

class UpdateContactView( UpdateView ):

    model = Contact
    template_name = 'edit_contact.html'
    form_class = forms.ContactForm

    def get_success_url(self):
        return reverse('contacts-list')
        
    def get_context_data(self, **kwargs):

        context = super( UpdateContactView, self ).get_context_data( **kwargs )
        context[ 'action' ] = reverse( 'contacts-edit' ,
                                    kwargs={'pk': self.get_object().id})

        return context
        
class DeleteContactView( DeleteView ):

    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse( 'contacts-list' )
        
class ContactView( DetailView ):

    model = Contact
    template_name = 'contact.html'
    
class EditContactAddressView( UpdateView ):

    model = Contact
    template_name = 'edit_addresses.html'
    form_class = forms.ContactAddressFormSet

    def get_success_url(self):

        # redirect to the Contact view.
        return self.get_object().get_absolute_url()