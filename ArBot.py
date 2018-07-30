from binance.client import Client
import time
from decimal import Decimal
import msvcrt as m
import math

client = Client(key, secret)

print("Connected")

def pauseProgram():
    # Pause program in case of errors and help with debugging
    print("Waiting until key press to allow error study")
    m.getch()
    print("Key has been pressed, now waiting 1,000,000 seconds to continue program")
    time.sleep(1000000)

def coinSearch(coin):
    print("Searching for trades in " + coin)
    try:
        # BTC conversion prices for bnb and eth are found
        bnbBtc = client.get_symbol_ticker(symbol="BNBBTC")
        time.sleep(0.05)
        ethBtc = client.get_symbol_ticker(symbol="ETHBTC")
        time.sleep(0.05)
        bnbBtcPrice = Decimal(bnbBtc.get("price"))
        ethBtcPrice = Decimal(ethBtc.get("price"))
    except:
        print("Error when getting BTC conversion prices")
        pauseProgram()
    try:
        #Orderbooks (which are dictionaries) are retrieved for btc, eth, and bnb in order to get ask and bid prices
        btcBook = client.get_orderbook_ticker(symbol=coin+"BTC")
        time.sleep(0.05)
        ethBook = client.get_orderbook_ticker(symbol=coin+"ETH")
        time.sleep(0.05)
        bnbBook = client.get_orderbook_ticker(symbol=coin+"BNB")
        time.sleep(0.05)
    except:
        print("Error when getting orderbooks for selected coin")
        pauseProgram()

    #Ask and bid prices are found and converted to BTC when needed
    btcAsk = Decimal(btcBook.get("askPrice"))
    btcBid = Decimal(btcBook.get("bidPrice"))
    ethAsk = Decimal(ethBook.get("askPrice")) * ethBtcPrice
    ethBid = Decimal(ethBook.get("bidPrice")) * ethBtcPrice
    bnbAsk = Decimal(bnbBook.get("askPrice")) * bnbBtcPrice
    bnbBid = Decimal(bnbBook.get("bidPrice")) * bnbBtcPrice

    #highest value among trades is found
    if btcBid >= max(ethBid, bnbBid):
        highest = "btc"
        highValue = btcBid
    elif ethBid >= max(btcBid, bnbBid):
        highest = "eth"
        highValue = ethBid
    elif bnbBid >= max(btcBid, ethBid):
        highest = "bnb"
        highValue = bnbBid
    
    print("Highest " + highest + " at " + str(highValue))
    
    #lowest value among trades is found, but prevents the lowest from being the same as the highest
    if highest == "btc":
        if ethAsk <= bnbAsk:
            lowest = "eth"
            lowValue = ethAsk
        else:
            lowest = "bnb"
            lowValue = bnbAsk
    elif highest == "eth":
        if btcAsk <= bnbAsk:
            lowest = "btc"
            lowValue = btcAsk
        else:
            lowest = "bnb"
            lowValue = bnbAsk
    elif highest == "bnb":
        if ethAsk <= btcAsk:
            lowest = "eth"
            lowValue = ethAsk
        else:
            lowest = "btc"
            lowValue = btcAsk

    print("Lowest " + lowest + " at " + str(lowValue))

    #cycle name is given
    trade = lowest + "2" + highest

    #profitability is found
    profit = highValue/lowValue
    print("Profitability is x" + str(profit))

    return trade, profit

def startSearch():
    #This function is not very scaleable in it's current state

    #create a list of the highest profitability for each coin
    coin1trade, coin1profit = coinSearch("LOOM")
    coin2trade, coin2profit = coinSearch("ADX")
    coin3trade, coin3profit = coinSearch("EOS")
    coin4trade, coin4profit = coinSearch("ADA")
    coin5trade, coin5profit = coinSearch("XLM")
    coin6trade, coin6profit = coinSearch("XRP")
    coin7trade, coin7profit = coinSearch("VET")
    coin8trade, coin8profit = coinSearch("NANO")
    coin9trade, coin9profit = coinSearch("NAS")
    coin10trade, coin10profit = coinSearch("ONT")
    

    #cycle with highest profitability is chosen
    if coin1profit >= max(coin2profit, coin3profit, coin4profit, coin5profit, coin6profit, coin7profit, coin8profit, coin9profit, coin10profit):
        coin = "LOOM"
        count = 100
        print("Current best for profit is, " + coin + " at x" + str(coin1profit))
        startTrades(coin, coin1trade, count)
    elif coin2profit >= max(coin1profit, coin3profit, coin4profit, coin5profit, coin6profit, coin7profit, coin8profit, coin9profit, coin10profit):
        coin = "ADX"
        count = 100
        print("Current best for profit is, " + coin + " at x" + str(coin2profit))
        startTrades(coin, coin2trade, count)
    elif coin3profit >= max(coin2profit, coin1profit, coin4profit, coin5profit, coin6profit, coin7profit, coin8profit, coin9profit, coin10profit):
        coin = "EOS"
        count = 100
        print("Current best for profit is, " + coin + " at x" + str(coin3profit))
        startTrades(coin, coin3trade, count)
    elif coin4profit >= max(coin2profit, coin3profit, coin1profit, coin5profit, coin6profit, coin7profit, coin8profit, coin9profit, coin10profit):
        coin = "ADA"
        count = 100
        print("Current best for profit is, " + coin + " at x" + str(coin4profit))
        startTrades(coin, coin4trade, count)
    elif coin5profit >= max(coin2profit, coin3profit, coin4profit, coin1profit, coin6profit, coin7profit, coin8profit, coin9profit, coin10profit):
        coin = "XLM"
        count = 100
        print("Current best for profit is, " + coin + " at x" + str(coin5profit))
        startTrades(coin, coin5trade, count)
    elif coin6profit >= max(coin2profit, coin3profit, coin4profit, coin5profit, coin1profit, coin7profit, coin8profit, coin9profit, coin10profit):
        coin = "XRP"
        count = 100
        print("Current best for profit is, " + coin + " at x" + str(coin6profit))
        startTrades(coin, coin6trade, count)
    elif coin7profit >= max(coin2profit, coin3profit, coin4profit, coin5profit, coin6profit, coin1profit, coin8profit, coin9profit, coin10profit):
        coin = "VET"
        count = 100
        print("Current best for profit is, " + coin + " at x" + str(coin7profit))
        startTrades(coin, coin7trade, count)
    elif coin8profit >= max(coin2profit, coin3profit, coin4profit, coin5profit, coin6profit, coin7profit, coin1profit, coin9profit, coin10profit):
        coin = "NANO"
        count = 100
        print("Current best for profit is, " + coin + " at x" + str(coin8profit))
        startTrades(coin, coin8trade, count)
    elif coin9profit >= max(coin2profit, coin3profit, coin4profit, coin5profit, coin6profit, coin7profit, coin8profit, coin1profit, coin10profit):
        coin = "NAS"
        count = 100
        print("Current best for profit is, " + coin + " at x" + str(coin9profit))
        startTrades(coin, coin9trade, count)
    elif coin10profit >= max(coin2profit, coin3profit, coin4profit, coin5profit, coin6profit, coin7profit, coin8profit, coin9profit, coin1profit):
        coin = "ONT"
        count = 100
        print("Current best for profit is, " + coin + " at x" + str(coin10profit))
        startTrades(coin, coin10trade, count)

def startTrades(coin, trade, count):
    #Create what trades are to be used in cycle
    if trade == "btc2eth":
        trade1 = "ETHBTC"
        trade2 = coin + "BTC"
        trade3 = coin + "ETH"
        trade3pro = "ETHBTC"
        btcTrade = ""

    elif trade == "btc2bnb":
        trade1 = "BNBBTC"
        trade2 = coin + "BTC"
        trade3 = coin + "BNB"
        trade3pro = "BNBBTC"
        btcTrade = ""

    elif trade == "eth2btc":
        trade1 = "ETHBTC"
        trade2 = coin + "ETH"
        trade2pro = "ETHBTC"
        trade3 = coin + "BTC"
        btcTrade = "ETHBTC"
        btcRound = 1000

    elif trade == "eth2bnb":
        trade1 = "BNBETH"
        trade2 = coin + "ETH"
        trade2pro = "ETHBTC"
        trade3 = coin + "BNB"
        trade3pro = "BNBBTC"
        btcTrade = "ETHBTC"
        btcRound = 1000

    elif trade == "bnb2btc":
        trade1 = "BNBBTC"
        trade2 = coin + "BNB"
        trade2pro = "BNBBTC"
        trade3 = coin + "BTC"
        btcTrade = "BNBBTC"
        btcRound = 100

    elif trade == "bnb2eth":
        trade1 = "BNBETH"
        trade2 = coin + "BNB"
        trade2pro = "BNBBTC"
        trade3 = coin + "ETH"
        trade3pro = "ETHBTC"
        btcTrade = "BNBBTC"
        btcRound = 100
        
        

   
    #Check current profitability, if this has changed to no longer be profitable, a new search will begin
    if (trade == "bnb2btc") or (trade == "eth2btc"):
        try:
            #Get orderbooks and btc prices
            trade2book = client.get_orderbook_ticker(symbol=trade2)
            time.sleep(0.05)
            trade3book = client.get_orderbook_ticker(symbol=trade3)
            time.sleep(0.05)
            trade2proBook = client.get_symbol_ticker(symbol=trade2pro)
            time.sleep(0.05)
        except:
            print("Error when getting orderbooks for profitability check, section 1")
            pauseProgram()

        #Get btc conversion price
        trade2proPrice = Decimal(trade2proBook.get("price"))
        
        #Get bid and ask prices all in BTC
        trade2Ask = Decimal(trade2book.get("askPrice")) * trade2proPrice
        trade3Bid = Decimal(trade3book.get("bidPrice"))

        #bid/ask to find profitability
        profit = trade3Bid/trade2Ask
    elif (trade == "btc2eth") or (trade == "btc2bnb"):
        try:
            #Get orderbooks and btc prices
            trade2book = client.get_orderbook_ticker(symbol=trade2)
            time.sleep(0.05)
            trade3book = client.get_orderbook_ticker(symbol=trade3)
            time.sleep(0.05)
            trade3proBook = client.get_symbol_ticker(symbol=trade3pro)
            time.sleep(0.05)
        except:
            print("Error when getting orderbooks for profitability check, section 2")
            pauseProgram()

        #Get btc conversion price
        trade3proPrice = Decimal(trade3proBook.get("price"))

        #Get bid and ask prices all in BTC
        trade2Ask = Decimal(trade2book.get("askPrice"))
        trade3Bid = Decimal(trade3book.get("bidPrice")) * trade3proPrice

        #bid/ask to find profitability
        profit = trade3Bid/trade2Ask
    else:
        try:
            #Get orderbooks and btc prices
            trade2book = client.get_orderbook_ticker(symbol=trade2)
            time.sleep(0.05)
            trade3book = client.get_orderbook_ticker(symbol=trade3)
            time.sleep(0.05)
            trade2proBook = client.get_symbol_ticker(symbol=trade2pro)
            time.sleep(0.05)
            trade3proBook = client.get_symbol_ticker(symbol=trade3pro)
            time.sleep(0.05)
        except:
            print("Error when getting orderbooks for profitability check, section 3")
            pauseProgram()

        #Get btc conversion price
        trade2proPrice = Decimal(trade2proBook.get("price"))
        trade3proPrice = Decimal(trade3proBook.get("price"))
        
        #Get bid and ask prices all in BTC
        trade2Ask = Decimal(trade2book.get("askPrice")) * trade2proPrice
        trade3Bid = Decimal(trade3book.get("bidPrice")) * trade3proPrice

        #bid/ask to find profitability
        profit = trade3Bid/trade2Ask

    print("Current profitability x" + str(profit))

    profitAtStart = False

    if profit >= 1.003 and btcTrade != "":                              #change back to 1.003
        try:
            startingTicker = client.get_symbol_ticker(symbol=trade2)
            time.sleep(0.05)
            startingPrice = Decimal(startingTicker.get("price")) * count
            startingPrice = math.ceil(startingPrice * btcRound)/btcRound
            print(startingPrice)
            print(btcTrade)
        except:
            print("Error when getting starting Price")
            pauseProgram()

        try:
            orderForStart = client.create_test_order(
    symbol= btcTrade,
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity= startingPrice)                                        #fixed
            time.sleep(0.05)
        except:
            print("Error on trading in BTC")
            pauseProgram()
        print("Traded in BTC to start trade cycles")
        profitAtStart = True
   
    while profit >= 1.003:

        try:
            #cycle starts with order 2 for REASONS
            order2 = client.create_test_order(
    symbol= trade2,
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity= count)
        except:
            print("Error for order2")
            pauseProgram()

        print("Buying " + str(count) + " in " + trade2)
        time.sleep(0.1)

        try:
            order3 = client.create_test_order(
    symbol= trade3,
    side=Client.SIDE_SELL,
    type=Client.ORDER_TYPE_MARKET,
    quantity= count)                                  #test for sell
        except:
            print("Error for order3")
            pauseProgram()

        print("Selling " + str(count) + " in " + trade3)
        time.sleep(0.1)

        try:
            coinPriceTicker = client.get_symbol_ticker(symbol=trade2)
            coinPrice = Decimal(coinPriceTicker.get("price")) * count
            coinPrice = math.ceil(coinPrice * btcRound)/btcRound
        except:
            print("Error when getting coinPrice for order1")
            pauseProgram()
        time.sleep(0.1)

        #Buy or sell depending on the exchanged
        if trade == "bnb2eth" or trade == "bnb2btc" or trade == "ETHBTC":
            #BUY
            try:
                order1 = client.create_test_order(
    symbol= trade1,
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity= coinPrice) # quantity based on price and count
                time.sleep(0.1)
            except:
                print("Error for order1, section 1")
                pauseProgram()

            print("Buying in " + trade1)
        else:
            #SELL
            #try:
            order1 = client.create_test_order(
    symbol= trade1,
    side=Client.SIDE_SELL,
    type=Client.ORDER_TYPE_MARKET,
    quantity= coinPrice)
            time.sleep(0.1)
            #except:
            #    print("Error for order1, section 2")
            #    pauseProgram()

            print("Buying in " + trade1)

    #Check current profitability, if this has changed to no longer be profitable, a new search will begin
        if (trade == "bnb2btc") or (trade == "eth2btc"):
            try:
                #Get orderbooks and btc prices
                trade2book = client.get_orderbook_ticker(symbol=trade2)
                time.sleep(0.1)
                trade3book = client.get_orderbook_ticker(symbol=trade3)
                time.sleep(0.1)
                trade2proBook = client.get_symbol_ticker(symbol=trade2pro)
                time.sleep(0.1)
            except:
                print("Error for getting orderbooks for profit in cycle, section 1")
                pauseProgram()

            #Get btc conversion price
            trade2proPrice = Decimal(trade2proBook.get("price"))
        
            #Get bid and ask prices all in BTC
            trade2Ask = Decimal(trade2book.get("askPrice")) * trade2proPrice
            trade3Bid = Decimal(trade3book.get("bidPrice"))

            #bid/ask to find profitability
            profit = trade3Bid/trade2Ask
        elif (trade == "btc2eth") or (trade == "btc2bnb"):
            try:
                #Get orderbooks and btc prices
                trade2book = client.get_orderbook_ticker(symbol=trade2)
                time.sleep(0.1)
                trade3book = client.get_orderbook_ticker(symbol=trade3)
                time.sleep(0.1)
                trade3proBook = client.get_symbol_ticker(symbol=trade3pro)
                time.sleep(0.1)
            except:
                print("Error for getting orderbooks for profit in cycle, section 2")
                pauseProgram()

            #Get btc conversion price
            trade3proPrice = Decimal(trade3proBook.get("price"))

            #Get bid and ask prices all in BTC
            trade2Ask = Decimal(trade2book.get("askPrice"))
            trade3Bid = Decimal(trade3book.get("bidPrice")) * trade3proPrice

            #bid/ask to find profitability
            profit = trade3Bid/trade2Ask
        else:
            try:
                #Get orderbooks and btc prices
                trade2book = client.get_orderbook_ticker(symbol=trade2)
                time.sleep(0.1)
                trade3book = client.get_orderbook_ticker(symbol=trade3)
                time.sleep(0.1)
                trade2proBook = client.get_symbol_ticker(symbol=trade2pro)
                time.sleep(0.1)
                trade3proBook = client.get_symbol_ticker(symbol=trade3pro)
                time.sleep(0.1)
            except:
                print("Error for getting orderbooks for profit in cycle, section 3")
                pauseProgram()

            #Get btc conversion price
            trade2proPrice = Decimal(trade2proBook.get("price"))
            trade3proPrice = Decimal(trade3proBook.get("price"))
        
            #Get bid and ask prices all in BTC
            trade2Ask = Decimal(trade2book.get("askPrice")) * trade2proPrice
            trade3Bid = Decimal(trade3book.get("bidPrice")) * trade3proPrice

            #bid/ask to find profitability
            profit = trade3Bid/trade2Ask
        print("Current profitability x" + str(profit))
        
        #stop on user input
        if m.kbhit():
            break;

    #start next search, should probably make it apart of an if statement
    print("Profitability has crossed below threshold, starting new search...")
    if profitAtStart == True:
        try:
            startingTicker = client.get_symbol_ticker(symbol=trade2)
            startingPrice = Decimal(coinPriceTicker.get("price")) * count
            time.sleep(0.1)
        except:
            print("Error when getting ending Price")
            pauseProgram()

        try:
            #trade coin back to btc
            orderForEnd = client.create_test_order(
            symbol= btcTrade,
            side=Client.SIDE_SELL,
            type=Client.ORDER_TYPE_MARKET,
            quantity= startingPrice)                        #change to amount for coin
            time.sleep(0.1)
        except:
            print("Error on trading out for BTC")
            pauseProgram()
    #stop on user input
    if m.kbhit():
        pauseProgram()
    startSearch()

#user starts bot
input = input("Press the <ENTER> key to start")
print("Starting search")
startSearch()


#Current things to do: bug testing -> add more coins that can exchange for BTC, BNB, and ETH
# market (must be able to fetch prices from other orders)

#client.order_market_buy(
#    symbol='BNBBTC',
#    quantity= count)

#search function debugged

#major bug in startTrades fixed:
#   order1 quantity
#   orderForStart quantity
#       issue for both was that quantity has too many decimal places than binance uses
#       btc only trades down to a place of .001 for eth and 0.01 for bnb
#fix: rounded up numbers to minimum place that binance allows
#   note that this may cause an issue with coin amounts as extra will be made