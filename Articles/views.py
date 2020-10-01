import random
import smtplib

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Articles.models import CustomUser, Post, Comments, contact

OTP = 0


def Home(request):
    post = Post.objects.all()
    return render(request, 'index.html', {"post": post})


def LoginHandle(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        password = request.POST.get('pass')
        user = authenticate(username=Name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully!!")
        else:
            messages.error(request, "Username or Password not found,try again ")
        return redirect("/")


def SignHandle(request):
    if request.method == 'POST':
        Username = request.POST.get('name')
        First = request.POST.get('first')
        Email = request.POST.get('newemail')
        password = request.POST.get('pass')
        Number = request.POST.get('phone')
        address = request.POST.get('address')
        Pic = request.FILES['Picture']
        otp = int(request.POST.get('OTP'))
        try:
            if otp == OTP:
                if Username.isalnum():
                    user = CustomUser.objects.create_user(username=Username, first_name=First, email=Email,
                                                          password=password, Phone_Number=Number, Address=address,
                                                          profile_pic=Pic)
                    user.save()
                    login(request, user)
                    messages.success(request, "Registered Successfully")
                else:
                    messages.error(request, "Username must contains Alphanumeric Characters.")
            else:
                messages.error(request, "Wrong OTP")
        except:
            messages.error(request, "Username already exist,Try another Username.")
        return redirect("/")


def LogoutHandle(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('/')


def Profile(request):
    return render(request, 'profile.html')


def HandlePost(request, Slug):
    if request.method == "POST":
        comment = request.POST.get("comment")
        if request.user.is_authenticated:
            Comment = Comments(Author=request.user.username, Content=comment, Slug=Slug,
                               author_pic=request.user.profile_pic)
        else:
            Comment = Comments(Author="AnonymousUser", Content=comment, Slug=Slug)
        Comment.save()
        return redirect(f"/post/{Slug}")
    else:
        comment = Comments.objects.all().filter(Slug=Slug)
        post = Post.objects.filter(Slug=Slug)
        for query in post:
            related_tag = query.tag
        related_post = Post.objects.all().filter(tag=related_tag)
    return render(request, 'articles.html',
                  {"post": post, "comment": comment, "related_post": related_post, "no_of_comment": comment.count()})


def contact_us(request):
    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("email")
        feedback = request.POST.get("feedback")
        choice = request.POST.get("choice")
        contact(username=username, email=email, feedback=feedback, choice=choice).save()
        messages.success(request, "Thanks for your feedback!!")
        return redirect('/')
    if request.method == "GET":
        return render(request, "contact.html")


def error_404(request, id):
    return render(request, "error_404.html")


def pop(request):
    related_post = Post.objects.all().filter(tag="POP")
    return render(request, "prince_of_persia.html", {"related_post": related_post})


def red(request):
    related_post = Post.objects.all().filter(Title__icontains="i")
    return render(request, "red-dead-redemption.html", {"related_post": related_post})


def assassins(request):
    related_post = Post.objects.all().filter(Title__icontains="i")
    return render(request, "assassins_creed.html", {"related_post": related_post})


def SendOtp(request):
    if request.method == 'POST':
        try:
            global OTP
            OTP = random.randint(1000, 9999)
            print(OTP)
            receivers = request.POST.get('email')
            print(receivers)
            sender = 'mafiacoding100@gmail.com'
            message = f"Your Verification Code is {OTP}"
            smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.ehlo()
            smtpObj.login('mafiacoding100@gmail.com', '8510961367')
            smtpObj.sendmail(sender, receivers, message)
            smtpObj.quit()
            print("Successfully sent email")
        except smtplib.SMTPException:
            print("Error: unable to send email")
        return HttpResponse('')
