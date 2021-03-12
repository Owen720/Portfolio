import random

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K',] * 16
sum = int(0)

player_card = []
dealer_card = []
split_record = []
record = []
cost = 1000


def card_name():
    rd = random.choice(cards)
    if rd == "A":
        cards.remove("A")
        return rd
    elif rd == "2":
        cards.remove("2")
        return rd
    elif rd == "3":
        cards.remove("3")
        return rd
    elif rd == "4":
        cards.remove("4")
        return rd
    elif rd == "5":
        cards.remove("5")
        return rd
    elif rd == "6":
        cards.remove("6")
        return rd
    elif rd == "7":
        cards.remove("7")
        return rd
    elif rd == "8":
        cards.remove("8")
        return rd
    elif rd == "9":
        cards.remove("9")
        return rd
    elif rd == "10":
        cards.remove("10")
        return rd
    elif rd == "J":
        cards.remove("J")
        return rd
    elif rd == "Q":
        cards.remove("Q")
        return rd
    elif rd == "K":
        cards.remove("K")
        return rd
    
def card_point(n, c):
    if n == 'A':
        c += 1
        return c
    elif n == '2':
        c += 2
        return c
    elif n == '3':
        c += 3
        return c
    elif n == '4':
        c += 4
        return c
    elif n == '5':
        c += 5
        return c
    elif n == '6':
        c += 6
        return c
    elif n == '7':
        c += 7
        return c
    elif n == '8':
        c += 8
        return c
    elif n == '9':
        c += 9
        return c
    elif n == '10':
        c += 10
        return c
    elif n == 'J':
        c += 10
        return c
    elif n == 'Q':
        c += 10
        return c
    elif n == 'K':
        c += 10
        return c

def checkMoney(money):
    m = int(money)
    if m > 0:
        return True
    else:
        return False

def blackJack(card):
    if card == 21:
      return True
    else:
      return False

def win(m):
    m = m
    return m

def lose(m):
    m = m
    return m

def doubleWin(m):
    m = m * 2
    return m

def doubleLose(m):
    m = m * 2
    return m  

def tie(m):
    m = 0
    return m

def calculate(c, sum):
    cal_point = int(0)
    for i in c:
        point = card_point(i, cal_point)
        sum += point
        point -= point
    return sum

def checkAce(n):
  if "A" in n:
    ace = True
    return ace
  else:
    ace = False
    return ace

def stand(player_card, dealer_card):
    player_total = calculate(player_card, sum)
    
    print("\n----------------------------")
    print("\nPlayer:")
    print(*player_card)
    if checkAce(player_card) == True:
        if player_total <= 21 and player_total + 10 <= 21:
            print("Total: ", player_total, "/", player_total + 10, "\n")
        elif player_total < 21 and player_total + 10 > 21:
            print("Total: ", player_total, "\n")
    else:
        print("Total: ", player_total, "\n")

    card = card_name()
    dealer_card.append(card)
    dealer_total = calculate(dealer_card, sum)

    if checkAce(dealer_card) == True and blackJack(dealer_total + 10) == True:
        print("Dealer:")
        print(*dealer_card)
        print("Dealer BlackJack")
        player_card.clear()
        dealer_card.clear()
        return "Lose"

    elif checkAce(dealer_card) == True and blackJack(dealer_total + 10) == False and dealer_total + 10 >= 17:
        print("Dealer:")
        print(*dealer_card)
        
    else:
        while dealer_total < 17:
            if len(dealer_card) < 5:
                card = card_name()
                dealer_card.append(card)
                dealer_total = calculate(dealer_card, sum)
            else:
                break

        print("Dealer:")
        print(*dealer_card)

    if len(dealer_card) == 5 and dealer_total <= 21:
        print("Total: ", dealer_total)
        return "Lose"
        
    if checkAce(dealer_card) == True:
        if dealer_total + 10 < 21:
            print("Total: ", dealer_total + 10)
        elif dealer_total + 10 > 21 and dealer_total <= 21:
            print("Total: ", dealer_total)
        elif dealer_total + 10 > 21 and dealer_total > 21:
            print("Total: ", dealer_total)
    else:
        print("Total: ", dealer_total)

    if checkAce(dealer_card) == True:
        if checkAce(player_card) == True:
            dealer_ace = dealer_total + 10
            player_ace = player_total + 10
            if dealer_ace > 21 and dealer_total > 21:
                print("\nDealer Over")
                return "Win"
            elif player_ace <= 21:
                if player_ace > dealer_ace:
                    return "Win"
                elif player_ace == dealer_ace:
                    return "Tie"
                elif player_ace < dealer_ace :
                    return "Lose" 
            elif player_ace > 21:
                if player_total > dealer_ace:
                    return "Win"
                elif player_total == dealer_ace:
                    return "Tie"
                elif player_total < dealer_ace :
                    return "Lose" 

        elif checkAce(player_card) == False :
            dealer_ace = dealer_total + 10
            if dealer_ace > 21 and dealer_total > 21:
                print("\nDealer Over")
                return "Win"
            elif player_total > dealer_ace:
                return "Win"
            elif player_total == dealer_ace:
                return "Tie"
            elif player_total < dealer_ace or player_total < dealer_total:
                return "Lose"
    
    elif checkAce(dealer_card) == False:
        if checkAce(player_card) == True:
            player_ace = player_total + 10
            if dealer_total > 21:
                print("\nDealer Over")
                return "Win"
            elif player_ace <= 21:
                if player_ace > dealer_total or player_total > dealer_total:
                    return "Win"
                elif player_total <= dealer_total:
                    if player_ace > dealer_total:
                        return "Win"
                    elif player_ace == dealer_total:
                        return "Tie"
                    elif player_ace < dealer_total:
                        return "Lose"
            elif player_ace > 21:
                if player_total > dealer_total:
                    return "Win"
                elif player_total == dealer_total:
                    return "Tie"
                elif player_total < dealer_total:
                    return "Lose"

        elif checkAce(player_card) == False:
            if dealer_total > 21:
                print("\nDealer Over")
                return "Win"
            elif player_total > dealer_total:
                return "Win"
            elif player_total == dealer_total:
                return "Tie"
            elif player_total < dealer_total:
                return "Lose"

    player_card.clear()
    dealer_card.clear()

def hit(player_card,dealer_card):
    card = card_name()
    player_card.append(card)

    player_total = calculate(player_card, sum)
    print("\n----------------------------")
    print("\nPlayer:")
    print(*player_card)
    if checkAce(player_card) == True:
        print("Total: ", player_total, "/", player_total + 10, "\n")
    else:
        print("Total: ", player_total, "\n")

    dealer_total = calculate(dealer_card, sum)
    print("Dealer:")
    print(*dealer_card)
    if checkAce(dealer_card) == True:
        print("Total: ", dealer_total, "/", dealer_total + 10, "\n")
    else:
        print("Total: ", dealer_total, "\n")

    if player_total < 21:
        choose = int(input("1.Stand   2.Hit\n"))
        if choose == 1:
            result = stand(player_card, dealer_card)
            return result
        elif choose == 2:
            result = hit(player_card, dealer_card)
            return result

    elif player_total == 21:
        result = stand(player_card, dealer_card)
        return result

    elif player_total > 21:
        print("Player Over")
        return "Lose"

    player_card.clear()
    dealer_card.clear()
    
def doubleDown(player_card,dealer_card):
    card = card_name()
    player_card.append(card)

    player_total = calculate(player_card, sum)
    print("\n----------------------------")
    print("\nPlayer:")
    print(*player_card)
    if checkAce(player_card) == True:
        print("Total: ", player_total, "/", player_total + 10, "\n")
    else:
        print("Total: ", player_total, "\n")

    dealer_total = calculate(dealer_card, sum)
    print("Dealer:")
    print(*dealer_card)
    if checkAce(dealer_card) == True:
        print("Total: ", dealer_total, "/", dealer_total + 10, "\n")
    else:
        print("Total: ", dealer_total, "\n")
    
    if player_total > 21:
        print("Over")
        return "Lose"
    else:
        result = stand(player_card, dealer_card)
        return result

def split_choose(money, player_total):
    choose1 = int(input("Stand   Hit   Double Down\n"))
    if choose1 == 1:
        return money, player_total

    elif choose1 == 2:
        player_total = split_hit(player_card)
        return money, player_total
        
    elif choose1 == 3:
        money *= 2
        player_total = split_double(player_card)
        return money, player_total

def split(player_card,dealer_card, money):
    player_card2 = []
    money2 = money

    print("\n----------------------------")
    for i in range(1):
        player_card2.append(player_card[1])
        player_card.remove(player_card[1])

    card = card_name()
    player_card.append(card)
    card = card_name()
    player_card2.append(card)

    player_total = calculate(player_card, sum)
    player_total2 = calculate(player_card2, sum)

    print("\nPlayer:")
    print(*player_card)
    if checkAce(player_card) == True:
        if player_total <= 21 and player_total + 10 <= 21:
            print("Total: ", player_total, "/", player_total + 10)
        elif player_total < 21 and player_total + 10 > 21:
            print("Total: ", player_total)
    else:
        print("Total: ", player_total)

    print(*player_card2)
    if checkAce(player_card2) == True:
        if player_total2 <= 21 and player_total2 + 10 <= 21:
            print("Total: ", player_total2, "/", player_total2 + 10, "\n")
        elif player_total2 < 21 and player_total2 + 10 > 21:
            print("Total: ", player_total2, "\n")
    else:
        print("Total: ", player_total2, "\n")

    dealer_total = calculate(dealer_card, sum)
    print("Dealer:")
    print(*dealer_card)
    if checkAce(dealer_card) == True:
        print("Total: ", dealer_total, "/", dealer_total + 10, "\n")
    else:
        print("Total: ", dealer_total, "\n")

    print("Hand 1")
    money, player_total = split_choose(money, player_total)
    print("\n----------------------------")

    print("Hand 2")
    money2, player_total2 = split_choose(money, player_total2)
    print("\n----------------------------")

    card = card_name()
    dealer_card.append(card)
    dealer_total = calculate(dealer_card, sum)

    print("\nPlayer:")
    print(*player_card)
    if checkAce(player_card) == True:
        if player_total <= 21 and player_total + 10 <= 21:
            print("Total: ", player_total, "/", player_total + 10, "\n")
        elif player_total < 21 and player_total + 10 > 21:
            print("Total: ", player_total, "\n")
    else:
        print("Total: ", player_total, "\n")

    print(*player_card2)
    if checkAce(player_card2) == True:
        if player_total2 <= 21 and player_total2 + 10 <= 21:
            print("Total: ", player_total2, "/", player_total2 + 10, "\n")
        elif player_total2 < 21 and player_total2 + 10 > 21:
            print("Total: ", player_total2, "\n")
    else:
        print("Total: ", player_total2, "\n")

    if checkAce(dealer_card) == True and blackJack(dealer_total + 10) == True:
        print("\nDealer:")
        print(*dealer_card)
        print("Dealer BlackJack")
        money = lose(money)
        print("\nResult:", "-%d" % money)
        return -money

    elif checkAce(dealer_card) == True and blackJack(dealer_total + 10) == False and dealer_total + 10 >= 17:
        print("Dealer:")
        print(*dealer_card)
        
    else:
        while dealer_total < 17:
            card = card_name()
            dealer_card.append(card)
            dealer_total = calculate(dealer_card, sum)
        print("Dealer:")
        print(*dealer_card)

    if checkAce(dealer_card) == True:
        if dealer_total + 10 < 21:
            print("Total: ", dealer_total + 10)
        elif dealer_total + 10 > 21 and dealer_total <= 21:
            print("Total: ", dealer_total)
        elif dealer_total + 10 > 21 and dealer_total > 21:
            print("Total: ", dealer_total)
    else:
        print("Total: ", dealer_total)


    result = deal(player_card, player_total, dealer_card, dealer_total, money)
    split_record.append(result)
    print("\n")
    result = deal(player_card2, player_total2, dealer_card, dealer_total, money2)
    split_record.append(result)


    if split_record[0] == "Win":
        if split_record[1] == "Win":
            return "Win2"
        elif split_record[1] == "Lose":
            return "Tie"
        elif split_record[1] == "Tie":
            return "Win1"

    if split_record[0] == "Tie":
        if split_record[1] == "Win":
            return "Win1"
        elif split_record[1] == "Lose":
            return "Lose1"
        elif split_record[1] == "Tie":
            return "Tie"

    if split_record[0] == "Lose":
        if split_record[1] == "Win":
            return "Tie"
        elif split_record[1] == "Lose":
            return "Lose2"
        elif split_record[1] == "Tie":
            return "Lose1"
    
    player_card.clear()
    player_card2.clear()
    dealer_card.clear()

def split_hit(player_card):
    card = card_name()
    player_card.append(card)

    player_total = calculate(player_card, sum)
    print("\n----------------------------")
    print("\nPlayer:")
    print(*player_card)
    if checkAce(player_card) == True:
        print("Total: ", player_total, "/", player_total + 10, "\n")
    else:
        print("Total: ", player_total, "\n")

    if player_total < 21:
        choose = int(input("1.Stand   2.Hit\n"))
        if choose == 1:
            return player_total
        elif choose == 2:
            player_total = split_hit(player_card)

    elif player_total == 21:
        return player_total

    elif player_total > 21:
        print("Player Over")
        return player_total

def split_double(player_card):
    card = card_name()
    player_card.append(card)

    player_total = calculate(player_card, sum)
    print("\n----------------------------")
    print("\nPlayer:")
    print(*player_card)
    if checkAce(player_card) == True:
        print("Total: ", player_total, "/", player_total + 10, "\n")
    else:
        print("Total: ", player_total, "\n")
    
    if player_total > 21:
        print("Player Over")
        return player_total
    else:
        return player_total

def deal(player_card, player_total, dealer_card, dealer_total, money):

    if checkAce(dealer_card) == True:
        if checkAce(player_card) == True:
            dealer_ace = dealer_total + 10
            player_ace = player_total + 10
            if dealer_ace > 21 and dealer_total > 21:
                print("\nDealer Over")
                money = win(money)
                print("Result:", "+%d" % money)
                return "Win"
            elif player_ace <= 21:
                if player_ace > dealer_ace:
                    money = win(money)
                    print("Result:", "+%d" % money)
                    return "Win"
                elif player_ace == dealer_ace:
                    money = tie(money)
                    print("Result:", money)
                    return "Tie"
                elif player_ace < dealer_ace :
                    money = lose(money)
                    print("Result:", "-%d" % money)
                    return "Lose"
            elif player_ace > 21:
                if player_total > dealer_ace:
                    money = win(money)
                    print("Result:", "+%d" % money)
                    return "Win"
                elif player_total == dealer_ace:
                    money = tie(money)
                    print("Result:", money)
                    return "Tie"
                elif player_total < dealer_ace :
                    money = lose(money)
                    print("Result:", "-%d" % money)
                    return "Lose"

        elif checkAce(player_card) == False :
            dealer_ace = dealer_total + 10
            if dealer_ace > 21 and dealer_total > 21:
                print("Dealer Over")
                money = win(money)
                print("Result:", "+%d" % money)
                return "Win"
            elif player_total > dealer_ace:
                money = win(money)
                print("Result:", "+%d" % money)
                return "Win"
            elif player_total == dealer_ace:
                money = tie(money)
                print("Result:", money)
                return "Tie"
            elif player_total < dealer_ace or player_total < dealer_total:
                money = lose(money)
                print("Result:", "-%d" % money)
                return "Lose"
    
    elif checkAce(dealer_card) == False:
        if checkAce(player_card) == True:
            player_ace = player_total + 10
            if dealer_total > 21:
                print("Dealer Over")
                money = win(money)
                print("\nResult:", "+%d" % money)
                return "Win"
                
            elif player_ace <= 21:
                if player_ace > dealer_total or player_total > dealer_total:
                    money = win(money)
                    print("\nResult:", "+%d" % money)
                    return "Win"
                elif player_total <= dealer_total:
                    if player_ace > dealer_total:
                        money = win(money)
                        print("\nResult:", "+%d" % money)
                        return "Win"
                    elif player_ace == dealer_total:
                        money = tie(money)
                        print("\nResult:", money)
                        return "Tie"
                    elif player_ace < dealer_total:
                        money = lose(money)
                        print("\nResult:", "-%d" % money)
                        return "Lose"

            elif player_ace > 21:
                if player_total > dealer_total:
                    money = win(money)
                    print("\nResult:", "+%d" % money)
                    return "Win"
                elif player_total == dealer_total:
                    money = tie(money)
                    print("\nResult:", money)
                    return "Tie"
                elif player_total < dealer_total:
                    money = lose(money)
                    print("\nResult:", "-%d" % money)
                    return "Lose"

        elif checkAce(player_card) == False:
            if dealer_total > 21:
                print("\nDealer Over")
                money = win(money)
                print("\nResult:", "+%d" % money)
                return "Win"
            elif player_total > dealer_total:
                money = win(money)
                print("\nResult:", "+%d" % money)
                return "Win"
            elif player_total == dealer_total:
                money = tie(money)
                print("\nResult:", money)
                return "Tie"
            elif player_total < dealer_total:
                money = lose(money)
                print("\nResult:", "-%d" % money)
                return "Lose"

    player_card.clear()
    dealer_card.clear()

def menu():
    print("1.Stand   2.Hit   3.Double Down   4.Split\n")

def main(cost):
        if len(cards) <= 13:
            print("No Card")
        else:
            print("Cards:", len(cards))

        print("Cost:", "$%d" % cost)
        money = int(input("Bet: "))

        for i in range(2):
            card = card_name()
            player_card.append(card)

        card = card_name()
        dealer_card.append(card)

        player_total = calculate(player_card, sum)
        print("\nPlayer:")
        print(*player_card)

        if checkAce(player_card) == True and blackJack(player_total + 10) == True:
            print("Player BlackJack!")

            dealer_total = calculate(dealer_card, sum)
            print("\nDealer:")
            print(*dealer_card)
            if checkAce(dealer_card) == True:
                print("Total: ", dealer_total, "/", dealer_total + 10)
            else:
                print("Total: ", dealer_total)

            money = win(money)
            money *= 1.5
            cost += money
            print("\nResult:", "+%d" % money)
            record.append("Win")
            player_card.clear()
            dealer_card.clear()
            return cost
            
        elif blackJack(player_card) == False:
            if checkAce(player_card) == True:
                print("Total: ", player_total, "/", player_total + 10, "\n")
            elif checkAce(player_card) == False:
                print("Total: ", player_total, "\n")

        dealer_total = calculate(dealer_card, sum)
        print("\nDealer:")
        print(*dealer_card)
        if checkAce(dealer_card) == True:
            print("Total: ", dealer_total, "/", dealer_total + 10, "\n")
        else:
            print("Total: ", dealer_total, "\n")

        loop = True

        while loop:
            menu()
            choose = int(input("Enter Your Choose: "))

            if choose == 1:
                loop = False
                result = stand(player_card, dealer_card)
                if result == "Win":
                    money = win(money)
                    print("\nResult:", "+$%d" % money)
                    record.append("Win")
                    cost += money
                    print("Record:", '[%s]' % ', '.join(map(str, record)))
                    player_card.clear()
                    dealer_card.clear()
                    return cost
                elif result == "Lose":
                    money = lose(money)
                    print("\nResult:", "-$%d" % money)
                    record.append("Lose")
                    cost -= money
                    print("Record:", '[%s]' % ', '.join(map(str, record)))
                    player_card.clear()
                    dealer_card.clear()
                    return cost
                elif result == "Tie":
                    money = tie(money)
                    print("\nResult:", money)
                    record.append("Tie")
                    cost += 0
                    print("Record:", '[%s]' % ', '.join(map(str, record)))
                    player_card.clear()
                    dealer_card.clear()
                    return cost

            elif choose == 2:
                loop = False
                result = hit(player_card, dealer_card)
                if result == "Win":
                    money = win(money)
                    print("\nResult:", "+%d" % money)
                    record.append("Win")
                    cost += money
                    print("Record:", '[%s]' % ', '.join(map(str, record)))
                    player_card.clear()
                    dealer_card.clear()
                    return cost
                elif result == "Lose":
                    money = lose(money)
                    print("\nResult:", "-%d" % money)
                    record.append("Lose")
                    cost -= money
                    print("Record:", '[%s]' % ', '.join(map(str, record)))
                    player_card.clear()
                    dealer_card.clear()
                    return cost
                elif result == "Tie":
                    money = tie(money)
                    print("\nResult:", money)
                    record.append("Tie")
                    cost += 0
                    print("Record:", '[%s]' % ', '.join(map(str, record)))
                    player_card.clear()
                    dealer_card.clear()
                    return cost
                
            elif choose == 3:
                loop = False
                result = doubleDown(player_card,dealer_card)
                if result == "Win":
                    money = doubleWin(money)
                    print("\nResult:", "+%d" % money)
                    record.append("Win")
                    record.append("Win")
                    cost += money
                    print("Record:", '[%s]' % ', '.join(map(str, record)))
                    player_card.clear()
                    dealer_card.clear()
                    return cost
                elif result == "Lose":
                    money = doubleLose(money)
                    print("\nResult:", "-%d" % money)
                    record.append("Lose")
                    record.append("Lose")
                    cost -= money
                    print("Record:", '[%s]' % ', '.join(map(str, record)))
                    player_card.clear()
                    dealer_card.clear()
                    return cost
                elif result == "Tie":
                    money = tie(money)
                    print("\nResult:", money)
                    record.append("Tie")
                    cost += 0
                    print("Record:", '[%s]' % ', '.join(map(str, record)))
                    player_card.clear()
                    dealer_card.clear()
                    return cost

            elif choose == 4:
                if player_card[0] == player_card[1]:
                    loop = False
                    result = split(player_card,dealer_card, money)
                    if result == "Win2":
                        money = doubleWin(money)
                        print("\nTotal Result:", "+%d" % money)
                        record.append("Win")
                        record.append("Win")
                        cost += money
                        print("Record:", '[%s]' % ', '.join(map(str, record)))
                        player_card.clear()
                        dealer_card.clear()
                        return cost
                    
                    elif result == "Win1":
                        money = win(money)
                        print("\nTotal Result:", "+%d" % money)
                        record.append("Win")
                        cost += money
                        print("Record:", '[%s]' % ', '.join(map(str, record)))
                        player_card.clear()
                        dealer_card.clear()
                        return cost

                    elif result == "Tie":
                        money = tie(money)
                        print("\nTotal Result:", money)
                        record.append("Tie")
                        cost += 0
                        print("Record:", '[%s]' % ', '.join(map(str, record)))
                        player_card.clear()
                        dealer_card.clear()
                        return cost

                    elif result == "Lose1":
                        money = lose(money)
                        print("\nTotal Result:", "-%d" % money)
                        record.append("Lose")
                        cost -= money
                        print("Record:", '[%s]' % ', '.join(map(str, record)))
                        player_card.clear()
                        dealer_card.clear()
                        return cost
                    
                    elif result == "Lose2":
                        money = doubleLose(money)
                        print("\nTotal Result:", "-%d" % money)
                        record.append("Lose")
                        record.append("Lose")
                        cost -= money
                        print("Record:", '[%s]' % ', '.join(map(str, record)))
                        player_card.clear()
                        dealer_card.clear()
                        return cost
                elif player_card[0] != player_card[1]:
                    print("\nPlease Choose Again\n")
                    loop = True


        print("Record:", '[%s]' % ', '.join(map(str, record)))
        player_card.clear()
        dealer_card.clear()

new_cost = cost
for i in range(100):
    if len(cards) > 52 and new_cost > 0:
        if new_cost > 0:
            new_cost = main(new_cost)
            win_num = record.count("Win")
            win_rate = round((win_num / len(record)) * 100, 2)
            str_win_rate = str(win_rate)
            print("Win Rate:", str_win_rate, end = '%')
            print("\n-------------------------------------------------------\n")
        else:
            print("No Money")
    else:
        print("No Card")
