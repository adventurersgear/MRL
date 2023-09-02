from math import factorial
import tkinter as tk

class HostClock:
    def __init__(self):
        self.time_step = 0
    def tick(self):
        self.time_step += 1

class MemorySpace:
    def __init__(self):
        self.nodes = []
        self.topology_map = {}
    def add_node(self, node):
        self.nodes.append(node)
        topology_engine.update_topology(node)
    

class BitStream:
    def __init__(self):
        self.bits = []
    def generate_bits(self, num_bits):
        import random
        self.bits = [random.randint(0, 1) for _ in range(num_bits)]

class Infuser:
    def __init__(self, bit_stream):
        self.bit_stream = bit_stream

    def generate_elements(self, pre_memory_staging):
        for bit in self.bit_stream.bits:
            # Create the default identity element for each bit
            identity_element = Node(0, host_clock)
            pre_memory_staging.staging_nodes.append(identity_element)


class PreMemorySpaceStaging:
    def __init__(self):
        self.staging_nodes = []
    def flush_to_memory_space(self, memory_space):
        for node in self.staging_nodes:
            node.temporal_vector = [0, host_clock.time_step]
            memory_space.add_node(node)
        self.staging_nodes = []

class TopologyEngine:    
    def __init__(self, memory_space):
        self.memory_space = memory_space
    def update_topology(self, new_node):
        if new_node.base == 0:
            for node in self.memory_space.nodes: 
                if node is not new_node:
                    if new_node not in node.topological_vector:
                        node.topological_vector.append(new_node)
                    if node not in new_node.topological_vector:
                        new_node.topological_vector.append(node)
            print(f"Debug: Topological Vector for Node {new_node}: {new_node.topological_vector}")


class ElementUpdateEngine:
    def __init__(self, memory_space, perception_function):
        self.memory_space = memory_space
        self.perception_function = perception_function

    def update_elements(self):
        for node in self.perception_function.elements_to_transform:
            node.base = 1
            node.temporal_vector[0] = node.temporal_vector[1]
            node.temporal_vector[1] = host_clock.time_step
        
        self.perception_function.elements_to_transform.clear()

class Node:
    def __init__(self, base, host_clock):
        self.base = base
        self.temporal_vector = [0, 0]  # Initialize with [0, 0]
        self.topological_vector = []
        self.host_clock = host_clock
        self.time_step = host_clock.time_step
    def __repr__(self) -> str:
        return f"Base-{self.base}, Temporal Vector-{self.temporal_vector}, Topological Vector Length-{len(self.topological_vector)}"

class PerceptionFunction:
    def __init__(self):
        self.elements_to_transform = []

    def perceive(self, memory_space):
        for node in memory_space.nodes:
            if node.base == 0:
                future_base = 1  # As per the current rule
                future_temporal_vector = [node.temporal_vector[1], host_clock.time_step]
                self.elements_to_transform.append(node)
                print(f"PERCEPTION FUNCTION INITIATED AT Element(Base-{node.base}, Temporal Vector - {node.temporal_vector}) FOR Future Element(Base-{future_base}, Temporal Vector - {future_temporal_vector})")
                break  # Perceive only one base-0 element for now

def update_terminal():
    print("\033c", end="")  # Clear terminal
    print(f"Step Time: {host_clock.time_step}")  # Static content
    for line in terminal_buffer[-buffer_size:]:  # Dynamic content
        print(line)

####################################################
####################################################
####################################################

terminal_buffer = []
buffer_size = 10  # 10 lines for dynamic content
static_lines = 3  # 3 lines for static content

# Initialize Memory Space
memory_space = MemorySpace()

# Initialize Perception Function
perception_function = PerceptionFunction()

# Initialize Element Update Engine
element_update_engine = ElementUpdateEngine(memory_space, perception_function)

# Initialize Host Clock
host_clock = HostClock()
host_clock.time_step = 0

# Initialize Bit Stream
bit_stream = BitStream()

# Initialize Infuser
infuser = Infuser(bit_stream)

# Initialize Pre-memory Staging
pre_memory_staging = PreMemorySpaceStaging()

# Initialize Topology Engine
topology_engine = TopologyEngine(memory_space)

# Initialize Element Update Engine
element_update_engine = ElementUpdateEngine(memory_space, perception_function)

# Main simulation loop
for i in range(10):
    host_clock.tick()  # Increment the host clock
    
    # Generate new bits
    bit_stream.generate_bits(1)
    
    # Create new elements based on bits and stage them
    infuser.generate_elements(pre_memory_staging)
    
    # Flush staging to Memory Space
    pre_memory_staging.flush_to_memory_space(memory_space)
    
    # Update topology
    for new_node in memory_space.nodes:
        topology_engine.update_topology(new_node)
        
    # # Update elements if any
    # if i == 5:  # Just an example condition
    #     perception_function.perceive(memory_space)
    # if perception_function.elements_to_transform:
    #     element_update_engine.update_elements()
    
    # Clear terminal and print step time
    print("\033c", end="")
    print(f"Step Time: {host_clock.time_step}")
    for idx, node in enumerate(memory_space.nodes):
        print(f"Element {idx}: {node}")
    print(f"Tick {host_clock.time_step} completed.")
