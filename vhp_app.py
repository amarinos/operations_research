from or_tools.vehicle_routing_problem import optimize_routes
from distance_api.distance_matrix import create_distance_matrix
from distance_api.geocoding import visualize_map
from constants import api_key




class VehicleRouting:
    """
    This class enables users to define and solve the vehicle routing problem.
    It uses the google distance API and the google OR-tools
    """
    def __init__(self,addresses = [],demands = [], vehicle_capacities = [], num_vehicles= 0, depot= 0, api_key = api_key):
        self.addresses = addresses
        self.demands = demands
        self.vehicle_capacities  = vehicle_capacities
        self.num_vehicles = num_vehicles
        self.depot = depot
        self.api_key = api_key
        self.distance_matrix = None

    def add_address_and_demand(self,address,demand):
        """
        Add an address to the addresses list
        """
        self.addresses.append(address)
        self.demands.append(demand)

    def remove_address(self,address):
        """
        Remove an address from the addresses list
        """
        idx = self.addresses.index(address)
        self.addresses.remove(address)
        self.demands.pop(idx)
    
    def add_vehicle(self,capacity):
        """
        Add a new vehicle to the fleet with given capacity
        """
        self.vehicle_capacities.append(capacity)
        self.num_vehicles+=1

    def create_distance_matrix(self):
        """
        Call the google distance API for the defined addresses parameter
        Calculates the distance_matrix and saves it within the class
        """
        self.distance_matrix = create_distance_matrix(self.addresses, self.api_key)

    def optimize_routes_vhp(self,):
        results = optimize_routes(self.distance_matrix,self.demands,self.vehicle_capacities,self.num_vehicles, self.depot)
        #location_list = [self.addresses[i] for i in results[:-1]]
        return results #location_list,

    def create_map(self,):
        results = visualize_map(self.addresses)
        return results