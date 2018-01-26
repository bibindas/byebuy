from django.shortcuts import render
from .models import Brand,Product,Item,Colour,Category,Image
from django.db.models import Q

# Create your views here.
def home(request):
	brand = Brand.objects.all()
	products = Product.objects.all()
	colour = Colour.objects.all()
	brand_name = request.GET.get("brand_name", None)
	print brand_name
	print request.GET
	search = request.GET.get("search","")
	sl_colour = request.GET.get("colours", None)
	sl_type = request.GET.get("sl_type",None)
	sl_price = request.GET.get("sl_price",None)
	query_dict = {}

	if brand_name:
		query_dict["product_brand__brand_name"] = brand_name

	if sl_colour:
		sl_colour = sl_colour.split(",")
		query_dict["product_colour__colour__in"] = sl_colour

	if sl_type:
		query_dict["product_type"] = sl_type
	if sl_price:
		query_dict["product_price__lt"] = sl_price	
	print query_dict
	if query_dict:
		products = Product.objects.filter(**query_dict)	
	if search:
		products = products.filter(Q(product_brand__brand_name__contains=search)|Q(product_item__item_name__contains=search)|Q(product_name__contains=search))
	types = []
	if products:
		first_product = products[0]
		price_max = first_product.product_price
		price_min = first_product.product_price
	else:
		price_min = 0
		price_max = 0
	for i in products:
		if i.product_price > price_max:
			price_max = i.product_price
		if i.product_price < price_min:
			price_min = i.product_price
		if i.product_type not in types:
			types.append(i.product_type)
	print types
	context = {'brand':brand,'types':types,'colour':colour,'products':products}
	context["brand_name"] = brand_name
	context["sl_colour"] = sl_colour
	context["sl_type"] = sl_type
	context["price_min"] = price_min
	context["price_max"] = price_max
	context["sl_price"] = (price_max+price_min)/2
	context["search"] = search
	return render(request,'byebuy/index.html', context)