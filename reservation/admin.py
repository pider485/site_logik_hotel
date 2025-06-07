from django.contrib import admin

from reservation.models import Room, Reservation, TypeRoom

# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room','date_start','date_end','phone')
    search_fields = ('date_start','date_end','phone')


admin.site.register(Room)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(TypeRoom)
