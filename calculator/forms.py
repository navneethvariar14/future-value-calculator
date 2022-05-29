from django import forms

class CalcForm(forms.Form):
  n = forms.IntegerField(label="Number of Periods(N) ",widget=forms.TextInput(attrs={'class':'input-container'}))
  pv = forms.IntegerField(label="Start Amount",widget=forms.TextInput(attrs={'class':'input-container'}))
  rate = forms.IntegerField(label="Interest Rate ",widget=forms.TextInput(attrs={'class':'input-container'}));
  pmt = forms.IntegerField(label="Periodic Deposit ",widget=forms.TextInput(attrs={'class':'input-container'}))
  begin = forms.ChoiceField(label="PMT made at ", choices=[('b','beginning'), ('e','end')],widget=forms.RadioSelect)