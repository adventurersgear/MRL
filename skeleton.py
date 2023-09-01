from math import factorial
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
        self.update_topology(node)
    def update_topology(self, new_node):
        if new_node.base == 0:
            for node in self.nodes:
                if new_node.base == 0 and node is not new_node:
                    node.topological_vector.append(new_node)
                    new_node.topological_vector.append(node)
    

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
    def update_topology(self):
        pass
    def calculate_walks_and_steps(self):
        n = len(self.memory_space.nodes)
        if n < 2:
            return 0, 0  # No walks or steps if less than 2 nodes

        num_unique_walks = factorial(n - 1)
        total_steps = (n - 1) * num_unique_walks
        return num_unique_walks, total_steps

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
        self.temporal_vector = []
        self.topological_vector = []
        self.place = None  # Will be updated later
        self.host_clock = host_clock
        self.time_step = host_clock.time_step
    
    def __repr__(self) -> str:
        return f"Node(Base-{self.base}, Temporal Vector - {self.temporal_vector}, Topological Vector Length - {len(self.topological_vector)})"

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

# Initialize Memory Space
memory_space = MemorySpace()

# Initialize Perception Function
perception_function = PerceptionFunction()

# Initialize Element Update Engine
element_update_engine = ElementUpdateEngine(memory_space, perception_function)

# Initialize Host Clock
host_clock = HostClock()

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

# Tick Loop for Simulation
for i in range(7):  # Run for 10 ticks
    host_clock.tick()
    
    # Generate Bits
    bit_stream.generate_bits(1)
    
    # Infuse Bits to Elements and Stage Them
    infuser.generate_elements(pre_memory_staging)

    if i == 5:
        perception_function.perceive(memory_space)
    
    # Flush Staging to Memory Space
    pre_memory_staging.flush_to_memory_space(memory_space)
    
    # Update Topology
    topology_engine.update_topology()
    
    if perception_function.elements_to_transform:
        element_update_engine.update_elements()
    
    # Print elements in MemorySpace
    print(f"Tick {host_clock.time_step} completed. MemorySpace contains {len(memory_space.nodes)} elements.")
    
    # Print element structure for verification
    for idx, node in enumerate(memory_space.nodes):
        print(f"Element {idx}: Base-{node.base}, Temporal Vector-{node.temporal_vector}, Topological Vector-{node.topological_vector}")
