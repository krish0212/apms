from django.shortcuts import render, redirect,get_object_or_404
from .models import ParkingLot
from .forms import ParkingLotForm
#from .models import ParkingLot

def create_parking_lot(request):
    if request.method == 'POST':
        form = ParkingLotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parking_lots')
    else:
        form = ParkingLotForm()
    return render(request, 'create_parking_lot.html', {'form': form})

def parking_lots(request):
    parking_lots = ParkingLot.objects.all()
    return render(request, 'parking_lots.html', {'parking_lots': parking_lots})

def view_parking_lot(request, id):
    parking_lot = ParkingLot.objects.get(id=id)
    return render(request, 'view_parking_lot.html', {'parking_lot': parking_lot})