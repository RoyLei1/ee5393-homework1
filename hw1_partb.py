import random
import statistics

# Number of trials (100,000 gives a very stable estimate for mean and variance)
trials = 100000

# Lists to store the final quantities of X1, X2, and X3 after 7 steps
res_x1, res_x2, res_x3 = [], [], []

for _ in range(trials):
    # Initial state S = [9, 8, 7]
    x1, x2, x3 = 9, 8, 7
    
    # Forcibly execute exactly 7 reaction steps
    for _ in range(7):
        # 1. Calculate the propensity (unnormalized weight) for each reaction
        w1 = 0.5 * x1 * (x1 - 1) * x2
        w2 = x1 * x3 * (x3 - 1)
        w3 = 3 * x2 * x3
        
        total_w = w1 + w2 + w3
        
        # Safety check: if total_w is 0, no reactions can occur
        if total_w == 0:
            break
            
        # 2. Roulette wheel selection
        rand_val = random.uniform(0, total_w)
        
        if rand_val < w1:
            # R1 fires: consumes 2 X1, 1 X2; produces 4 X3
            x1, x2, x3 = x1 - 2, x2 - 1, x3 + 4
        elif rand_val < w1 + w2:
            # R2 fires: consumes 1 X1, 2 X3; produces 3 X2
            x1, x2, x3 = x1 - 1, x2 + 3, x3 - 2
        else:
            # R3 fires: consumes 1 X2, 1 X3; produces 2 X1
            x1, x2, x3 = x1 + 2, x2 - 1, x3 - 1
            
    # Record the final state after 7 steps
    res_x1.append(x1)
    res_x2.append(x2)
    res_x3.append(x3)

# Print the calculated mean and POPULATION variance
print("Simulation completed for 100,000 trials (7 steps each).")
print("-" * 50)
print(f"X1 -> Mean: {statistics.mean(res_x1):.4f}, Variance: {statistics.pvariance(res_x1):.4f}")
print(f"X2 -> Mean: {statistics.mean(res_x2):.4f}, Variance: {statistics.pvariance(res_x2):.4f}")
print(f"X3 -> Mean: {statistics.mean(res_x3):.4f}, Variance: {statistics.pvariance(res_x3):.4f}")
