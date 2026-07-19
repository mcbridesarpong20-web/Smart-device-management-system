class SmartDevice:
    def __init__(self, device_id, name):
        if not device_id or not str(device_id).strip():
            raise ValueError("Device ID cannot be empty.")
        self.__device_id = device_id
        self.__power_status = False
        self.name = name

    @property
    def device_id(self):
        return self.__device_id

    @property
    def power_status(self):
        return "On" if self.__power_status else "Off"

    def turn_on(self):
        self.__power_status = True

    def turn_off(self):
        self.__power_status = False

    def display_info(self):
        print(f"Device Name: {self.name}")
        print(f"Device ID: {self.device_id}")
        print(f"Power Status: {self.power_status}")


class TemperatureSensor(SmartDevice):
    def __init__(self, device_id, name, temperature=22.0):
        super().__init__(device_id, name)
        self.temperature = temperature

    def read_temperature(self):
        if self.power_status == "Off":
            print(f"Cannot read temperature. {self.name} is powered off.")
        else:
            print(f"{self.name} Temperature Reading: {self.temperature}°C")


class SmartLight(SmartDevice):
    def __init__(self, device_id, name, brightness=50):
        super().__init__(device_id, name)
        self.__brightness = brightness

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, value):
        if 0 <= value <= 100:
            self.__brightness = value
        else:
            print("Brightness must be between 0 and 100.")

    def increase_brightness(self, amount=10):
        if self.power_status == "Off":
            print(f"Cannot adjust brightness. {self.name} is powered off.")
        else:
            self.brightness = min(100, self.__brightness + amount)
            print(f"{self.name} brightness increased to {self.__brightness}%.")

    def decrease_brightness(self, amount=10):
        if self.power_status == "Off":
            print(f"Cannot adjust brightness. {self.name} is powered off.")
        else:
            self.brightness = max(0, self.__brightness - amount)
            print(f"{self.name} brightness decreased to {self.__brightness}%.")

    def display_info(self):
        super().display_info()
        print(f"Brightness Level: {self.brightness}%")


class SecurityCamera(SmartDevice):
    def __init__(self, device_id, name):
        super().__init__(device_id, name)
        self.__recording_status = False

    @property
    def recording_status(self):
        return "Recording" if self.__recording_status else "Not Recording"

    def start_recording(self):
        if self.power_status == "Off":
            print(f"Cannot start recording. {self.name} is powered off.")
        else:
            self.__recording_status = True
            print(f"{self.name} has started recording.")

    def stop_recording(self):
        if self.power_status == "Off":
            print(f"Cannot stop recording. {self.name} is powered off.")
        else:
            self.__recording_status = False
            print(f"{self.name} has stopped recording.")

    def display_info(self):
        super().display_info()
        print(f"Recording Status: {self.recording_status}")


if __name__ == "__main__":
    sensor = TemperatureSensor("T101", "Living Room Sensor", 24.5)
    light = SmartLight("L202", "Bedroom Smart Light", 70)
    camera = SecurityCamera("C303", "Front Door Camera")

    devices = [sensor, light, camera]

    while True:
        print("\n--- Smart Device Management System ---")
        print("1. Display Device Information")
        print("2. Turn Device On")
        print("3. Turn Device Off")
        print("4. Read Temperature")
        print("5. Adjust Brightness")
        print("6. Start/Stop Recording")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\n--- Current Device Status ---")
            for dev in devices:
                dev.display_info()
                print("-" * 30)

        elif choice == "2":
            print("\nSelect a device to turn ON:")
            for i, dev in enumerate(devices, 1):
                print(f"{i}. {dev.name}")
            idx = int(input("Enter device number: ")) - 1
            if 0 <= idx < len(devices):
                devices[idx].turn_on()
                print(f"{devices[idx].name} is now turned ON.")

        elif choice == "3":
            print("\nSelect a device to turn OFF:")
            for i, dev in enumerate(devices, 1):
                print(f"{i}. {dev.name}")
            idx = int(input("Enter device number: ")) - 1
            if 0 <= idx < len(devices):
                devices[idx].turn_off()
                print(f"{devices[idx].name} is now turned OFF.")

        elif choice == "4":
            sensor.read_temperature()

        elif choice == "5":
            print("\n1. Increase Brightness")
            print("2. Decrease Brightness")
            sub_choice = input("Select action: ").strip()
            if sub_choice == "1":
                light.increase_brightness()
            elif sub_choice == "2":
                light.decrease_brightness()

        elif choice == "6":
            print("\n1. Start Recording")
            print("2. Stop Recording")
            sub_choice = input("Select action: ").strip()
            if sub_choice == "1":
                camera.start_recording()
            elif sub_choice == "2":
                camera.stop_recording()

        elif choice == "7":
            print("Exiting Smart Device Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid menu number.")