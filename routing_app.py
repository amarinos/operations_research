from or_tools.travelling_salesman_problem import optimize_routes
from distance_api.distance_matrix import create_distance_matrix
from distance_api.geocoding import visualize_map
from constants import api_key

class RoutingOptimizer:
    """
    This class enables access to the google distance API and the google OR-tools
    You can provide a set of addresses, get the distance matrix between them and then calculate
    the optimal routing between them (travelling salesman problem)

    Args:
        addresses: Define a list of addresses when initializing (not mandatory)
        depot: Define the integer position in the list, where your depot (starting point) is
    """
    def __init__(self,addresses = [],depot= 0, api_key = api_key):
        self.addresses = addresses
        self.depot = depot
        self.api_key = api_key
        self.distance_matrix = None

    def add_address(self,address):
        """
        Add an address to the addresses list
        """
        self.addresses.append(address)

    def remove_address(self,address):
        """
        Remove an address from the addresses list
        """
        self.addresses.remove(address)

    def create_distance_matrix(self):
        """
        Call the google distance API for the defined addresses parameter
        Calculates the distance_matrix and saves it within the class
        """
        self.distance_matrix = create_distance_matrix(self.addresses, self.api_key)

    def optimize_routes_tsp(self,):
        results = optimize_routes(self.distance_matrix, self.depot)
        location_list = [self.addresses[i] for i in results[:-1]]
        return location_list,results

    def create_map(self,):
        results = visualize_map(self.addresses)
        return results
        
class VehicleRouting:
    """
    This class enables users to define and solve the vehicle routing problem.
    It uses the google distance API and the google OR-tools
    """
    def __init__(self,addresses = [],demand = [], depots= [], api_key = api_key):
        self.addresses = addresses
        self.demand = demand
        self.depots = depots
        self.api_key = api_key
        self.distance_matrix = None

    def add_address(self,address):
        """
        Add an address to the addresses list
        """
        self.addresses.append(address)

    def remove_address(self,address):
        """
        Remove an address from the addresses list
        """
        self.addresses.remove(address)

    def create_distance_matrix(self):
        """
        Call the google distance API for the defined addresses parameter
        Calculates the distance_matrix and saves it within the class
        """
        self.distance_matrix = create_distance_matrix(self.addresses, self.api_key)

    def optimize_routes_tsp(self,):
        results = optimize_routes(self.distance_matrix, self.depot)
        location_list = [self.addresses[i] for i in results[:-1]]
        return location_list,results

    def create_map(self,):
        results = visualize_map(self.addresses)
        return results