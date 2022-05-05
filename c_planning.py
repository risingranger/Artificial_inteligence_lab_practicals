# Conditional planning
import random

left_room = {
    "room":"left",
    "status":"dirty"
}

right_room = {
    "room":"right",
    "status":"clean"
}
# Initial position of vaccum is in the left room.

class Vaccum:
  def _init_(self):
    self.room = ""
    
  def suck(self, room):
    # Suck the dirt from the room and make it clean
    room["status"] = "clean"
  
  def move_from(self, room):
    # While moving from a room. It may be possible that the room may be left dirty
    self.room = ""
    if random.randint(1, 100) > 65:
      room["status"] = "dirty"

  def move_to(self, room):
    self.room = room["room"]

vaccum = Vaccum()

print("Initial state: ")
print(f"Left room : {left_room['status']}")
print(f"Right room : {right_room['status']}\n")

while left_room["status"] == "dirty" or right_room["status"] == "dirty":
  if right_room["status"] == "dirty":
    vaccum.move_from(left_room)
    vaccum.move_to(right_room)
    vaccum.suck(right_room)
    print("Cleaned right room")

  if left_room["status"] == "dirty":
    vaccum.move_from(right_room)
    vaccum.move_to(left_room)
    vaccum.suck(left_room)
    print("Cleaned left room")

  print(f"Left room : {left_room['status']}")
  print(f"Right room : {right_room['status']}\n")

if left_room["status"] == "clean" and right_room["status"] == "clean":
  print("\nReached the goal state")
