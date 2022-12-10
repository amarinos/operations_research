from __future__ import division
from __future__ import print_function
import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
import json
from urllib.request import urlopen

def create_distance_matrix(addresses, api_key):
  # Distance Matrix API only accepts 100 elements per request, so get rows in multiple requests.
  max_elements = 100
  num_addresses = len(addresses)
  # Maximum number of rows that can be computed per request (6 in this example).
  max_rows = max_elements // num_addresses
  # num_addresses = q * max_rows + r (q = 2 and r = 4 in this example).
  q, r = divmod(num_addresses, max_rows)
  dest_addresses = addresses
  distance_matrix = []
  # Send q requests, returning max_rows rows per request.
  for i in range(q):
    origin_addresses = addresses[i * max_rows: (i + 1) * max_rows]
    response = send_request(origin_addresses, dest_addresses, api_key)
    distance_matrix += build_distance_matrix(response)

  # Get the remaining remaining r rows, if necessary.
  if r > 0:
    origin_addresses = addresses[q * max_rows: q * max_rows + r]
    response = send_request(origin_addresses, dest_addresses, api_key)
    distance_matrix += build_distance_matrix(response)
  return distance_matrix

def send_request(origin_addresses, dest_addresses, api_key):
  """ Build and send request for the given origin and destination addresses."""
  def build_address_str(addresses):
    # Build a pipe-separated string of addresses
    address_str = ''
    for i in range(len(addresses) - 1):
      address_str += addresses[i] + '|'
    address_str += addresses[-1]
    return address_str

  request = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'
  origin_address_str = build_address_str(origin_addresses)
  dest_address_str = build_address_str(dest_addresses)
  request = request + '&origins=' + origin_address_str + '&destinations=' + \
                       dest_address_str + '&key=' + api_key
  jsonResult = urlopen(request).read()
  response = json.loads(jsonResult)
  return response

def build_distance_matrix(response):
  distance_matrix = []
  for row in response['rows']:
    row_list = [row['elements'][j]['distance']['value'] for j in range(len(row['elements']))]
    distance_matrix.append(row_list)
  return distance_matrix

########
# Main #
########
def define_distance_matrix(addresses, api_key):
  """Entry point of the program"""
  # Create the data.
  distance_matrix = create_distance_matrix(addresses, api_key)
  print(distance_matrix)
  return(distance_matrix)