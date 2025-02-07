from django.shortcuts import render, get_object_or_404, redirect
from .models import House, Booking, PaymentRecord, invoice
from django.contrib.auth.decorators import login_required
from .models import Complaint
from .forms import ComplaintForm, PaymentRecordForm
from django.utils.timezone import localtime
from django.contrib import messages
from django.http import JsonResponse


def home(request):
    houses = House.objects.all()
    return render(request, 'houses/home.html', {'houses': houses})

def house_detail(request, house_id):
    house = get_object_or_404(House, id=house_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        # Handle rating submission logic here
        return redirect('house_detail', house_id=house.id)
    return render(request, 'houses/house_detail.html', {'house': house})


def complain_page(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('complain_page')  # Redirect to refresh the page after submission
    else:
        form = ComplaintForm()

    # Retrieve all complaints, order by submission date (latest first)
    complaints = Complaint.objects.all().order_by('-date_submitted')

    context = {
        'form': form,
        'complaints': complaints,
        'localtime': localtime,  # For formatting datetime
    }
    return render(request, 'complain_page.html', context)
def book_house(request, house_id):
    house = House.objects.get(id=house_id)
    if request.method == 'POST':
        room_no = request.POST.get('room_no')  # Get room number
        contact = request.POST.get('contact')  # Get user contact

        Booking.objects.create(user=request.user, house=house, room_no=room_no, contact=contact)
        house.is_booked = True
        house.save()
        return redirect('home')

    return render(request, 'houses/book_house.html', {'house': house})

def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('house')  # Optimize query
    return render(request, 'houses/my_bookings.html', {'bookings': bookings})

def view_invoice(request, booking_id):
     booking = get_object_or_404(Booking, id=booking_id)
     invoices = booking.invoices.all()
     context = {"invoices": invoices, "booking": booking}
     return render(request, "houses/view_invoice.html", context)

def submit_payment(request):
    latest_booking = Booking.objects.filter(user=request.user).order_by('-booking_date').first()

    if request.method == 'POST':
        form = PaymentRecordForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save()

            # Return JSON response for AJAX
            return JsonResponse({
                'success': True,
                'message': 'Your record was received by the admin and is pending for approval.',
                'record': {
                    'date_submitted': payment.date_submitted.strftime('%Y-%m-%d %H:%M:%S'),
                    'name': payment.name,
                    'room_no': payment.room_no,
                    'contact': payment.contact,
                    'receipt_url': payment.receipt.url,
                    'status': payment.status
                }
            })

        else:
            return JsonResponse({'success': False, 'message': 'Invalid form submission.', 'errors': form.errors})

    form = PaymentRecordForm()
    records = PaymentRecord.objects.all()
    return render(request, 'submit_payment.html', {
        'form': form,
        'records': records,
        'latest_booking': latest_booking
    })






