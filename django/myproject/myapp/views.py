from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        marital_status = request.POST.get('marital_status')
        education = request.POST.get('education')

        return render(request, 'myapp/success.html', {
            'name': name,
            'email': email,
            'address': address,
            'phone': phone,
            'marital_status': marital_status,
            'education': education
        })

