from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import reel_entry,reel_transactions
from django.db.models import Sum

from django.contrib.contenttypes.models import ContentType
# Create your views here.
# def index(request):
#     #return HttpResponse("This is stg's homepage")
#     context= {
#         'variable':'variable bhej diya'
#     }
#     return render(request,'index.html',context)
check = 0
def reel(request):
    return render(request,'reel.html')
def welcome(request):
    return render(request,'welcome.html')
def submit(request):
    if request.method == "POST":
        reel_no = request.POST.get('reel_no')
        reel_gsm = request.POST.get('reel_gsm')
        reel_weight = request.POST.get('reel_weight')
        reel_size = request.POST.get('reel_size')
        reel_date = request.POST.get('reel_date')
        reel_mill = request.POST.get('reel_mill')
        reel_rate = request.POST.get('reel_rate')
        reel_reg = reel_entry(reel_no=reel_no, reel_date=reel_date, reel_gsm=reel_gsm, reel_size=reel_size, reel_weight=reel_weight,reel_mill=reel_mill, reel_rate=reel_rate, reel_balance=reel_weight, reel_amount= int(reel_rate) * int(reel_weight) )
        reel_reg.save()
        reel_tran = reel_transactions(reel_no=reel_no, reel_new_balance=reel_weight, reel_new_utilization=0, reel_new_waste=0, reel_new_amount= int(reel_rate) * int(reel_weight))
        reel_tran.save()
    return render(request,'welcome.html')
def inventory(request):
    
    show=reel_entry.objects.all()
    sum_reelwaste=reel_entry.objects.aggregate(reelwaste=Sum('reel_waste'))
    reelwaste=sum_reelwaste['reelwaste']
    sum_reelbalance=reel_entry.objects.aggregate(reelbalance=Sum('reel_balance'))
    reelbalance=sum_reelbalance['reelbalance']
    sum_reelrate=reel_entry.objects.aggregate(reelrate=Sum('reel_rate'))
    reelrate=sum_reelrate['reelrate']
    sum_reelweight=reel_entry.objects.aggregate(reelweight=Sum('reel_weight'))
    reelweight=sum_reelweight['reelweight']
    sum_reelutilization=reel_entry.objects.aggregate(reelutilization=Sum('reel_utilization'))
    reelutilization=sum_reelutilization['reelutilization']
    sum_reelamount=reel_entry.objects.aggregate(reelamount=Sum('reel_amount'))
    reelamount=sum_reelamount['reelamount']
    list = {'show':show,'reelwaste':reelwaste,'reelrate':reelrate,'reelamount':reelamount,'reelutilization':reelutilization,'reelbalance':reelbalance,'reelweight':reelweight}
    return render(request,'inventory.html',list)
def use(request):
    if request.method == "POST":
        use_reelno = request.POST.get('use_reelno')
        use_sheetheight = request.POST.get('use_sheetheight')
        use_reelquantity = request.POST.get('use_reelquantity')
        #update=reel_entry.objects.filter(reel_no=use_reelno).values_list(flat=True)
        #obj = reel_entry.objects.get(reel_no=use_reelno)
        edit_reel_entry =reel_entry.objects.get(reel_no=use_reelno)
        edit_reel_tran = reel_transactions.objects.get(reel_no=use_reelno)
        #sum = reel_entry.objects.aggregate(Sum('reel_weight'))
        use_reelutilization=((((int(use_sheetheight)*edit_reel_entry.reel_gsm*edit_reel_entry.reel_size)/1525)*int(use_reelquantity))/1000)
       # update.update(reel_utilization=edit.reel_utilization+int(use_reelutilization) )
        reel_balance= edit_reel_entry.reel_balance - int(use_reelutilization)
        edit_reel_entry.reel_utilization=edit_reel_entry.reel_utilization+int(use_reelutilization)
        edit_reel_entry.reel_balance=reel_balance
        edit_reel_entry.reel_amount=edit_reel_entry.reel_rate*reel_balance
        

        edit_reel_tran.reel_old_amount=edit_reel_tran.reel_new_amount
        edit_reel_tran.reel_old_balance=edit_reel_tran.reel_new_balance
        edit_reel_tran.reel_old_utilization=edit_reel_tran.reel_new_utilization
        edit_reel_tran.reel_old_waste=edit_reel_tran.reel_new_waste

        edit_reel_tran.reel_new_balance=reel_balance
        edit_reel_tran.reel_new_amount=edit_reel_entry.reel_rate*reel_balance
        edit_reel_tran.reel_new_utilization=edit_reel_entry.reel_utilization

        edit_reel_entry.save()
        edit_reel_tran.save()
        
        global check
        check=1
        return render(request,'welcome.html')
    
def waste(request):
    if request.method == "POST":
        use_reelno = request.POST.get('use_reelno') 
        edit_reel_entry= reel_entry.objects.get(reel_no=use_reelno)
        edit_reel_tran= reel_transactions.objects.get(reel_no=use_reelno)
        #balance = reel_entry.objects.filter(reel_no=use_reelno).values_list('reel_balance',flat=True)[0]
        #waste = reel_entry.objects.filter(reel_no=use_reelno).values_list('reel_waste',flat=True)[0]
        edit_reel_entry.reel_waste= edit_reel_entry.reel_balance
        edit_reel_entry.reel_balance=0
        edit_reel_entry.reel_amount=0

        edit_reel_tran.reel_new_waste= edit_reel_entry.reel_waste
        edit_reel_tran.reel_old_waste=0
        edit_reel_tran.reel_old_balance=edit_reel_tran.reel_new_balance
        edit_reel_tran.reel_old_amount=edit_reel_tran.reel_new_amount
        edit_reel_tran.reel_new_balance=0 
        edit_reel_tran.reel_new_amount=0
        edit_reel_entry.save()
        edit_reel_tran.save()
        
        
        global check 
        check=2
        return render(request,'welcome.html')
    
def delete(request):
    if request.method == "POST":
        use_reelno = request.POST.get('del_reelno') 
        obj = reel_entry.objects.get(reel_no=use_reelno)
        obj_tran = reel_transactions.objects.get(reel_no=use_reelno)
        obj.delete()
        obj_tran.delete()
        
           
       
        
        

        return render(request,'welcome.html')
    
def undo(request):
    if request.method == "POST":
        undo_reelno = request.POST.get('undo_reelno') 
        edit_reel_tran = reel_transactions.objects.get(reel_no=undo_reelno)
        edit_reel_entry = reel_entry.objects.get(reel_no=undo_reelno)

        global check
        
        if  check==1 :
            edit_reel_tran.reel_new_utilization=edit_reel_tran.reel_old_utilization
            edit_reel_entry.reel_utilization=edit_reel_tran.reel_old_utilization

        edit_reel_tran.reel_new_amount=edit_reel_tran.reel_old_amount
        edit_reel_tran.reel_new_balance=edit_reel_tran.reel_old_balance
        
        edit_reel_tran.reel_new_waste=edit_reel_tran.reel_old_waste

        edit_reel_entry.reel_amount=edit_reel_tran.reel_old_amount
        edit_reel_entry.reel_balance=edit_reel_tran.reel_old_balance

        edit_reel_entry.reel_waste=edit_reel_tran.reel_old_waste

        edit_reel_tran.save()
        edit_reel_entry.save()
        check=0
           
       
        
        

        return render(request,'welcome.html') 


def edit(request):
    if request.method == "POST":
        edit_oldreelno = request.POST.get('edit_oldreelno') 
        edit_newreelno = request.POST.get('edit_newreelno')
        edit_mill = request.POST.get('edit_mill')
        edit_gsm = request.POST.get('edit_gsm')
        edit_size = request.POST.get('edit_size')
        edit_rate = request.POST.get('edit_rate')
        edit_weight = request.POST.get('edit_weight')
        edit_reel_tran = reel_transactions.objects.get(reel_no=edit_oldreelno)
        edit_reel_entry = reel_entry.objects.get(reel_no=edit_oldreelno)

        if edit_mill != '':
            edit_reel_entry.reel_mill= edit_mill

        if edit_gsm != '':
            edit_reel_entry.reel_gsm= edit_gsm 

        if edit_size != '':
            edit_reel_entry.reel_size= edit_size
       
        if edit_rate != '':
            edit_reel_entry.reel_rate= edit_rate

        if edit_weight != '':
            edit_reel_entry.reel_weight= edit_weight
            edit_reel_entry.reel_balance= edit_weight
            edit_reel_tran.reel_old_balance=edit_reel_tran.reel_new_balance
            edit_reel_tran.reel_new_balance=edit_weight

        if edit_weight != '' or edit_rate != '':
            edit_amount = int(edit_weight)*int(edit_rate)
            edit_reel_entry.reel_amount= edit_amount
            edit_reel_tran.reel_old_amount= edit_reel_tran.reel_new_amount
            edit_reel_tran.reel_new_amount= edit_amount        

        if edit_newreelno != '':
            edit_reel_tran.reel_no= edit_newreelno
            edit_reel_entry.reel_no= edit_newreelno           

         


        edit_reel_tran.save()
        edit_reel_entry.save()
        
           
       
        
        

        return render(request,'welcome.html')       



    
def report(request):
  
    return render(request,'report.html')


        


def report_all(request):
    
    show=reel_entry.objects.all().order_by('reel_gsm')
    unique_gsm= reel_entry.objects.values_list('reel_gsm').distinct()
    sum_reelwaste=reel_entry.objects.aggregate(reelwaste=Sum('reel_waste'))
    reelwaste=sum_reelwaste['reelwaste']
    sum_reelbalance=reel_entry.objects.aggregate(reelbalance=Sum('reel_balance'))
    reelbalance=sum_reelbalance['reelbalance']
    sum_reelrate=reel_entry.objects.aggregate(reelrate=Sum('reel_rate'))
    reelrate=sum_reelrate['reelrate']
    sum_reelweight=reel_entry.objects.aggregate(reelweight=Sum('reel_weight'))
    reelweight=sum_reelweight['reelweight']
    sum_reelutilization=reel_entry.objects.aggregate(reelutilization=Sum('reel_utilization'))
    reelutilization=sum_reelutilization['reelutilization']
    sum_reelamount=reel_entry.objects.aggregate(reelamount=Sum('reel_amount'))
    reelamount=sum_reelamount['reelamount']
    list = {'show':show,'reelwaste':reelwaste,'reelrate':reelrate,'reelamount':reelamount,'reelutilization':reelutilization,'reelbalance':reelbalance,'reelweight':reelweight,'unique_gsm':unique_gsm}
    print(len(unique_gsm))
    return render(request,'report_all.html',list)
    
def report_gsm(request):
    if request.method == "POST":
        use_gsm = request.POST.get('req_gsm')
        show=reel_entry.objects.filter(reel_gsm=use_gsm).all()
        sum_reelwaste=show.aggregate(reelwaste=Sum('reel_waste'))
        reelwaste=sum_reelwaste['reelwaste']
        sum_reelbalance=show.aggregate(reelbalance=Sum('reel_balance'))
        reelbalance=sum_reelbalance['reelbalance']
        sum_reelrate=show.aggregate(reelrate=Sum('reel_rate'))
        reelrate=sum_reelrate['reelrate']
        sum_reelweight=show.aggregate(reelweight=Sum('reel_weight'))
        reelweight=sum_reelweight['reelweight']
        sum_reelutilization=show.aggregate(reelutilization=Sum('reel_utilization'))
        reelutilization=sum_reelutilization['reelutilization']
        sum_reelamount=show.aggregate(reelamount=Sum('reel_amount'))
        reelamount=sum_reelamount['reelamount']
        list = {'show':show,'reelwaste':reelwaste,'reelrate':reelrate,'reelamount':reelamount,'reelutilization':reelutilization,'reelbalance':reelbalance,'reelweight':reelweight}
        return render(request,'report_gsm.html',list)
      

