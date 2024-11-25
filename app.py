import matplotlib.pyplot as plt
import numpy as np
import random
import streamlit as st

# Define the pick and probability functions
def pick(n, d):
    draws = [random.randint(0, d - 1) for _ in range(n)]
    return len(set(draws))

def probability(unique, total, d, samplesize):
    count = 0
    for _ in range(samplesize):
        if pick(total, d) == unique:
            count += 1
    return count / samplesize

def compute_probabilities(unique, total, upper):
    d_values = range(unique, upper, max(1, upper // 100))
    probabilities = [probability(unique, total, d, 5000) for d in d_values]
    return d_values, probabilities

# Streamlit App
def main():
    st.title("Nanobody Library Diversity Probability Simulator")
    st.write("Simulate and visualize the diversity of your nanobody library")
    st.write("To get started you need to isolate and sequence individual clones from your library")

    # Streamlit input widgets
    total = st.number_input("Enter the total number of clones you sequenced:", min_value=1, value=20, step=1)
    unique = st.number_input("Enter the number of unique clones you have after removing all duplicates:", min_value=1, value=15, step=1)
    upper = st.number_input("Enter the upper limit of diversity range:", min_value=unique, value=200, step=1)

    if st.button("Calculate"):
        # Calculate probabilities
        d_values, probabilities = compute_probabilities(unique, total, upper)

        # Determine the most probable diversity value
        max_prob_index = np.argmax(probabilities)
        most_probable_diversity = d_values[max_prob_index]
        highest_probability = probabilities[max_prob_index]

        st.write(f"### Most probable diversity value: {most_probable_diversity}")
        st.write(f"### Probability: {highest_probability:.4f}")

        # Plotting
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(d_values, probabilities, marker='o', linestyle='-')
        ax.set_xlabel('Diversity')
        ax.set_ylabel('Probability')
        ax.set_title('Probability Plot')
        ax.axvline(x=most_probable_diversity, color='red', linestyle='--',
                   label=f'Most Probable ({most_probable_diversity}) with Probability {highest_probability:.4f}')
        ax.legend()
        ax.grid(True)

        # Display plot in Streamlit
        st.pyplot(fig)

if __name__ == "__main__":
    main()
