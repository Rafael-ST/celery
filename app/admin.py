from django.contrib import admin
from .models import Pessoa

from .tasks import export_data_to_csv

class PessoaAdmin(admin.ModelAdmin):
    actions = ['export_csv']

    def export_csv(modeladmin, request, queryset):
        selected_records = queryset.all()  # Converta o queryset para uma lista
        print(type(selected_records))
        data_list = []
        for obj in queryset:
            data_list.append({
                'Nome': obj.nome,
            })
        print(type(data_list))
        export_data_to_csv.delay(data_list)

    export_csv.short_description = "Exportar para CSV"

admin.site.register(Pessoa, PessoaAdmin)
