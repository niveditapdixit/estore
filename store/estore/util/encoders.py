import json
from django.db.models.query import QuerySet


from estore.models import Category
from estore.models import Product

class CategoryEncoder(json.JSONEncoder):
    def default(self, object):
        if isinstance(object, Category):
            return {"id":object.categoryId, "name":object.categoryName, "childCategories":[c.categoryId for c in object.childCategories.all()], "childProducts":[prod.productId for prod in object.childProducts.all()]}
        if isinstance(object, QuerySet):
            return {"categories":[cat for cat in object]}
        return None 

class ProductEncoder(json.JSONEncoder):
    def default(self, object):
        if isinstance(object, Product):
            return {"id":object.productId, "partNumber":object.partNumber, "price":object.price(), "imageUrl":"/estore/prodimages/" + str(object.productId) + ".jpg", "inventory":object.stock()}
        if isinstance(object, QuerySet):
            return {"products":[prod for prod in object]}        
        return None 
