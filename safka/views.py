from django.template import Context, loader
from django.http import HttpResponse

def home(request):
    t = loader.get_template('home.html')
    c = Context()
    return HttpResponse(t.render(c))