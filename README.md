# CIT PC Connector

A Python application to automate the tedious process of logging into the campus Wi-Fi. Instead of manually navigating to the login page and entering credentials every time you connect, this program automates the entire process with a single click.

## Inspiration and Motivation 💡

Every time a student connects to the campus Wi-Fi, they are redirected to a login page to enter their username and password. This repetitive task can be cumbersome, especially when dealing with frequent disconnections. I built this application to bypass this tedious workflow, making the login process seamless and efficient.

The project began as a mobile app (using **Kivy**) and was later adapted for a desktop environment (using **Tkinter**), demonstrating the same core logic across different platforms.

## How it Works ⚙️

The program works by reverse-engineering the login process of the CIT Wi-Fi portal. It uses Python's `requests` library to simulate a web browser, sending a `POST` request to the login server with the necessary parameters.

### Key Logic

-   **Endpoint:** The login URL (`https://10.100.1.1:8090/login.xml`) is the destination for the login request.
-   **Payload:** The request includes a **`payload`** dictionary containing the username, password, and other parameters like `mode` and `producttype`. These parameters were discovered by observing the data sent by a web browser during a successful login.
-   **Headers:** The request also includes specific **`headers`** to mimic a standard web browser, ensuring the server accepts the connection and doesn't flag it as an unusual program.
-   **Response Handling:** The program checks the server's response. A successful login is indicated by a status code of `200` and a specific string in the response text, like `"You are signed in as"`.

## Project Structure 📁

The repository contains several files that showcase the logic and different application versions:

-   **`opensource.py`**: This file contains the core logic for connecting to the Wi-Fi. It is a simplified version of the code used in the full applications, demonstrating the `requests` payload and header configuration.
-   **`connector.py`**: A module containing a reusable `connect` function. This function is called by the desktop application (`citPC_desktop.py`) to handle the login process.
-   **`citPC_desktop.py`**: The desktop version of the application, built with the **Tkinter** library. It provides a simple graphical interface for entering credentials and triggering the login.

## Usage 🚀

### For Developers

The core logic can be integrated into any application. The `opensource.py` script can be run directly to test the connection. Simply update the `username` and `password` variables with your credentials.

### For Users

-   **Desktop App:** The `citPC_desktop.py` file provides a user-friendly interface. Just run the script, enter your credentials, and click connect.
-   **Mobile App:** The original mobile application was built using Kivy and provided the same seamless login experience on a smartphone. Link for Mobile app ->https://drive.google.com/file/d/1ObPaYTTq0AWcloaFy0C7VskUTUN5O00D/view?usp=drive_link

---