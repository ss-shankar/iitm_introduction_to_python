"""
You have nn gold coins with you. You wish to divide this among three of your
friends under the following conditions:
(1) All three of them should get a non-zero share.
(2) No two of them should get the same number of coins.
(3) You should not have any coins with you at the end of this sharing process.
The input has four lines. The first line contains the number of coins with you.
The next three lines will have the share given to your three friends.
All inputs shall be non-negative integers. If the division satisfies these
conditions, then print the string FAIR. If not, print UNFAIR.
"""

total_gold = int(input())
gold_1 = int(input())
gold_2 = int(input())
gold_3 = int(input())

if total_gold != gold_1 + gold_2 + gold_3:
    print("UNFAIR")
elif gold_1 == gold_2 or gold_1 == gold_3 or gold_2 == gold_3:
    print("UNFAIR")
elif gold_1 == 0 or gold_2 == 0 or gold_3 == 0:
    print("UNFAIR")
else:
    print("FAIR")
