import matplotlib.pyplot as plt
import numpy as np
import random
import argparse

# Define the pick and probability functions
def pick(n, d):
    draws = [random.randint(0, d-1) for _ in range(n)]
    return len(set(draws))

def probability(unique, total, d, samplesize):
    count = 0
    for _ in range(samplesize):
        if pick(total, d) == unique:
            count += 1
    return count / samplesize

def compute_probabilities(unique, total, upper):
    d_values = range(unique, upper, max(1, upper // 100)) # change unique to 1 
    probabilities = [probability(unique, total, d, 5000) for d in d_values]
    return d_values, probabilities

def main():
    # Prompt user for inputs
    unique = int(input("Enter the number of unique clones: "))
    total = int(input("Enter the total number of clones: "))
    upper = int(input("Enter the upper limit of diversity range: "))

    # Calculate probabilities
    d_values, probabilities = compute_probabilities(unique, total, upper)
    
    # Determine the most probable diversity value
    max_prob_index = np.argmax(probabilities)
    most_probable_diversity = d_values[max_prob_index]
    highest_probability = probabilities[max_prob_index]
    
    print("The most probable diversity value is:", most_probable_diversity)
    print("With a probability of:", highest_probability)
    
    # Plotting the probabilities
    plt.figure(figsize=(10, 5))
    plt.plot(d_values, probabilities, marker='o', linestyle='-')
    plt.xlabel('Diversity')
    plt.ylabel('Probability')
    plt.title('Probability Plot')
    plt.axvline(x=most_probable_diversity, color='red', linestyle='--', label=f'Most Probable ({most_probable_diversity}) with Probability {highest_probability:.4f}')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
