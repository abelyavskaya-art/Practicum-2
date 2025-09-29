all_cost = int(input())
silver_watch = 96
gold_watch = 96 // 16
silver_cost = 48
gold_cost = (all_cost - (silver_watch * silver_cost)) // gold_watch
print(gold_cost)