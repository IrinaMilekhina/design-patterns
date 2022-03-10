import pages.views as views

urlpatterns = {
    '/': views.index_page,
    '/contacts/': views.contacts_page,
    '/about/': views.about_page,
}
