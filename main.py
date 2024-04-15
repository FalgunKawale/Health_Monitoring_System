                                            # Health Monitoring System
import random
import time

class HealthMonitor:
    def __init__(self, user_id):
        self.user_id = user_id
        self.heart_rate = 0
        self.sleep_quality = 0
        self.steps = 0

    def measure_heart_rate(self):
        # Simulate heart rate measurement
        self.heart_rate = random.randint(60, 100)
        print(f"Heart rate: {self.heart_rate} bpm")

    def measure_sleep_quality(self):
        # Simulate sleep quality measurement
        self.sleep_quality = random.randint(0, 100)
        print(f"Sleep quality: {self.sleep_quality}")

    def measure_steps(self):
        # Simulate steps measurement
        self.steps += random.randint(1000, 5000)
        print(f"Steps: {self.steps}")

def main():
    user_id = input("Enter your user ID: ")
    monitor = HealthMonitor(user_id)

    print("Health Monitoring System")

    while True:
        print("\nSelect an option:")
        print("1. Measure Heart Rate")
        print("2. Measure Sleep Quality")
        print("3. Measure Steps")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            monitor.measure_heart_rate()
        elif choice == "2":
            monitor.measure_sleep_quality()
        elif choice == "3":
            monitor.measure_steps()
        elif choice == "4":
            print("Exiting Health Monitoring System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Simulate measuring data every 5 seconds
        time.sleep(5)

if __name__ == "__main__":
    main()
