#Creating URLs (urls.py) - In order for users to navigate to the curriculum page, we need to create a URL that will be associated with this view.

#This piece of code is created using chatGPT

# idp_app/urls.py
from django.urls import path
from . import views  # Import views from file views.py
from django.contrib.auth import views as auth_views 

urlpatterns = [
    # URL pattern for the learning_plans view
    path('learning-plans/', views.learning_plans, name='learning_plans'),  # URL for the development plans page
    
    # URL pattern for the login page (using Django's built-in login view)
    path('login/', auth_views.LoginView.as_view(), name='login'),
]

# Now we need to include this urls.py file in the main urls.py file of the project 
# so that Django knows where to look for URLs for the application. 
# Next, we need to open the urls.py file in the project folder (myproject/urls.py)



