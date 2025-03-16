from django.shortcuts import render
from django.conf import settings
import os


# Create your views here.
def home(request):
    # Debug prints
    base_template_path = os.path.join(settings.BASE_DIR, 'templates', 'base.html')
    print(f"Looking for base.html at: {base_template_path}")
    print(f"File exists: {os.path.exists(base_template_path)}")
    print(f"Template dirs: {settings.TEMPLATES[0]['DIRS']}")
    
    return render(request, 'blogs/home.html')

