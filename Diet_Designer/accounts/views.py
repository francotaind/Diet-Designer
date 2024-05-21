from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Customer
from django.views import View

# The sign up view
class Signup(View):
    def get(self, request):
        return render(request, 'accounts/signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        confirm_password = postData.get('confirmpassword')

        # Validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        if password != confirm_password:
            error_message = 'Passwords do not match'
        else:
            customer = Customer(first_name=first_name,
                                last_name=last_name,
                                phone=phone,
                                email=email,
                                password=password)
            error_message = self.validateCustomer(customer)

            if not error_message:
                customer.password = make_password(customer.password)
                customer.register()
                return redirect('homepage')

        data = {
            'error': error_message,
            'values': value
        }
        return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "Please Enter your First Name !!"
        elif len(customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len(customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        return error_message

# The log in view
class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'accounts/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return redirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Invalid email or password'
        else:
            error_message = 'Invalid email or password'

        return render(request, 'login.html', {'error': error_message})

# The logout view
def logout(request):
    request.session.clear()
    return redirect('homepage')

# The homepage view
class Homepage(View):
    def get(self, request):
        customer_id = request.session.get('customer')
        customer = None
        if customer_id:
            customer = Customer.objects.get(id=customer_id)
        return render(request, 'base.html', {'customer': customer})
