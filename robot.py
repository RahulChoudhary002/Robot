class Robot:
    def __init__(self, name, model, year_created, purpose):
        self.name = name
        self.model = model
        self.year_created = year_created
        self.purpose = purpose
        self.powered_on = False
        self.battery_level = 100

    def power_on(self):
        if not self.powered_on:
            self.powered_on = True
            print(f"{self.name} is now powered on!")
        else:
            print(f"{self.name} is already powered on.")

    def power_off(self):
        if self.powered_on:
            self.powered_on = False
            print(f"{self.name} is now powered off.")
        else:
            print(f"{self.name} is already powered off.")

    def introduce(self):
        print("\n" + "="*40)
        print(f"Hello! I am {self.name}, model {self.model}.")
        print(f"I was created in {self.year_created}.")
        print(f"My purpose is: {self.purpose}")
        print(f"Current status: {'Powered On' if self.powered_on else 'Powered Off'}")
        print(f"Battery level: {self.battery_level}%")
        print("="*40 + "\n")

    def perform_task(self, task):
        if not self.powered_on:
            print(f"Cannot perform task - {self.name} is powered off.")
            return
        
        if self.battery_level < 10:
            print("Warning: Battery critically low! Please recharge.")
            return
        
        print(f"{self.name} is now performing: {task}")
        self.battery_level -= 15
        print(f"Task completed! Battery level now: {self.battery_level}%")

    def recharge(self):
        self.battery_level = 100
        print(f"{self.name} has been fully recharged!")

    def update_purpose(self, new_purpose):
        self.purpose = new_purpose
        print(f"{self.name}'s purpose has been updated to: {new_purpose}")


my_robot = Robot(
    name="RoboGenius",
    model="X-3000",
    year_created=2023,
    purpose="To assist humans with programming and learning OOP concepts"
)

my_robot.introduce()
my_robot.power_on()
my_robot.perform_task("explaining OOP concepts")
my_robot.perform_task("demonstrating class methods")
my_robot.update_purpose("To teach Python programming and AI concepts")
my_robot.introduce()
my_robot.power_off()