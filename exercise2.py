from queue import Queue

class DeskManager:
    def __init__(self):
        self.patient_queue = Queue()

    def register_patient(self, patient_name):
        """Register a new patient."""
        self.patient_queue.put(patient_name)
        print(f"Patient '{patient_name}' registered.")

    def remove_patient(self):
        """Remove the next patient after they meet the doctor."""
        if not self.patient_queue.empty():
            next_patient = self.patient_queue.get()
            print(f"Patient '{next_patient}' met the doctor and has been removed from the queue.")
        else:
            print("No patients in the queue.")

    def display_patient_queue(self):
        """Display the current patient queue."""
        if not self.patient_queue.empty():
            print("Current Patient Queue:")
            for index, patient in enumerate(list(self.patient_queue.queue), start=1):
                print(f"{index}. {patient}")
        else:
            print("No patients in the queue.")

def main():
    desk_manager = DeskManager()

    while True:
        print("\nMenu:")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_name = input("Enter patient's name: ")
            desk_manager.register_patient(patient_name)
        elif choice == '2':
            desk_manager.remove_patient()
        elif choice == '3':
            desk_manager.display_patient_queue()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
