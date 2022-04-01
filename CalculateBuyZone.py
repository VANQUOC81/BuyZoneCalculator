from colorama import Fore, Back, Style

# This calculates the buy zone based on inputs of open price and ATR.

def CalculateBuyZone():
    Style.RESET_ALL
    openPrice = float(input(f"{Fore.RESET}What is the Open Price: $ "))
    atr = float(input("What is the ATR: "))
    # fixed 25% range of atr
    range = atr * 0.25
    print(f"Range: {range}")
    incrementOpenPrice = range / 2
    long = openPrice + incrementOpenPrice
    short = openPrice - incrementOpenPrice
    maxLongPriceMovement = openPrice + atr
    maxShortPriceMovement = openPrice - atr
    print(f"{Fore.MAGENTA}Max Long Price Movement: {maxLongPriceMovement}")
    print(f"{Fore.MAGENTA}Max Short Price Movement: {maxShortPriceMovement}")    
    print(f"{Fore.BLUE}Long: {long}")
    print(f"{Fore.RED}Short: {short}")
    
"""     ROI = ((difference)) / (boughtPrice  * amountShares) * 100

    print('\n')

    if difference > 0 :
        print(f"{Fore.GREEN}Investment gain $ {format(difference, '.2f')}")
        print(f'{Fore.GREEN}ROI {ROI}%')
    else :
        print(f"{Fore.RED}Investment loss $ {format(difference, '.2f')}")
        print(f"{Fore.RED}ROI {ROI}%")"""

 


while True:
    CalculateBuyZone()
