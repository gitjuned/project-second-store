from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .TestFire import getdb, getstore
import uuid
from .Common import CUser
import time
import pyrebase
from collections import OrderedDict
#from BookBuddy.Common.TestFire import getdb
#Create your views here.
def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote

def login(request):
    c={}
    return render(request,'./static/template/Login.html',c)

def register(req):
    return render(req,'./static/template/signup.html',{})

def forgotpass(req):
    return render(req,'./static/template/forget.html',{})

def resetpass(req):
    return render(req,'./static/template/reset.html',{})

def addBook(req):
    if CUser.isLogin:
        return render(req, './static/template/addbook.html', {})
    else:
        return render(req, './static/template/gotohome.html', {})
def dashboard(req):
    if CUser.isLogin:
        c = {'user': CUser.currentuser.val()}
        return render(req, './static/template/cong.html', c)
    else:
        return render(req, './static/template/login.html', {})

def verify(request):

    if not CUser.isLogin:
        mail=request.POST.get('mail')
        password=request.POST.get('password')

        db=getdb()
        user=db.child("users").child(mail).get()

        if not user.val():
            return HttpResponse("User does not exist")
        elif (password==user.val().get("password")):
            c={'user':user.val()}
            CUser.currentuser=user
            CUser.isLogin=True
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Wrong password")
    else:
        c = {'user': CUser.currentuser.val()}
        return HttpResponseRedirect('/')

def userlogout(req):
    CUser.isLogin=False
    return render(req, './static/template/login.html', {})


def getcat(req):

    db = getdb()
    allbooks = db.child("bookbuddybook").order_by_child("bookcat").equal_to("Textbook").limit_to_last(1).get().val()
    print(allbooks)
    '''

            "bookbuddybook" : {
                ".indexOn": ["bookcat"]
            },

    '''
    allbook = {'allbooks': allbooks}
    return render(req, 'booklist.html', allbook)


def search(req,test):

    search=req.GET.get('booksearch')
    search_txt=search.lower()
    if len(search)>3:
        db = getdb()
        allbooks = db.child("bookbuddybook").order_by_key().get().val()
        print(allbooks)
        searchBooks = OrderedDict()

        for key,values in allbooks.items():
            for k,name in values.items():
                if k=="name":
                    res=(name.lower()).find(search_txt)
                    if res!=-1:
                        print("Book found")
                        searchBooks[key]=values
        if searchBooks:
            print(searchBooks)
            allbooks = {'searchbooks': searchBooks}
            return render(req, './static/template/results.html', allbooks)
            #return  HttpResponse(allbooks)

        else:

            return  render(req, './static/template/booklist.html',{'book':'True'})


    else:
        return  HttpResponse("Enter more than three character")




def addBookdb(req):

    print("HEre add book db")
    if CUser.isLogin:

        bname = req.POST['bookname']
        publication = req.POST['bpublication']
        author = req.POST['bauthor']
        description = req.POST['bdescription']
        price = req.POST['bprice']
        cat1 = req.POST['bcat1']
        path = "bookimages/"+req.POST['imgpath']

        print(" book db"+bname+publication+author+description)



        bookid = str(time.time())
        bookid=bookid.replace(".","")
        phone = CUser.currentuser.val().get("phone")
        uname = CUser.currentuser.val().get("name")
        imgid = uuid.uuid4().hex


        db = getdb()
        storage = getstore()

        storage.child("BookImages").child(imgid).put(path)
        #imgurl = storage.child("BookImages").child(imgid).get_url(csrfmiddlewaretoken)
        imgurl=f"https://firebasestorage.googleapis.com/v0/b/bookr-98a0a.appspot.com/o/BookImages%2F"+imgid+"?alt=media"
        print(imgurl)
        data = {"name": bname, "publication": publication, "author": author,
                "description": description,  "price": price, "bookcat": cat1,
                 "userphone": phone,"bookimg":imgurl,"username":uname}

        db.child("bookbuddybook").child(bookid).set(data)
        """db = getdb()
        threebooks = db.child("bookbuddybook").order_by_key().limit_to_last(3).get()
        allbooks = db.child("bookbuddybook").order_by_key().get()


        '''

                "bookbuddybook" : {
                    ".indexOn": ["bookcat"]
                },

        '''


        return render(req,'./static/template/gotohome.html',{
            'threebooks':threebooks.val(),
            'allbooks':allbooks.val(),
            })"""
        return HttpResponseRedirect('/')
    else:
        return render(req, './static/template/gotohome.html', {})

def adduser(req):
    name=req.POST['name']
    email=req.POST['email']
    phone=req.POST['phone']
    address=' '#req.POST['address']
    passwrd=req.POST['pass']
    cpasswrd=req.POST['passc']
    stream=' '#req.POST['Streams']

    if(passwrd!=cpasswrd):
        return HttpResponse("Password Not match")
    else:
        db=getdb()
        user = db.child("users").child(phone).get()

        if  user.val():
           return HttpResponse("User exist")

            #return render(req,'./static/template/login.html',{})
        else:
            data = {
                "name": name,"mail":email,"password":passwrd,"phone":phone
             }
            db.child("users").child(phone).set(data)

            return render(req,'./static/template/login.html',{})
'''
def viewbook(req):
    db = getdb()

    allbooks = db.child("bookbuddybook").order_by_key().limit_to_last(3).get()

    allbook={'books':allbooks.val()}
    print(allbook)
    return render(req,'./static/template/booklist.html', allbook)
'''

def cat(req,tst):

    cat=req.GET['category']
    db=getdb()

    bookcat = db.child("bookbuddybook").order_by_child("bookcat").equal_to(cat).get()

    #cat url -- getcat/?category=Other
    return render(req,'./static/template/category.html',{'catbooks':bookcat.val() })


def viewbook(req):
    db = getdb()
    threebooks = db.child("bookbuddybook").order_by_key().limit_to_last(3).get()
    allbooks = db.child("bookbuddybook").order_by_key().get()


    '''

            "bookbuddybook" : {
                ".indexOn": ["bookcat"]
            },

    '''


    return render(req,'./static/template/booklist.html',{
        'threebooks':threebooks.val(),
        'allbooks':allbooks.val(),
        })

def usertestBook(req, pk):
    db = getdb()
    currentBook = db.child("bookbuddybook").child(str(pk)).get()
    print(CUser.isLogin)
    book={"book":currentBook.val(),"islog":CUser.isLogin}
    return render(req,'./static/template/viewbook.html', book)