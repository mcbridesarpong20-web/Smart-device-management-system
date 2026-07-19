# Smart-device-management-system
# README.md

A Python-based Object-Oriented Programming (OOP) project that simulates a management system for various smart home devices[span_0](start_span)[span_0](end_span). The system models real-world smart devices using clean inheritance structures, robust encapsulation, and a terminal-based interactive control menu[span_1](start_span)[span_1](end_span).

---

## Task Summary

The application provides a software backbone to track, update, and monitor the power statuses and individual capabilities of different connected electronics[span_2](start_span)[span_2](end_span):

* **SmartDevice (Parent Class):** Standardizes core attributes such as a secure device ID, public device name, and underlying power metrics[span_3](start_span)[span_3](end_span).
* **TemperatureSensor (Child Class):** Inherits global behaviors and provides unique environmental temperature readouts[span_4](start_span)[span_4](end_span).
* **SmartLight (Child Class):** Inherits global behaviors and integrates variable brightness scaling, capped strictly between 0% and 100%[span_5](start_span)[span_5](end_span).
* **SecurityCamera (Child Class):** Inherits global behaviors and handles live monitoring statuses[span_6](start_span)[span_6](end_span).

### Key Programming Principles Demonstrated
* **Inheritance & Subclassing:** Shared behaviors are housed efficiently in a central class, reducing boilerplate code through `super()` constructor initializations[span_7](start_span)[span_7](end_span).
* **Encapsulation:** Protected properties (like device identifiers, recording statuses, and light intensiveness) remain secure from direct external alterations, utilizing standard properties and setter guards to ensure valid system input[span_8](start_span)[span_8](end_span).
* **Modular Architecture:** The codebase decouples explicit hardware components cleanly for seamless long-term maintainability[span_9](start_span)[span_9](end_span).

---

## How to Run the Program

Follow these quick steps to set up and run the terminal program locally:

### Prerequisites
* Ensure **Python 3.x** is installed on your operating system.

### Running the Script

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/smart-device-management-system.git](https://github.com/YOUR_USERNAME/smart-device-management-system.git)
   cd smart-device-management-system
