# Expectancy formula = (average $ winners * win % + average $ losers * lose %) / (-average $ losers).
# if expectancy is 0.2 then expect 20 cents of gain for every $1 dollar you risk.
averageWinners = float(input("Enter average $ winners: "))
percWinners = float(input("Enter win %: "))
averageLosers = float(input("Enter average $ losers: ")) * -1
percLosers = 100 - float(percWinners)

averageTradeNetProfit = ((averageWinners * (percWinners / 100)) +
                         (averageLosers * (percLosers / 100)))
expectancyVanTharp = averageTradeNetProfit / abs(averageLosers)

print(f"Average Trade Net Profit: {averageTradeNetProfit}")
print(f"Van Tharp Expectancy: {expectancyVanTharp}")
