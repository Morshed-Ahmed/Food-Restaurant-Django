from django.shortcuts import render

# Create your views here.
def about(request):
    data = [
        {
            "name":"CHRISTOPHER CIPOLLONE",
            "img":"https://images.getbento.com/accounts/d48c31d33aab2e64c03bffa365760c0f/media/images/2041_S7A0684.JPG?w=1200&fit=max&auto=compress,format"
        },
        {
            "name":"JOHN WINTERMAN",
            "img":"https://images.getbento.com/accounts/d48c31d33aab2e64c03bffa365760c0f/media/images/44213_S7A0706.JPG?w=1200&fit=max&auto=compress,format"
        },
        {
            "name":"THE FRANCIE TEAM",
            "img":"https://images.getbento.com/accounts/d48c31d33aab2e64c03bffa365760c0f/media/images/30660IMG_7345.jpg?w=1200&fit=max&auto=compress,format"
        }
    ]
    return render(request,'about.html',{"data":data})