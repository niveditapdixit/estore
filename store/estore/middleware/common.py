from estore.models import Category
class CategoryLoader(object):
    def process_request(self, request):
        rootCategory = Category.objects.get(pk = 1)
        request.root = rootCategory
        #request.targetProd = rootCategory.childCategories.all()[0].childCategories.all()[0].childProductSet.all()[0].childProductId
        return None