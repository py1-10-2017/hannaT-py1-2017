from django.shortcuts import render, redirect, HttpResponse
import random
secret_key = 'somesecret'

def index(request):
    total_gold = request.session.get('total_gold', 0)
    request.session['total_gold'] = total_gold
    return render(request, 'ninja_gold/index.html')
    

def process_money(request):
    # n = random.randint(a,b)
    building = request.POST['building']
    if building == 'farm':
        # n = random.randint(10,20)
        # request.session['total_gold'] += n
        add_gold(request,10,21,"farm")
    elif building == 'cave':
        # n = random.randint(5,10)
        # request.session['total_gold'] += n
        add_gold(request,5,11,"cave")
    elif building == 'house':
        # n = random.randint(2,5)
        # request.session['total_gold'] += n
        add_gold(request,2,6,"house")
    elif building == 'casino':
        # n = random.randint(-50,50)
        # request.session['total_gold'] += n
        add_gold(request,-50,51,"casino")

    return redirect('/')
def add_gold(request, a,b,place):
    rand_num = random.randint(a,b)
    win = 'Earned {}'.format(rand_num)+" golds from the "+place
    loss = "Entered a "+place+ "  and lost {}".format(rand_num)
    msg = win if rand_num >=0 else loss
    request.session['total_gold'] += rand_num
    
    log = request.session.get('log', [])
    log.append(msg)
    request.session['log'] = log
    print request.session['log']
    