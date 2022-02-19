from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse

from .models import frutas
from .forms import frutaForm

class index(View):
    def get(self, request, *args, **kwargs):
        form=frutaForm
        contexto={"form":form}
        return render(request, "index.html",contexto)


class AgregarFruta(CreateView):
    model = frutas
    form_class = frutaForm
    template_name = "Frutas/crearFruta.html"
    success_url = reverse_lazy("listado")

# def pruebas(request):
#     form=frutaForm
#     contexto={"form":form}
#     modelo=frutas
#     if request.method == "POST":
#         guardar=form(request.POST)
#         if guardar.is_valid():
#             guardar.save()
#             return redirect("pruebas")
#         else:
#             errores=guardar.errors
#             mensaje=f"{modelo.__name__} no se registro"
#             response= JsonResponse({"mensaje":mensaje, "errors":errores})
#             response.status_code = 400
#             return response
#         return JsonResponse({"validacion":"si se registro"})
#     else:
#         return render(request, "pruebas.html",contexto)


class pruebas(CreateView):
    model = frutas
    form_class = frutaForm
    template_name = "pruebas.html"
    success_url = reverse_lazy("pruebas")