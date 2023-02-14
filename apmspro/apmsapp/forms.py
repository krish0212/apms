from django import forms
#from .models import ParkingLot
#from .models import ParkingSlot
from .models import ParkingLot

class ParkingLotForm(forms.ModelForm):
    rows = forms.IntegerField(min_value=1)
    columns = forms.IntegerField(min_value=1)
    class Meta:
        model = ParkingLot
        fields = ['rows', 'columns','slots']
  
     