from django import forms
from .models import GeeksModel
from .models import LatLngCity
 
 # creating a form
class LatLngCityForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = LatLngCity
 
        # specify fields to be used
        fields = [
            "Latitude",
            "Longitude",
            "City",
            "Zone",
        ]
# creating a form
class GeeksForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = GeeksModel
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]