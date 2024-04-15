from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import customer
from django.contrib import messages
from .models import Transaction
import uuid
from django.core.mail import send_mail
from django.conf import settings

from django.http import JsonResponse


def home(request):
    return render(request,"home.html")
def learn(request):

    if request.method=='POST':
        username=request.POST.get('username')





    context={}
    return render(request,"index.html",context)
def register(request):
    return render(request,"register.html")
def admi (request):
    return render(request,"admin.html")
def img(request):
    return render(request,"image.jpeg")
def pay(request):
    return render(request,"payment.html")
def transaction_history(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transaction_history.html', {'transactions': transactions})
def user_details(request):
    return render(request,"user_details.html")
"""def user_login(request):
    return render(request,"user_login.html")"""

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        mobile = request.POST['mobile']
        proof=request.FILES['proof']
        balance = 0
        if password == confirmpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request,'username Already used')
                return redirect('register')
            else:
                # users = User(username = username,email=email,password = password,mobile=mobile,proof=proof)
                #users = User(username = username,email=email,password = password)
                users = User.objects.create_user(username=username, email=email, password=password)
                users.save()
                new_customer = customer()
                new_customer.user = users
                new_customer.confirmpassword = confirmpassword
                new_customer.mobile = mobile
                new_customer.proof = proof
                new_customer.balance = balance
                new_customer.cardid = 'not issued'
                new_customer.save()
                messages.info(request,'User Succesfully Registered!')
                return redirect('learn')
        else:
            messages.info(request,'Password not the same')
            return redirect('register')
    else:
        return render(request,'register.html')
    

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        # Authenticate user
        user = authenticate(request,username=username, password=password)
        print("hi")
        print(user)
        if user is not None:
            # Login successful
            print("0")
            login(request, user)
            return redirect('user_details')  # Redirect to a success page
            print("9")
        else:
            print("2")
            # Login unsuccessful
            messages.error(request, 'Invalid username or password')
            return redirect('learn')  # Render login page again with error message
    else:
        print("3")
        # If GET request, render the login page
        return render(request, 'index.html') 

def logout(request):
    return render(request,'')

def delete(request):
    #username = request.user.username
    request.user.delete()

    messages.error(request, 'Your account is sucessfuly deleted')
    return redirect('learn')  # Render login page again with error messag

def add_money(request):
    if request.method == 'POST':    
        amount = request.POST['amount']
        creditCardNumber = request.POST['creditCardNumber']
        print
        i = int(amount)
        print(i)
        print(request.user.customer.balance)
        request.user.customer.balance = request.user.customer.balance + i
        print(request.user.customer.balance)
        request.user.customer.save() 
       
        transaction_id = str(uuid.uuid4())
        new_transaction = Transaction.objects.create(
            user=request.user,
            amount=amount,
            transaction_id=transaction_id  # Generate unique transaction ID
        )
        new_transaction.save()

        """# Send email to user
        subject = 'Payment Confirmation'
        message = f'Dear {request.user.username},\n\nYour payment of Rs. {amount} has been successfully processed.'
        from_email = settings.EMAIL_HOST_USER
        to_email = [request.user.email]
        send_mail(subject, message, from_email, to_email)"""


        messages.success(request,'Payment Succesfull!')

        return redirect('user_details')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('user_details')



"""def gomail(request):
    if request.method == 'POST':
        # Get user's email from the request or database
        user_email = request.user.email
        user_name=request.user.username
        user_amount=request.user.customer.balance
        # Get transaction details from the database or request
        transaction_details = "Transaction details: User name:{user_name},amount:{user_amount}"  
        send_mail(
            'Transaction details of{user_name}',
            transaction_details,
            'settings.EMAIL_HOST_USER',
            [user_email],
            fail_silently=False
        )
        return render(request,'user_details')"""

       
    
