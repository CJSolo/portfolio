from django.shortcuts import render
from .models import customer, customer_notes, announcement, dog
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.


def index(request):
	num_customer = customer.objects.all().count()
	announcements = announcement.objects.all().order_by('-id')[:10]

	context = {  
		'num_customer': num_customer,
		'announcements': announcements
	}
	
	return render(request, 'index.html', context=context)

class customerListView(generic.ListView):
	model = customer
	paginate_by = 10

class customerDetailView(generic.DetailView):
	model = customer

class SearchResultsView(generic.ListView):
	model = customer
	template_name = 'search_results.html'
	def get_queryset(self):
		query = self.request.GET.get("q", default='')
		return customer.objects.filter(Q(name__icontains=query))
	paginate_by = 10

class AnnouncementListView(generic.ListView):
	model = announcement
	paginate_by = 10

class AnnouncementDetailView(generic.DetailView):
	model = announcement

class DogOwnedListView(generic.ListView):
	model = dog
	paginate_by = 10

class CustomerNotesListView(generic.ListView):
	model = customer_notes
	paginate_by = 10

class CustomerCreate(CreateView):
	model = customer
	fields = ['name', 'phone', 'address', 'city', 'state', 'zip_code', 'email_add']

class AnnouncementCreate(CreateView):
	model = announcement
	fields = ['made_by', 'announce']

