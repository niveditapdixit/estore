from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.utils import timezone
from django.db.models import Max
from django.contrib.auth import authenticate

from estore.models import Product
from estore.models import Category
from estore.models import Customer
from estore.forms import RegistrationForm

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
	
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
			# store the customer in DB
            custId = Customer.objects.count() + 1
            new_customer = Customer(customerId= custId, firstName=form.cleaned_data['firstName'],lastName=form.cleaned_data['lastName'],shippingAddress=form.cleaned_data['shippingAddress'],addressline2=form.cleaned_data['addressline2'],city=form.cleaned_data['city'],country=form.cleaned_data['country'],state=form.cleaned_data['state'],zipCode=form.cleaned_data['zipCode'], homePhone=form.cleaned_data['homePhone'],mobilePhone=form.cleaned_data['mobilePhone'] ,emailId=form.cleaned_data['emailId'] ,password=form.cleaned_data['password'])
            new_customer.save()
            # get all featured products from db
            featuredProducts = Product.objects.filter(type="ProductBean").filter(featured="Y").all()
            # get the top 6 best sellers 
            bestSellers = Product.objects.filter(type="ProductBean").filter(salesRank__isnull=False).order_by("salesRank")[:6]            		
            return render(request, "home.html", {"featuredProducts": featuredProducts, "bestSellers": bestSellers}, content_type='text/html')
    else:
        form = RegistrationForm()
        return render(request,'register.html', {'form': form}) 

def login(request):
        user = Customer.objects.get(emailId=request.POST['username'])
        request.session['username'] = user.firstName
            # get all featured products from db
        featuredProducts = Product.objects.filter(type="ProductBean").filter(featured="Y").all()
           # get the top 6 best sellers 
         bestSellers = Product.objects.filter(type="ProductBean").filter(salesRank__isnull=False).order_by("salesRank")[:6]            		
        return render(request, "home.html", {"featuredProducts": featuredProducts, "bestSellers": bestSellers}, content_type='text/html')

def logout(request):
            # get all featured products from db
        featuredProducts = Product.objects.filter(type="ProductBean").filter(featured="Y").all()
           # get the top 6 best sellers 
         bestSellers = Product.objects.filter(type="ProductBean").filter(salesRank__isnull=False).order_by("salesRank")[:6]            		
        return render(request, "home.html", {"featuredProducts": featuredProducts, "bestSellers": bestSellers}, content_type='text/html')
	
	
	
	 
	
