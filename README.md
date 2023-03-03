# Calculator
This code is a simple calculator application with a graphical user interface (GUI) using the tkinter module. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division. The application also integrates with Discord Rich Presence (RPC) to display the user's current activity in the application.

The application window is created using the tkinter module, and it contains two entry boxes for inputting the numbers and four buttons for performing the arithmetic operations. When the user clicks on a button, the corresponding function is called, which retrieves the numbers from the entry boxes, performs the calculation, and displays the result in a label.

The GUI is styled using the ttk module, which provides more modern-looking widgets than the standard tkinter widgets. The background color of the GUI is set to "#1C1C1C", and the foreground color of the buttons is set to "#4CAF50".

The code also includes a function called "update_rpc", which updates the Discord Rich Presence information for the user. The function is called whenever an arithmetic operation is performed, and it updates the user's Discord status to show that they are performing a calculation.

Finally, the code initializes the Discord RPC client and connects to it, and it calls the "update_rpc" function once to update the initial status. The client ID for the Discord application is defined in the code as '1234'.
