from django.shortcuts import render
from .forms import CalcForm

def home(request):
  form = CalcForm()
  context={}
  if(request.method=="POST"):
    dataset = request.POST
    form = CalcForm(request.POST)
    data = dataset.copy()
    
    n = int(data['n'])
    pv = float(data['pv'])
    rate = float(data['rate'])
    pmt = float(data['pmt'])

    context = {'n':n,'pv':pv,'rate':rate,'pmt':pmt,}
    
    begin = 1 if dataset.get('begin') =='b' else 0
    period_data=[]
    sps=[]
    sbs=[]
    eps=[]
    ebs=[]
    i_s=[]

    if(begin==1):
      sp=pv+pmt
      sb=pv+pmt
      i = sb*(rate/100)
      eb=sb+i
      ep=sp
      period_data.append([round(k,2) for k in [sp,sb,i,eb,ep]])
      sbs.append(round(sb,2))
      ebs.append(round(eb,2))
      sps.append(round(sp,2))
      eps.append(round(ep,2))
      i_s.append(round(i,2))
      for j in range(n-1):
        sp+=pmt
        sb=eb+pmt
        i = sb*(rate/100)
        eb=sb+i
        ep=sp
        period_data.append([round(k,2) for k in [sp,sb,i,eb,ep]])
        sbs.append(round(sb,2))
        ebs.append(round(eb,2))
        sps.append(round(sp,2))
        eps.append(round(ep,2))
        i_s.append(round(i,2))
    else:
      sp=pv
      sb=pv
      i = sb*(rate/100)
      eb=sb+i+pmt
      ep=sp+pmt
      period_data.append([round(k,2) for k in [sp,sb,i,eb,ep]])
      sbs.append(round(sb,2))
      ebs.append(round(eb,2))
      sps.append(round(sp,2))
      eps.append(round(ep,2))
      i_s.append(round(i,2))
      for j in range(n-1):
        sp=ep
        sb=eb
        i=sb*(rate/100)
        eb=sb+i+pmt
        ep=sp+pmt
        period_data.append([round(k,2) for k in [sp,sb,i,eb,ep]])
        sbs.append(round(sb,2))
        ebs.append(round(eb,2))
        sps.append(round(sp,2))
        eps.append(round(ep,2))
        i_s.append(round(i,2))
      

    context['tpd']=pmt*n
    context['tot_int'] = round(eb-context['tpd']-pv,2)
    context['fv']=round(eb,2)
    context['pdata']=period_data
    context['balance']=sorted(sbs+ebs)
    context['principal']=sorted(sps+eps)
    context['i_s']=i_s

  context['form']=form









  return render(request, 'calculator/future-value-calculator.html',context)
