from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from safka.models import Restaurant, Vote
from django.utils import simplejson
from datetime import datetime

def home(request):
    restaurants = Restaurant.objects.all()

    return render_to_response('home.html', {'restaurants': restaurants},
                                context_instance=RequestContext(request))
    
def fetch_votes(request):
    votes = Vote.objects.all()

    json = simplejson.dumps([{'voter': v.voter, 'restaurant': v.restaurant.name, 'time': str(v.time)} for v in votes])
    print json
    return HttpResponse(json, content_type='application/json')
    
def add(request):
    voter = request.POST['voter']
    if voter == '':
        return HttpResponse('')
    restaurant = Restaurant.objects.filter(name=request.POST['restaurant'])[0]
    time = request.POST['time']
    
    orig_vote = get_vote(voter)

    if (orig_vote != None):
        orig_vote.restaurant = restaurant
        orig_vote.time = time
        orig_vote.save()
    else:
        new_vote = Vote(voter=voter, restaurant=restaurant, time=time)
        new_vote.save()

    return HttpResponse('')

def clear_votes(request):
    Vote.objects.all().delete()
    return HttpResponse('')


def get_vote(voter):
    for vote in Vote.objects.all():
        if vote.voter == voter:
            return vote
    return None
    
