# django-pawapay-integration
This tutorial is about how you can integrate pawapay to your django app to handle payments.

The assumption of this tutorial is that you have some Django knowledge but if you are a complete beginner you will still get something out of it. So first of all visit pawapay and get your token. Replace your actual token in the views.py (pawapay_app) as the token in the mentioned file is wrong. 
Please note that this is just for demonstration purposes, that is why, the token is hard coded. But in production make sure you keep your token in .env file or any other secure forms you prefer.

The requirements for this project to run on your local machine are as follows;

    Django==4.2.11, 

    uuid==1.30, 
  
    requests==2.31.0

Alternatively, you can install the requirements by running "python -m pip install -r requirements.txt" on your terminal if you have cloned this repository. 
Open the terminal with your project path, and in this case it is for pawapay_project and make sure you're able to the manage.py file within it.
After replacing with your actual token, installing the requirements then you can run "python manage.py runserver" on your terminal. 


Click the purchase button to buy the book, and it will redirect you to the pawapay payment page. Enter the phone number from the pawapay test numbers (read pawapay documentation). Click return to merchant button.

Voila, you just learnt how to integrate pawapay in your django app, if you have any questions or concerns feel free to reach to me or contact the pawapay team, you will be assisted accordingly.

Regards

Hope Sain
