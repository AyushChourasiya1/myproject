from django.http import HttpResponse
from django.shortcuts import render #render is a method of django.shortcuts module which is used to render the template and return the response to the client and also call the page.  
def homepage(request):
    # data = {
    #     'title': 'homenew',#here we are passing the title variable to the template which is present in the templates folder and we can access this variable in the template using {{ title }} syntax
    #     'message': 'This is the homepage of my Django project.',
    #     'clist': ['Python', 'Django', 'JavaScript'],
    #     'studentDetails': [
    #         { 'name': 'John Doe', 'age': 20, 'course': 'Python'},
    #         { 'name': 'Jane Smith', 'age': 22, 'course': 'Django'},
    #         { 'name': 'Alice Johnson', 'age': 19, 'course': 'JavaScript'},
    #     ],
    #     'Numbers': [1, 2, 3, 4, 5],

    #}   
    return render(request, 'index.html') #here we are rendering the index.html template which is present in the templates folder        

def aboutUs(request):
    return render(request, 'about.html')

def courses(request): #request is an object of HttpRequest class which is used to get the request data from the client
    return render(request, 'contact.html')

def coursesdetails(request,):
    return render(request, 'services.html') #here we are passing the course_id variable to the template which is present in the templates folder and we can access this variable in the template using {{ course_id }} syntax

def userfrom(request):
    try:
        name = request.GET['name'] #here we are getting the value of name from the GET request and storing it in the name variable
        email = request.GET['email'] #here we are getting the value of email from the GET request and storing it in the email variable
        message = request.GET['message'] #here we are getting the value of message from the
        print(f"Name: {name}, Email: {email}, Message: {message}") #here we are printing the values of name, email and message in the console
    except:
        pass #here we are using pass statement to ignore the exception if any of the above variables are not present in the GET request    
    return render(request, 'userfrom.html') #here we are rendering the userform.html template which is present in the templates folder