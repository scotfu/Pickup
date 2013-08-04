#! /usr/bin/env python
#coding=utf-8
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from record.models import Record
from record.forms import RecordForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@csrf_protect
def create(request):
    if request.method=='POST':
        form=RecordForm(request.POST)
        if form.is_valid():
            record=Record.objects.create(
            	name =form.cleaned_data['name'],
                flight_company = form.cleaned_data['flight_company'],
                flight_no=form.cleaned_data['flight_no'],
                depart=form.cleaned_data['depart'],
                arrive=form.cleaned_data['arrive'],
                depart_airport=form.cleaned_data['depart_airport'],
                arrive_airport=form.cleaned_data['arrive_airport'],
                qq=form.cleaned_data['qq'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                package=form.cleaned_data['package'],
                need_room=form.cleaned_data['need_room'],
                expect_district=form.cleaned_data['expect_district'],
                )
            request.session['record']=record
            return HttpResponseRedirect(reverse('success'))
    else:
        form=RecordForm()

    return render_to_response('record_form.html', {
        'form': form,
        }, context_instance=RequestContext(request))

def success(request):
    record= request.session['record']
    if not record:
        return HttpResponse('Are you kidding?') 
    return render_to_response('record_success.html', {
            'r': record,
        }, context_instance=RequestContext(request))



