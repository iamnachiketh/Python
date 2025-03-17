import random

def gambler_simulation(stake, goal, simulations):
    wins = 0
    total_bets = 0
    
    for _ in range(simulations):
        cash = stake
        bets = 0
        
        while 0 < cash < goal:
            bet = random.choice([-1, 1])
            cash += bet
            bets += 1
        
        total_bets += bets
        if cash == goal:
            wins += 1
    
    loss_percentage = 100 - (wins / simulations * 100)
    
    print(f"Wins: {wins}")
    print(f"Loss Percentage: {loss_percentage:.2f}%")
    print(f"Total Bets Made: {total_bets}")

stake, goal, simulations = map(int, input().split())

gambler_simulation(stake, goal, simulations)