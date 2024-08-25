from django.shortcuts import render, redirect
from django.http import HttpResponse

# Simulate a database with a global list of accounts
accounts = [
    {'id': 1, 'email': 'gihanatef@gmail.com', 'password': '224455'},
    {'id': 2, 'email': 'safa.abduallah2001@hotmail.com', 'password': '332255'},
]

# Custom function to simulate get_object_or_404 for a list
def get_account_or_404(account_list, id):
    for account in account_list:
        if account['id'] == id:
            return account
    return None

def account_list(request):
    context = {'accounts': accounts}
    return render(request, 'account/createList.html', context)

def account_create(request):
    if request.method == 'POST':
        new_id = len(accounts) + 1
        new_email = request.POST.get('email')
        new_password = request.POST.get('password')

        new_account = {'id': new_id, 'email': new_email, 'password': new_password}

        accounts.append(new_account)

        return redirect('account_list')
    return render(request, 'account/createAccount.html')

def account_update(request, id):
    account = get_account_or_404(accounts, id)
    if not account:
        return HttpResponse("Account not found", status=404)

    if request.method == 'POST':
        account['email'] = request.POST.get('email')
        account['password'] = request.POST.get('password')
        return redirect('account_list')
    return render(request, 'account/updateAccount.html', {'account': account})

def account_delete(request, id):
    account = get_account_or_404(accounts, id)
    if not account:
        return HttpResponse("Account not found", status=404)

    if request.method == 'POST':
        accounts.remove(account)
        return redirect('account_list')
    return render(request, 'account/deleteAccount.html', {'account': account})

def account_details(request, id):
    account = get_account_or_404(accounts, id)
    if not account:
        return HttpResponse("Account not found", status=404)

    return render(request, 'account/accountDetails.html', {'account': account})
