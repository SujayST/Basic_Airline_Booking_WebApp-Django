from django import forms


class addForm(forms.Form):
    USN = forms.CharField()
    Name = forms.CharField()
    Semester = forms.CharField()
    phone_no = forms.CharField()


class bookForm(forms.Form):
    trn_id = forms.CharField()
    User_id = forms.CharField()
    Airline_id = forms.CharField()
    issue_date = forms.DateField()


class transfer(forms.Form):
    trnid = forms.IntegerField()
    return_date = forms.DateField()
