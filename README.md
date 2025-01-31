# semester-project
This project is a **Yearly Calendar with Event Management**, created using **Python and Tkinter**. 

The main goal of this project is to display a full-year calendar where users can add and remove events on specific dates. I used Tkinter to build the graphical user interface because it is simple and easy to work with.

One of the important things in this project is that events are saved even after closing the program. To do this, I used the pickle module, which allows me to store the events in a file (`events.pkl`). Every time the program starts, it loads the saved events so that the user does not lose any information.

I created several functions to make the program work properly:
- show_year_calendar(): This function generates the calendar for the given year. It arranges the months in a grid and correctly places the days in the right position.
- add_event(): This function lets users enter an event name and date in a small pop-up window. After the event is added, it is stored using pickle.
- remove_event(): Instead of asking the user to type a date, I made a scrollable list of events, so the user can just select which one to remove. This makes it easier and reduces errors.
- save_events() and load_events(): These functions handle saving and loading event data from a file.

I also used different colors and fonts in Tkinter to make the interface clear and easy to read. The event days are highlighted in blue, while the rest of the calendar remains in a light cream color. This project helped me understand Tkinter layouts, event handling, file storage, and user-friendly UI design.

**User-documentation**:
 
 Step 1: 
- Enter the year you want to see your calendar. Then click to "show calendar" button. 
You will now get a yearly calendar view. 

 Step 2:
- To add/remove event, use the buttons in the bottom of the window. 
 To add first name the event, in the next window that will be opened enter the date you want to add the event. If correctly implemented, you will see the event colored differently. Also when clicked on the date you will see what event you have on that day (a window will pop up).

 Note: The program will save the date added even if you exit. 

- To remove the event, click to "Remove Event" button and enter the date you want to remove. 

- To exit you can simply click on "Exit" button.