from or_tools.travelling_salesman_problem import optimize_routes
from distance_api.distance_matrix import create_distance_matrix


# Enter addresses
# Enter number of vehicles
# enter depot
def solve_tsp(addresses, depot, api_key):
    distance_matrix = create_distance_matrix(addresses, api_key)

    results = optimize_routes(distance_matrix, depot)
    return results