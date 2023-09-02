from math import factorial
import random
import time
import os
os.system('cls' if os.name == 'nt' else 'clear')
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
        self.bits = [random.randint(0, 1) for _ in range(num_bits)]

class Infuser:
    def __init__(self, bit_stream):
        self.bit_stream = bit_stream
    def generate_elements(self, pre_memory_staging):
        for bit in self.bit_stream.bits:
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
    def __init__(self, memory_space, perception_function=None):
        self.memory_space = memory_space
        self.perception_function = perception_function

    def update_topology(self, new_node):
        for node in self.memory_space.nodes:
            if node is not new_node:
                if new_node not in node.topological_vector:
                    node.topological_vector.append(new_node)
                if node not in new_node.topological_vector:
                    new_node.topological_vector.append(node)
        self.create_singularity_bridge()

    def create_singularity_bridge(self):
        base_1_nodes = [node for node in self.memory_space.nodes if node.base == 1]
        base_0_nodes = [node for node in self.memory_space.nodes if node.base == 0]
    
        if base_1_nodes and base_0_nodes:
            base_1_nodes.sort(key=lambda x: x.temporal_vector[1], reverse=True)
            base_0_nodes.sort(key=lambda x: x.temporal_vector[1])
            newest_base_1 = base_1_nodes[0]
            oldest_base_0 = base_0_nodes[0]

        # Clear existing singularity bridges
            for node in self.memory_space.nodes:
                node.topological_vector = [n for n in node.topological_vector if n.base == node.base]

            # Create new singularity bridge
            newest_base_1.topological_vector.append(oldest_base_0)
            oldest_base_0.topological_vector.append(newest_base_1)
            
            # Send the oldest base-0 node to the PerceptionFunction
            self.perception_function.perceive(oldest_base_0, newest_base_1)


    def calculate_max_density(self, base):
        try:
            base_nodes = [node for node in self.memory_space.nodes if node.base == base]
            n = len(base_nodes)
            if n < 2:
                return 0
            num_complete_walks = factorial(n - 1)
            steps_per_walk = n - 1
            return num_complete_walks * steps_per_walk
        except Exception:
            return "N/A"
    def calculate_total_unique_walks(self, base):
        try:
            base_nodes = [node for node in self.memory_space.nodes if node.base == base]
            n = len(base_nodes)
            if n < 2:
                return 0
            return factorial(n - 1)
        except Exception:
            return "N/A"

def print_system_state(memory_space, topology_engine, current_step):
    # Clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    try:
        max_density_0 = topology_engine.calculate_max_density(0)
        max_density_0 = format_max_density(max_density_0)
        total_unique_walks_0 = topology_engine.calculate_total_unique_walks(0)
    except Exception:
        max_density_0 = "N/A"
        total_unique_walks_0 = "N/A"

    try:
        max_density_1 = topology_engine.calculate_max_density(1)
        max_density_1 = format_max_density(max_density_1)
        total_unique_walks_1 = topology_engine.calculate_total_unique_walks(1)
    except Exception:
        max_density_1 = "N/A"
        total_unique_walks_1 = "N/A"
        
    # Print the fixed header
    print(f"BASE 0 || CURRENT STEP: {current_step} ||||| Total Nodes: {len([node for node in memory_space.nodes if node.base == 0])} ||||| Max Density: {max_density_0} ||||| Total Unique Walks: {total_unique_walks_0}")
    print(f"BASE 1 || CURRENT STEP: {current_step} ||||| Total Nodes: {len([node for node in memory_space.nodes if node.base == 1])} ||||| Max Density: {max_density_1} ||||| Total Unique Walks: {total_unique_walks_1}")
    available_lines = 30 - 2  # 2 lines are for the fixed headers
    base_0_nodes = [node for node in memory_space.nodes if node.base == 0]
    base_1_nodes = [node for node in memory_space.nodes if node.base == 1]
# Sort each list by time step
    sorted_base_0_nodes = sorted(base_0_nodes, key=lambda x: x.temporal_vector[1], reverse=True)[:available_lines]
    sorted_base_1_nodes = sorted(base_1_nodes, key=lambda x: x.temporal_vector[1], reverse=True)[:available_lines]
    sorted_nodes = sorted_base_0_nodes + sorted_base_1_nodes
    for idx, node in enumerate(sorted_nodes):
        same_base_nodes = [n for n in memory_space.nodes if n.base == node.base]
        singularity_bridge_connection = [n for n in node.topological_vector if n.base != node.base]
        singularity_bridge_str = "none" if not singularity_bridge_connection else f"{singularity_bridge_connection[0].temporal_vector}"
    
        print(f"_[Base {node.base}, {node.temporal_vector}][- {len(same_base_nodes)} -, [{singularity_bridge_str}]]_", end="")
        if (idx + 1) % 3 == 0:  # New line after every 3 nodes
            print()
    print("\n")
def format_max_density(max_density):
    max_density_str = str(max_density)
    num_digits = len(max_density_str)
    if num_digits > 21:
        trimmed = max_density_str[:21]
        excess = num_digits - 21
        return f"{trimmed}({excess})"
    else:
        return f"{max_density}(0)"


class Node:
    def __init__(self, base, host_clock):
        self.base = base
        self.temporal_vector = [0, 0]
        self.topological_vector = []
        self.host_clock = host_clock
        self.time_step = host_clock.time_step
    def __repr__(self) -> str:
        return f"Base-{self.base}, Temporal Vector-{self.temporal_vector}, Topological Vector Length-{len(self.topological_vector)}"

class PerceptionFunction:
    def __init__(self):
        self.elements_to_transform = []
    def perceive(self, specific_node, defining_node):
        future_temporal_vector = [defining_node.temporal_vector[1], host_clock.time_step]
        self.elements_to_transform.append((specific_node, future_temporal_vector, host_clock.time_step))



class ElementUpdateEngine:
    def __init__(self, memory_space, perception_function):
        self.memory_space = memory_space
        self.perception_function = perception_function
    def update_elements(self):
        new_queue = []
        for node, future_temporal_vector, update_time in self.perception_function.elements_to_transform:
            if update_time == host_clock.time_step:
                node.base = 1
                node.temporal_vector = future_temporal_vector  # Set it directly
            else:
                new_queue.append((node, future_temporal_vector, update_time))
        self.perception_function.elements_to_transform = new_queue



# Initialize
memory_space = MemorySpace()
perception_function = PerceptionFunction()
element_update_engine = ElementUpdateEngine(memory_space, perception_function)
host_clock = HostClock()
bit_stream = BitStream()
infuser = Infuser(bit_stream)
pre_memory_staging = PreMemorySpaceStaging()
topology_engine = TopologyEngine(memory_space, perception_function)

# Main loop
for i in range(1000):
    host_clock.tick()
    if host_clock.time_step == 10:
        special_node = Node(1, host_clock)
        special_node.temporal_vector = [0, host_clock.time_step]
        memory_space.add_node(special_node)
    bit_stream.generate_bits(1)
    infuser.generate_elements(pre_memory_staging)
    pre_memory_staging.flush_to_memory_space(memory_space)
    for new_node in memory_space.nodes:
        topology_engine.update_topology(new_node)
    print_system_state(memory_space,topology_engine, host_clock.time_step)
    element_update_engine.update_elements()  # Add this line
    time.sleep(0.5)

    
