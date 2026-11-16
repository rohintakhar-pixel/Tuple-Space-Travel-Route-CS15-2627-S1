mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

print(f"First destination: {mission_route[0]}")
print(f"Last destination: {mission_route[-1]}")

print(f"Total destinations: {len(mission_route)}")

print("Mission route:")
for destination in mission_route:
    print(destination)

if "Europa" in mission_route:
    print("Europa is part of the mission route.")
else:
    print("Europa is not part of the mission route.")

search = input("Enter a destination to search for: ")

if search in mission_route:
    print(f"{search} is part of the mission route.")

    position = 0
    for destination in mission_route:
        if destination == search:
            break
        position = position + 1

    stops_from_end = len(mission_route) - 1 - position

    print(f"Stops from start: {position}")
    print(f"Stops from end: {stops_from_end}")

    if stops_from_end == 0:
        print("This is the final stop of the journey.")
    else:
        print(f"Next stop: {mission_route[position + 1]}")
else:
    print(f"{search} is not part of the mission route.")
