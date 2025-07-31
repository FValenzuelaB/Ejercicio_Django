from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Producto
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request, "app/home.html", {})

def about(request):
    return render(request, "app/about.html", {})


def listar_productos(request):
    productos=Producto.objects.all()
    return render(request,"lista_de_productos.html", {"productos":productos})

#===CRUD===
class ProductoListView(ListView):
    model = Producto
    template_name = "app/home.html"
    context_object_name = "productos"

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos/producto_detail.html"
    context_object_name = "productos"

class ProductoCreateView(CreateView):
    model = Producto
    template_name = "app/producto_form.html"
    fields = ["nombre", "descripcion", "precio", "stock", "imagen"]
    success_url = reverse_lazy("home")

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "productos/producto_form.html"
    fields = ["nombre", "descripcion", "precio", "stock", "imagen"]
    success_url = reverse_lazy("lista_productos")

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "productos/producto_confirm.html"
    success_url = reverse_lazy("lista_productos")
    #===FIN CRUD===