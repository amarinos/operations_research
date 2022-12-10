from or_tools.travelling_salesman_problem import optimize_routes
from distance_api.distance_matrix import create_distance_matrix
from constants import api_key

# Enter addresses
class RoutingOptimizer:
    def __init__(self,addresses = [],depot= 0, api_key = api_key):
        self.addresses = addresses
        self.depot = depot
        self.api_key = api_key
        self.distance_matrix = None

    def add_address(self,address):
        self.addresses.append(address)
        return self.addresses

    def remove_address(self,address):
        self.addresses.remove(address)
        return self.addresses

    def create_distance_matrix(self):
        try:
            
            self.distance_matrix = create_distance_matrix(self.addresses, self.api_key)
        except:
            print("Error in creating distance matrix")

    def optimize_routes_tsp(self,):
        results = optimize_routes(self.distance_matrix, self.depot)
        return results