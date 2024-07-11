from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(
        """
                    <img src="https://i.kym-cdn.com/photos/images/newsfeed/002/492/561/011"
                    alt="Picture of a pig."
                    width="200"
                    height="200"
                    loading="lazy">
                    <h1>Hola mundo!</h1>
                    <p>Parrafo 1</p>
        """
    )
