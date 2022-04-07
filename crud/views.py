from urllib import request
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .forms import LeadsForm
from .models import Leads
from django.template.loader import render_to_string

# Create your views here.

def index(request):

    leads = Leads.objects.all().order_by('-id')

    paginator = Paginator(leads, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html' ,{'page_obj':page_obj})


def save_leads_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            
            data['form_is_valid'] = True
            
            leads = Leads.objects.all().order_by('-id')
            paginator = Paginator(leads, 60) 
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            
            data['html_book_list'] = render_to_string('leads_list.html', {
                'page_obj': page_obj
            })
        else:
            data['form_is_valid'] = False
    
    context = {'form': form}
    
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def leads_create(request):
    if request.method == 'POST':
        form = LeadsForm(request.POST)
    else:
        form = LeadsForm()
    return save_leads_form(request, form, 'leads_create.html')
