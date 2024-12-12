# Initially, I wrote the code, but it gave a lot of errors and I couldn't run it, 
# so I asked chatGPT a lot of questions to understand what the problem could be, 
# as a result of which the code was changed using chatGPT

from django.shortcuts import render # This imports the render function, 
#which is used to render HTML templates and send data to them.
from django.http import HttpResponseRedirect  # Used for redirection if the user is not logged in
from django.urls import reverse  # Used to get the URL for the login page dynamically
from .models import LearningPlan  # Import the LearningPlan model


# View function for displaying user's study plans
# This view handles the request for displaying the user's learning plans
def learning_plans(request):
    # Retrieving all training plans for the current user
    # Check if the user is authenticated (logged in)
    if not request.user.is_authenticated:
        # If the user is not logged in, redirect them to the login page
        return HttpResponseRedirect(reverse('login'))  # Redirect to the login page
    
    #This line retrieves all the records of the LearningPlan model 
    # that are associated with the current user (this is done by request.user).
    # If the user is authenticated, get the learning plans associated with the logged-in user
    plans = LearningPlan.objects.filter(user=request.user)
    
    # We send this data to the template for display.
    # Render the 'learning_plans.html' template and pass the user's learning plans to it
    return render(request, 'learning_plans.html', {'plans': plans})
    # We pass the plans data to the learning_plans.html template, which will display this data to the user.



