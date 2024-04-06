'''
1. Python Sets Adventure
Objective:
The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, 
ranging from basic operations to advanced manipulations and best practices. You will correct given codes, 
use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

Task 1: Flight Route Comparison
Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
You have two sets of flight destinations, one for each airline. Write a Python program to find out:

Destinations that both airlines fly to.
Destinations unique to your airline.
Whether there are any destinations that neither airline shares.
Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
'''

def shared_destinations(our_airline,*competitors):
  #                  the & is the same as intersection()
  shared_destination = our_routes & competitor_routes
  print(f"Shared Flights between Our Airline and Competitors:")
  for count, flights in enumerate(shared_destination):
    print(f"{count+1}. {flights}")


def unique_destinations(our_airline,*competitors):
  unique_destination = our_routes.difference(competitor_routes)
  print("Our Airlines unique destinations are:")
  for count, place in enumerate(unique_destination):
    print(f"{count +1}. {place}")
  

def destination_look_up(our_airline,*competitors):
  user_flight = input("Enter Air Port call sign (Ex. LAX): ").upper()
  all_flights = our_routes.union(competitors)
  if user_flight not in all_flights:
    print(f"The Flight '{user_flight}' is not in any of the Airlines on our line up.")
  elif user_flight in our_airline:
    print(f"The Flight '{user_flight}' is in Our Airline")
  else:
    print(f"The Flight '{user_flight}' is in A Competitors Airline")


our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


def main():
  print("Welcome to the Advanced Flight Look-up System")
  while True:
    print("\nMain Menu:\n1. Flight look-up\n2. Unique Destinations\n3. Shared Destinations\n4. Exit")
    user_input = input("Enter your choice: ")
    if user_input == "1":
      destination_look_up(our_routes,*competitor_routes)
    elif user_input == "2":
      unique_destinations(our_routes,*competitor_routes)
    elif user_input == "3":
      shared_destinations(our_routes,*competitor_routes)
    elif user_input == "4":
      print("Thank you for using our Advanced Flight Look-up System")
      break
    else:
      print("Invalid Input") 

main()   
