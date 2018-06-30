from django.shortcuts import render

def home_page(request):

	if request.method == "GET":
		return render(request, 'haircut/home_page.html')

	if request.method == "POST":
		return render(request, 'haircut/home_page.html')


# Create your views here.
