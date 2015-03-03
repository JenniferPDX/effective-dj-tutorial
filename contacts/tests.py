from django.test                            import TestCase
from contacts.models                        import Contact
from django.test.client                     import Client
from django.test.client                     import RequestFactory
from django.test                            import LiveServerTestCase
from selenium.webdriver.firefox.webdriver   import WebDriver
from rebar.testing                          import flatten_to_dict
from contacts                               import forms

# Create your tests here.

class ContactTests( TestCase ):
    """Contact model tests."""
    
    def test_str( self ):
    
        contact = Contact( first_name = 'John', last_name = 'Smith' )
        
        self.assertEquals( str( contact), 'John Smith',)

class EditContactFormTests(TestCase):

    def test_mismatch_email_is_invalid(self):

        form_data = flatten_to_dict(forms.ContactForm())
        form_data['first_name'] = 'Foo'
        form_data['last_name'] = 'Bar'
        form_data['email'] = 'foo@example.com'
        form_data['confirm_email'] = 'bar@example.com'

        bound_form = forms.ContactForm(data=form_data)
        self.assertFalse(bound_form.is_valid())

    def test_same_email_is_valid(self):

        form_data = flatten_to_dict(forms.ContactForm())
        form_data['first_name'] = 'Foo'
        form_data['last_name'] = 'Bar'
        form_data['email'] = 'foo@example.com'
        form_data['confirm_email'] = 'foo@example.com'

        bound_form = forms.ContactForm(data=form_data)
        self.assert_(bound_form.is_valid())