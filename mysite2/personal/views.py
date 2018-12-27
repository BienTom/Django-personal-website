from django.shortcuts import render


def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['Jeżeli chcesz się ze mną skontaktować, wyślij proszę maila na:','bienko.tom@gmail.com','lub skorzystaj z linków w stopce.']})