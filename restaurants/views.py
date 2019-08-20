from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list": [
    		{"restaurant_name": "Maki", "food_type": "Japanese"},
    		{"restaurant_name": "Backyard", "food_type": "Spanish"},
    		{"restaurant_name": "Doppio", "food_type": "Pizza"},
    	],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { 
    	"my_object": {
    		"restaurant_name": "Doppio",
    		"food_type": "Pizza",
    	}
    

    }
    return render(request, 'detail.html', context)
