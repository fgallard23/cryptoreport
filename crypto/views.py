from django.shortcuts import render


# Create your views here.
def home(request):
    import requests  # pip install requests
    import json

    # Price Request
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,BSV,USDT,LTC,EOS,BNB,ADA&tsyms=USD')
    price = json.loads(price_request.content)

    # New Request
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote'] # input form
        quote_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+quote+'&tsyms=USD')
        price = json.loads(quote_request.content)

        return render(request, 'prices.html', {'quote': quote, 'price': price})
    else:
        notfound = 'Enter crypto currency symbol in the form above....'
        return render(request, 'prices.html', {'notfound': notfound})

