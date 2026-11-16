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
