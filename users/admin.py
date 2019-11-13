from datetime import datetime
from django.contrib import admin
from django.contrib.messages import ERROR
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import path
from .models import User
from .forms import CsvImportForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_registration', 'date_birthday']
    change_list_template = "changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            for line in csv_file:
                line_data = line.decode().strip().split(',')
                try:
                    data = {
                        'first_name': line_data[0],
                        'last_name': line_data[1],
                        'date_birthday': datetime.strptime(line_data[2], '%Y/%m/%d'),
                        'date_registration': datetime.strptime(line_data[3], '%Y/%m/%d'),
                    }
                    User.objects.update_or_create(**data)
                    self.message_user(request, data)
                except (ValueError, IntegrityError) as e:
                    self.message_user(request, line_data, ERROR)

            self.message_user(request, "Your csv file has been processed")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "csv_form.html", payload
        )
