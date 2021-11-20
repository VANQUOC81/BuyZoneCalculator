from colorama import Fore, Back, Style

def CalculateRoi(): 
    # calculate ROI and investment gain/loss based on investment amount
    investmentAmount = float(input("How much did you invest: $ "))
    boughtPrice = float(input("Enter bought price: $ "))
    amountShares = investmentAmount / boughtPrice
    print(f"Amount shares: {amountShares}")
    soldPrice = float(input("Enter sold price: $ "))


    difference = (soldPrice - boughtPrice) * amountShares

    ROI = ((difference)) / (boughtPrice  * amountShares) * 100

    print('\n')

    if difference > 0 :
        print(f"{Fore.GREEN}Investment gain $ {format(difference, '.2f')}")
        print(f'{Fore.GREEN}ROI {ROI}%')
    else :
        print(f"{Fore.RED}Investment loss $ {format(difference, '.2f')}")
        print(f"{Fore.RED}ROI {ROI}%")

    print(Style.RESET_ALL)


while True:
    CalculateRoi()


