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
        base_1_nodes.sort(key=lambda x: x.temporal_vector[1], reverse=True)
        base_0_nodes.sort(key=lambda x: x.temporal_vector[1])

        if base_1_nodes and base_0_nodes:
            newest_base_1 = base_1_nodes[0]
            oldest_base_0 = base_0_nodes[0]

            # Clear existing singularity bridges
            for node in self.memory_space.nodes:
                node.topological_vector = [n for n in node.topological_vector if n.base == node.base]

            # Create new singularity bridge
            newest_base_1.topological_vector.append(oldest_base_0)
            oldest_base_0.topological_vector.append(newest_base_1)
            
            # Send the oldest base-0 node to the PerceptionFunction
            self.perception_function.perceive(oldest_base_0)
