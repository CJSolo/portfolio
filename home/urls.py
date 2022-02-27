from django.urls import path
from . import views
from .views import SearchResultsView


urlpatterns = [
	path('', views.index, name='index'),
	path('home/', SearchResultsView.as_view(), name='search_results'),
	path('home/', views.customerListView.as_view(), name='customers'),
	path('home/<int:pk>', views.customerDetailView.as_view(), name='customer-detail'),
	path('home/customer_form.html', views.CustomerCreate.as_view(), name='customer-create'),
	path('home/announcements/', views.AnnouncementCreate.as_view(), name='announcement-create'),
	path('home/announcements/', views.AnnouncementListView.as_view(), name='announcements'),
	path('home/announcements/<int:pk>', views.AnnouncementDetailView.as_view(), name='announcement-detail'),



]