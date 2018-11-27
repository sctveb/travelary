from django.contrib import admin
from .models import Data
from import_export.admin import ImportExportModelAdmin, ImportMixin
# Register your models here.

# @admin.register(Data)

class MyImportMixin(ImportMixin):
    from_encoding = 'utf-8'
        
class DataAdmin(ImportExportModelAdmin,MyImportMixin):
    pass


admin.site.register(Data, DataAdmin)