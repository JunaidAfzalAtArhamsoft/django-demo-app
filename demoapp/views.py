from django.http import HttpResponse


def home_page(request):
    content = '''
    <h1>Welcome To my first Django App</h1>
    <b>This is the home page of my first web app.</b>
    <p>This is paragraph line, do you like the page?</p>
    
    '''
    return HttpResponse(content)
