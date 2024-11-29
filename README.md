Screen-Scraping Loader Application

Overview
The Loader is a Python-based tool designed to automate data entry and extraction tasks for complex desktop applications that lack APIs. Using screen scraping and simulated user interactions, the Loader significantly reduces manual effort and enhances productivity.

Features

Automated Data Entry: Simulates mouse clicks and keyboard typing to input data into the application.
Screen Scraping: Captures and processes on-screen data using OpenCV for precise interaction.
Dynamic Adjustments: Adapts to varying screen resolutions and coordinate mapping.
Error Handling: Detects and resolves mismatches or delays during real-time execution.
Batch Processing: Processes multiple files or data points in a single run.
Technologies Used

Python: Core functionality.
OpenCV: Screen scraping and image recognition.
Pywinauto: GUI automation (switched to the win32 backend for enhanced compatibility).
How to Use

Configure the app with the file paths and data to be loaded.
Run the script to automate interactions with the target application.
Monitor the output for logs and any flagged inconsistencies.
Challenges Addressed

Overcame limitations of traditional Pywinauto APIs by switching to screen scraping with OpenCV.
Ensured compatibility across multiple systems with dynamic coordinate mapping.
Future Enhancements

Develop a robust GUI for configuration and monitoring.
Implement machine learning for smarter navigation and interaction.
