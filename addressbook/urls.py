from django.views.generic.edit          import CreateView       # For user registration, as per http://www.obeythetestinggoat.com/using-the-built-in-views-and-forms-for-new-user-registration-in-django.html
from django.contrib.auth.forms          import UserCreationForm # For user registration
from django.conf.urls                   import patterns, include, url
from django.contrib                     import admin
from django.contrib.staticfiles.urls    import staticfiles_urlpatterns
import contacts.views

urlpatterns = patterns('',
    url(r'^$',                      contacts.views.ListContactView.as_view(),   name='contacts-list',),
    url(r'^new$',                   contacts.views.CreateContactView.as_view(), name='contacts-new' ,),
    url(r'^edit/(?P<pk>\d+)/$',     contacts.views.UpdateContactView.as_view(), name='contacts-edit',),
    url(r'^delete/(?P<pk>\d+)/$',   contacts.views.DeleteContactView.as_view(), name='contacts-delete',),
    url(r'^(?P<pk>\d+)/$',          contacts.views.ContactView.as_view(),       name='contacts-view',),
    url(r'^edit/(?P<pk>\d+)/addresses$', contacts.views.EditContactAddressView.as_view(), name='contacts-edit-addresses',),
    url(r'^login/$',                'django.contrib.auth.views.login'),
    url(r'^logout/$',               'django.contrib.auth.views.logout'),
    url('^register/',               CreateView.as_view(                             # For user registration
                                        template_name='registration/register.html', # JM: Why do I need to specify the parent directory? 
                                                                                    # Is there a more elegant way? login and logout don't need this specification.
                                        form_class=UserCreationForm,
                                        success_url='/'
                                        )),
    url('^accounts/',               include('django.contrib.auth.urls')),           # For user registration
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
