from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
	ordering=['branch']
	actions=['mark_selected_students_as_placed']
	list_display = ('name','branch','roll_no','placed')
	search_fields=["roll_no__exact"]
	def mark_selected_students_as_placed(self,request,queryset):
		rows_updated=queryset.update(placed=True)
		if rows_updated==1:
			message_bit = "1 student was"
		else:
			message_bit="%s students were" % rows_updated
		self.message_user(request,"%s successfully marked as placed" %message_bit)



admin.site.register(Student,StudentAdmin)