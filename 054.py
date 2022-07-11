order = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
def cards(card):
    global order
    return order.index(card)
def same_suit(s):
    for i in range(1,len(s)):
        if s[i][1] != s[0][1]:
            return "0"
    return "1"
def del_suit(s):
    return [x[0] for x in s]
def flush(hand):
    for i in range(1,5):
        if hand[i] != order[order.index(hand[0])-i]:
            return "0"
    return hand[0]
def n_same(hand,n):
    global order
    c = [0]*len(order)
    for card in hand:
        c[order.index(card)] += 1
    result = ""
    for i in range(len(c)):
        if c[i]==n:
            result += order[i]
    if n==2:
        if result != "":
            return (2-len(result))*"0"+result
        return "00"
    else:
        if result != "":
            return result   
        return "0"
def compare_residue(res1,res2):
    global order
    for i in range(len(res1)):
        if order.index(res1[i]) > order.index(res2[i]):
            return 1
        else:
            return 0
def rank(hand, suit):
    residue = "".join(x for x in hand)
    used = ""
    s = n_same(hand, 4) + suit + flush(hand) + n_same(hand, 3) + n_same(hand, 2)
    #print("[4][flush][straight][3][2][2][5]")
    #print(s)
    if s[0] != "0": #if we would have same 4 cards then only highest card make winner
        residue = residue.replace(s[0], "")
    if s[2] != "0": #if we have same straight, we have to have equal cards(exept of suit)
        residue = residue = ""
    if s[3] != "0":
        residue = residue.replace(s[3], "")
    if s[4] != "0":
        residue = residue.replace(s[4], "")
    if s[5] != "0":
        residue = residue.replace(s[5], "")
    #[4][flush][straight][3][2][2] thats how s is formates. We can conclude combos from that
    if s[1] == "1" and s[2] == "A":
        return 10, used, residue #royal flush
    elif s[1] == "1" and s[2] != "0":
        return 9, used, residue #straight flush
    elif s[0] != "0":
        used = s[0]
        return 8, used, residue #4 of kind
    elif s[3] != "0" and s[5] != "0":
        used = s[3] + s[5]
        return 7, used, residue #full house
    elif s[1] == "1":
        return 6, used, residue #flush
    elif s[2] != "0":
        return 5, used, residue #straight
    elif s[3] != "0":
        used = s[3]
        return 4, used, residue #three of kind
    elif s[4] != "0":
        used = s[5]+s[4]
        return 3, used, residue #2 pairs
    elif s[5] != "0":
        used = s[5]
        return 2, used, residue # pair
    else:
        return 1, used, residue #no combo
def hands(s):
    s = s.split(" ")
    p1 = s[:5]
    p2 = s[5:]
    p1_suit = same_suit(p1)
    p1_hand = sorted(del_suit(p1), key=cards, reverse=True)
    p2_suit = same_suit(p2)
    p2_hand = sorted(del_suit(p2), key=cards, reverse=True)
    rank1, used1, residue1 = rank(p1_hand, p1_suit)
    rank2, used2, residue2 = rank(p2_hand, p2_suit)
    if rank1 > rank2:
        return 1
    elif rank1 == rank2: #they have same combo. We need to decide who is winner
        if rank1 == 9 or rank1 == 6 or rank1 == 5:
            if order.index(p1_hand[0]) > order.index(p2_hand[0]):
                return 1
        if rank1 == 8 or rank1 == 4 or rank1 == 2:
            if order.index(used1) > order.index(used2):
                return 1
            elif order.index(used1) == order.index(used2):
                return compare_residue(residue1, residue2)
        if rank1 == 7 or rank1 == 3:
            if order.index(used1[0]) > order.index(used2[0]):
                return 1
            elif order.index(used1[0]) == order.index(used2[0]):
                if order.index(used1[1]) > order.index(used2[1]):
                    return 1
                elif order.index(used1[1]) == order.index(used2[1]):
                    return compare_residue(residue1, residue2)
        if rank1 == 1:
            return compare_residue(residue1, residue2)
    return 0
s = 0
with open("p054_poker.txt", "r") as file:
    lines = file.read()
    lines = lines.split("\n")
    lines = lines[:-1]
    for line in lines:
        s += hands(line)
print(s)
