from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    count = text.split()
    num = {}
    for i in count:
        if i in num:
            num[i] +=1
        else:
            num[i] = 1
    return render(request, 'result.html',{ 'main' : text, 'total': len(count), 'num_total': num.items()})