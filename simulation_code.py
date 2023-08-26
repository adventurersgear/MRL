
import time

def run_simulation(steps=100, delay=0.5):
    # Initialize system state
    zeros = ["0"]
    undefineds = ["U"]
    
    # Store vectors for topology analysis
    zero_vectors = []
    u_vectors = []
    singularity_traverse = []
    
    for step in range(steps):
        # Print the current state
        state_str = "".join(zeros) + "|" + "".join(undefineds)
        print(f"Step {step + 1}: {state_str}")
        
        # Update vectors for each 0 and U
        zero_vectors.append([1 if i == j else 0 for i in range(len(zeros))])
        u_vectors.append([1 if i == j else 0 for i in range(len(undefineds))])
        
        # Update the singularity traverse
        singularity_traverse.append((zeros[-1], undefineds[0]))
        
        # Update the system state
        # Add 0s
        zeros.append("0")
        
        # Add Us: growing by 1 + n(U's)
        for _ in range(1 + len(undefineds)):
            undefineds.append("U")
        
        # Delay for visualization (user can adjust this for faster/slower simulation)
        time.sleep(delay)

    # Store vectors and singularity traverse for further analysis
    return zero_vectors, u_vectors, singularity_traverse

if __name__ == "__main__":
    zero_vectors, u_vectors, singularity_traverse = run_simulation()
