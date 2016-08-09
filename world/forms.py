# from django.contrib.gis import forms                                    
# from django import forms
from django.contrib.gis import forms
from .models import MapImage
from .models import MapLocation
from .models import HeritageSite
from .models import InterestPoint
from .models import Image

class MapImageForm(forms.ModelForm):
    class Meta:
        model = MapImage
        fields = '__all__'

class MapLocationForm(forms.ModelForm):
    class Meta:
        model = MapLocation
        fields = '__all__'


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


class InterestPointForm(forms.ModelForm):
    class Meta:
        model = InterestPoint
        title = forms.CharField(max_length=50)
        description = forms.CharField(widget=forms.Textarea)    
        exclude = ['location']