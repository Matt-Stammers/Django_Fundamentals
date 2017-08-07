from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    second_dict = {'insert_me': "<b>Hello there Clinical Developer, How may I help thee?</b>"}
    return render(request, 'second_app/index.html', context = second_dict)

def help(request):
    third_dict = {'insert_list': "<li> Yo <ul> YOYO <ul> YOYOYOYOYO </li>"}
    return render(request, 'second_app/help.html', context = third_dict)

def banjo_club(request):
    fourth_dict = {'Banjo_tag': "Did you bring ya banjos boy?"}
    return render(request, 'second_app/banjo_club.html', context = fourth_dict)
