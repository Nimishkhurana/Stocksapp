import re
import urllib.request
ch = 'y'
print('"Welcome in stocks app"')
while ch == 'y':
    url="https://finance.google.com/finance?q="
    stock=input("Enter the stock : ")
    url=url + stock
    dataen=urllib.request.urlopen(url).read()
    data=dataen.decode("utf-8")
    m=re.search('meta itemprop="price"',data)
    start=m.start()
    end=start+50
    newstring=data[start:end]
    m=re.search('content="',newstring)
    start=m.end()
    end=start+5
    string2=newstring[start:]
    m=re.search('"',string2)
    end=m.start()
    string3=string2[:end]
    print("The value of "+stock+" is "+string3)
    while True:
        ch=input("\nDo you want to continue [y/n]: ")
        if ch!='y' and ch!='n':
            print('Invalid choice')
        else:
            if ch=='n':
                print("\nHope to serve you again\nThanks for visiting !!\n")
            break
