# semester-project
This project is a **Yearly Calendar with Event Management**, created using **Python and Tkinter**. 

The main goal of this project is to display a full-year calendar where users can add and remove events on specific dates. I used Tkinter to build the graphical user interface because it is simple and easy to work with.

One of the important things in this project is that events are saved even after closing the program. To do this, I used the pickle module, which allows me to store the events in a file (`events.pkl`). Every time the program starts, it loads the saved events so that the user does not lose any information.

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


**Developer documentation**:
- load_events()
 Checks if events.pkl exists. If yes, it loads data from that file into the global events dictionary.
If the file does not exist, no action is taken (the events dictionary stays empty).

- save_events()
 Serializes the current contents of the events dictionary into events.pkl using pickle.dump().
Ensures event data will be available next time the program runs.

- add_event()
 Prompts the user for an event name and a date in YYYY-MM-DD format.
If valid inputs are provided, creates or updates the event in the events dictionary and saves changes to disk by calling save_events().
Refreshes the displayed calendar to reflect the new event.

- remove_event()
 Asks the user for a date in YYYY-MM-DD format.
If an event exists for that date, it is removed from the dictionary. The updated dictionary is then saved.
The calendar is refreshed so the removed event no longer appears.

- is_leap_year(year)
 Returns True if the specified year is a leap year, or False otherwise.
Follows the Gregorian rule: leap years are those divisible by 4 but not by 100, or divisible by 400.

- get_days_in_month(month, year)
 Returns the number of days in the given month of the specified year, taking into account whether the year is a leap year (for February).
get_start_day(month, year)

- Computes which day of the week the first day of a given month falls on.
 Uses 1900-01-01 as a reference point and counts days forward.
Returns an integer (0 to 6), where 0 corresponds to Sunday, 1 to Monday, and so forth.

- show_year_calendar()
 Reads the user’s input for the desired year from a Tkinter text entry box.
Clears out any previously drawn calendar frames, then generates a grid of 12 month frames.
Each frame contains buttons for each day in that month.
Days with events are highlighted with a colored border, and clicking on them shows event details.
s
- how_event(date)
 Invoked when a user clicks on a specific day.
Checks if the date is in the events dictionary and displays the associated event name.
If there is no event, it informs the user accordingly.