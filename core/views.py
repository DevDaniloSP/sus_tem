from django.http import HttpResponse
from core.models import Medicamento
from django.views import View
import json

class MedicamentoView(View):
    def get(self, request):
        data = list(Medicamento.objects.values())
        formatted_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(formatted_data, content_type="application/json")
