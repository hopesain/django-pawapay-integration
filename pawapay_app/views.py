from django.shortcuts import render, redirect
import uuid
import requests

# Use pawapay test numbers to test everything and get the token from pawapay.
# after getting the token you should define it as follows
# token = "Bearer your-token-here" it will look like something below

token = "Bearer shbdaahbhash1qeyqheq.ajha" # This is a wrong token, I am just showing you how to define it so that you get into trouble, lol.

# Replace 'shbdaahbhash1qeyqheq.ajha' with your actual token from pawapay.

#In production, make sure the token is stored in .env file and not hard coded as shown in this demo.

#Mind you this demo, is just to get you started with less complexity, but handle security accordingly in production.

def homepage(request):
    return render (request, 'homepage.html')

def initialize_payment(request):
    if request.method == 'POST':
        depositId = str(uuid.uuid4()) #This auto generates the uuid for your transaction and converts it to a string.
        amount = str(10000) #The user will enter the amount if you have not specified.
        reason = "PawaPay Book Payment" #The reason will not be shown to the user if you have not specified.

        #Both the amount and reason are optional. Either you can include them or not.

        url = "https://api.sandbox.pawapay.cloud/v1/widget/sessions"
        payload = {
            "depositId": depositId,
            "returnUrl": "http://127.0.0.1:8000/process_payment",
            "amount": amount,
            "reason": reason
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": token
        }
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 201:
            # After successful initialization, this redirects you to the pawapay payment page.
            data = response.json()
            redirect_url = data.get('redirectUrl')
            return redirect (f'{redirect_url}')
        
        elif response.status_code == 400:
            # This happens when you are missing something in your input, for example the returnUrl or depositId.
            # Do not include this logic if you have thoroughly tested it. 
            return render (request, 'missing_something.html')
        
        elif response.status_code == 401:
            #This happens when you are not authorized, so crosscheck your token.
            # Do not include this logic if you have thoroughly tested it.
            return render (request, 'unauthorized.html')
        
    return render (request, 'initialize_payment.html')

def process_payment(request):
    depositId = request.GET.get('depositId') # Getting the Deposit ID in the return url.
    url = "https://api.sandbox.pawapay.cloud/deposits/" + depositId 
    headers = {"Authorization": token}
    response = requests.get(url, headers=headers)
    data = response.json() 
    deposit_information = data[0] 
    status = deposit_information.get("status")

    if status == "COMPLETED":
        #Handle your preferred logic here after successful payment.
        context = {
            'depositId': depositId,
        }
        return render (request, 'successful_payment.html', context)
    
    elif status == "FAILED":
        #Get the failure reason and handle the logic accordingly.
        failureReason = deposit_information.get("failureReason", {})
        failureCode = failureReason.get("failureCode")
        failureMessage = failureReason.get("failureMessage")
        context = {
            'failureCode': failureCode,
            'failureMessage': failureMessage,
            'depositId': depositId,
        }
        return render (request, 'failed_payment.html',  context)
    
    return render (request, 'process_payment.html')
