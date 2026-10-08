from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import Category


class IndexView(TemplateView):
    template_name = "shop/index.html"
    
    def get(self, request, id=None):
        categories = Category.objects.order_by("name")
        filter = request.GET.get("q", "")  # get q or empty string
        if filter != "":
            title = f"Search results for '{filter}'"
            products = Product.objects.filter(name__icontains=filter).order_by("name")
        elif id is None:
            title = "All products"
            products = Product.objects.order_by("name")
        else:
            title = next(c.name for c in categories if c.id == id) 
            products = Product.objects.filter(Category_id=id).order_by("name")
            
        context = {
            "filter": filter,
            "categories": [{"id": c.id, "name": c.name} for c in categories],
            "title": title,
            "products": [{"id": p.id, "name": p.name, "price": p.price, "image": p.image} for p in products]
            }
        template = loader.get_template(self.template_name)
        template = loader.get_template(self.template_name)
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))