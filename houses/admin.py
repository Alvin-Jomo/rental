from django.contrib import admin
from .models import House, Booking, PaymentRecord, Complaint, invoice, HouseImage

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'house', 'booking_date', 'room_no', 'contact')
    search_fields = ('user__username', 'house__name')

class HouseImageInline(admin.TabularInline):
    model = HouseImage

class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')  # Include name, rating, and review
    list_filter = ('category',)
    search_fields = ('name', 'description', 'category')
    inlines = [HouseImageInline]

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('booking', 'water_bill', 'rent', 'garbage_fee', 'date_posted', 'is_approved')
    search_fields = ('booking__user__username', 'booking__house__name')
    list_filter = ('is_approved', 'date_posted')

@admin.register(PaymentRecord)
class PaymentRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_no', 'contact', 'date_submitted', 'status', 'amount_received')  # Include amount_received
    list_filter = ('status',)
    search_fields = ('name', 'room_no', 'contact')

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_number', 'date_submitted', 'date_responded', 'response')
    list_filter = ('date_submitted', 'date_responded')
    search_fields = ('name', 'room_number', 'contact', 'message', 'response')
    readonly_fields = ('date_submitted',)

    def save_model(self, request, obj, form, change):
        if obj.response and not obj.date_responded:
            obj.date_responded = timezone.now()
        super().save_model(request, obj, form, change)

admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Booking) 
admin.site.register(invoice)