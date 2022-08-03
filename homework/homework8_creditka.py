#Представь, что мы пишем программу для банковских карточек. Человек может совершать покупки,
# пока у него на карте хватает на это денег. В начале программы вводим количество денег,
# а потом вводим расходы, пока они не превышают баланс на карте.
# Когда превысили, мы должны получить, сколько успели сделать покупок и сколько осталось денег на карте.

money = int(input("Enter your amount of money:"))
buy = int(input("Enter purchase price:"))
n=0
while money>=0 and money>=buy:
    money=money-buy
    n +=1
    print('Account balance: ',money)
    buy = int(input("Enter the cost of the next purchase:"))
else:
    print('Number os purchase: ',n,'. Account balance: ',money)
