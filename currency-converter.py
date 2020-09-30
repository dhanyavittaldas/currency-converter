import requests 




class CurrencyConvertor:

    def  __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        #first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 
    
        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount



    def perform(self,):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()
    
        converted_amount= self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)
    
        self.converted_amount_field_label.config(text = str(converted_amount))
def input_function():
    
    try:
        converter = CurrencyConvertor(url)
        
        from_currency = str(input("Enter the from currency : ")).upper()
        
        to_currency = str(input("Enter the to currency : ")).upper()
        
        amount = float(input("Enter the amount to be converted : "))
        converted_amount = converter.convert(from_currency,to_currency, amount)
        print(from_currency + ": " + str(amount) + " is " + to_currency + ": " + str(converted_amount) )
        
    
    except KeyError as e:
        print ("I got a KeyError - reason " + str(e))
        input_function()

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    input_function()
    
