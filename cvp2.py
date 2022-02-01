"""Vehicles Routing Problem (VRP)."""

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] =    [[0, 24028, 33361, 14940, 1774262, 760200, 3711774, 1116440, 889401, 1406553, 677946, 1655264, 2917420, 3118469, 1717451, 918923, 1173682],
                                  [25049, 0, 8409, 10879, 1780040, 737264, 3688838, 1093504, 866465, 1412330, 655010, 1685450, 2894484, 3095533, 1723229, 949108, 1179460], [34059, 8586, 0, 14085, 1778967, 729045, 3680619, 1085286, 858247, 1411257, 646792, 1692340, 2886266, 3087315, 1722156, 955999, 1178386], [15494, 11675, 14024, 0, 1764978, 743121, 3694695, 1099361, 872322, 1397269, 660867, 1666781, 2900341, 3101390, 1708167, 930440, 1164398], [1759266, 1763806, 1763339, 1750571, 0, 2489969, 4556582, 2846210, 1272120, 365447, 2161890, 2057955, 4466800, 4667849, 114468, 1159322, 818842], [759694, 737056, 728371, 748741, 2505256, 0, 3373766, 357083, 1557349, 2137546, 415531, 2113411, 2312972, 2508417, 2448445, 1585863, 1876467], [3711685, 3689047, 3680362, 3700732, 4555335, 3333002, 0, 3088867, 3286647, 4412547, 3196864, 5305780, 1826871, 1521780, 4589433, 4569152, 4562174], [1114483, 1091844, 1083159, 1103529, 2860045, 356457, 3086603, 0, 1812051, 2492335, 705158, 2469163, 2007328, 2264586, 2803233, 1941615, 2232219], [888403, 865765, 857080, 877450, 1269599, 1556654, 3287130, 1812982, 0, 1126811, 1110836, 2219808, 3320815, 3521864, 1303698, 1309801, 1277108], [1407540, 1412081, 1411613, 1398845, 367435, 2138244, 4409915, 2494484, 1125452, 0, 1960929, 1692704, 4295464, 4496513, 310623, 794071, 453591], [678811, 656173, 647488, 667858, 2198812, 414304, 3196145, 704944, 1110693, 1977059, 0, 2325534, 2307708, 2508757, 2142001, 1589192, 1823793], [1658675, 1687580, 1695381, 1669659, 2062131, 2108759, 5310720, 2466196, 2221644, 1695701, 2341982, 0, 4399962, 4611920, 2005320, 1016640, 1290249], [2916353, 2893715, 2885030, 2905400, 4500619, 2311647, 1826738, 2005464, 3315163, 4294205, 2305607, 4398940, 0, 352527, 4443808, 3826734, 4061334], [3119005, 3096367, 3087682, 3108052, 4703271, 2510097, 1521204, 2265963, 3517815, 4496857, 2508259, 4617987, 352962, 0, 4646460, 4029386, 4263987], [1717432, 1721973, 1721505, 1708737, 131873, 2448136, 4588630, 2804376, 1304167, 312328, 2139644, 2004836, 4444554, 4645603, 0, 1106203, 765723], [920132, 949036, 956837, 931115, 1160805, 1586113, 4571960, 1943549, 1305381, 794374, 1603438, 1013504, 3842912, 4043961, 1103994, 0, 329819], [1174366, 1178906, 1178439, 1165671, 820955, 1876470, 4559124, 2233906, 1274662, 454525, 1822816, 1287984, 4062290, 4263339, 764144, 329730, 0]]
    
    [
        [
            0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354,
            468, 776, 662
        ],
        [
            548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674,
            1016, 868, 1210
        ],
        [
            776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164,
            1130, 788, 1552, 754
        ],
        [
            696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822,
            1164, 560, 1358
        ],
        [
            582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708,
            1050, 674, 1244
        ],
        [
            274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628,
            514, 1050, 708
        ],
        [
            502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856,
            514, 1278, 480
        ],
        [
            194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320,
            662, 742, 856
        ],
        [
            308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662,
            320, 1084, 514
        ],
        [
            194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388,
            274, 810, 468
        ],
        [
            536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764,
            730, 388, 1152, 354
        ],
        [
            502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114,
            308, 650, 274, 844
        ],
        [
            388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194,
            536, 388, 730
        ],
        [
            354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0,
            342, 422, 536
        ],
        [
            468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536,
            342, 0, 764, 194
        ],
        [
            776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274,
            388, 422, 764, 0, 798
        ],
        [
            662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730,
            536, 194, 798, 0
        ]
    ] 
    data['num_vehicles'] = 2
    data['depot'] = 0
    return data


def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    max_route_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += ' {} -> '.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        plan_output += '{}\n'.format(manager.IndexToNode(index))
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        print(plan_output)
        max_route_distance = max(route_distance, max_route_distance)
    print('Maximum of the route distances: {}m'.format(max_route_distance))




def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        100000000,  # vehicle maximum travel distance
        True,  # start cumul to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)


if __name__ == '__main__':
    main()