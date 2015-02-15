from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.cache import cache_control

from estore.models import Product
from estore.models import Category

def index(request):    
    # get all featured products from db
    featuredProducts = Product.objects.filter(type="ProductBean").filter(featured="Y").all()
    
    # get the top 6 best sellers 
    bestSellers = Product.objects.filter(type="ProductBean").filter(salesRank__isnull=False).order_by("salesRank")[:6]
    
    # render the home page
    return render(request, "home.html", {"featuredProducts": featuredProducts, "bestSellers": bestSellers}, content_type='text/html')

@cache_control(max_age=3000000000)
def getProductImage(request, product_id):
    prod = Product.objects.get(pk=product_id)
    desc = prod.productDescriptions.all()[0]
    imagePath = desc.fullImage
    f = open(imagePath.name, "rb")
    fileContent = f.read()
    f.close()
    return HttpResponse(fileContent, content_type="image/jpeg")


# return all categories as a json feed
def getJSONCategories(request):
    categories = Category.objects.all()
    return HttpResponse(json.dumps(categories, cls=encoders.CategoryEncoder), content_type='application/json')

# return category object as a json feed
def getJSONCategory(request, category_id):
    category = Category.objects.get(pk = category_id)
    return HttpResponse(json.dumps(category, cls=encoders.CategoryEncoder), content_type='application/json')


def productListing(request, categoryId):
    selectedCat = Category.objects.get(pk = categoryId)
    return render(request,'products.html', {'products': selectedCat.childProducts.all, "catName" : selectedCat.categoryName}, content_type='text/html')    
     
def productDetail(request, productId):
    product = Product.objects.get(pk=productId)
    return render(request,'productdetails.html', {'product': product}) 

def getJSONProduct(request, product_id):
    product = Product.objects.get(pk = product_id)
    return HttpResponse(json.dumps(product, cls=encoders.ProductEncoder), content_type="application/json")
