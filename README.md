# Traffic Lights

To run:

	$ python3 main.py

this will execute with lights changing every 5 *seconds* with yellow lights warning half a second before.

To run tests:

	$ python3 tests.py

## 30 Minute output

Example 30 "minute" output can be found in output.txt. It's actually just run with the minute units replaced with second units, for simplicity.

## Design Decisions

### Single Threaded

Having a separate thread calling the intervals would have been more accurate but would have increased complexity.

### Functional

The code is designed in a functional fashion to made testing easier. Except for the main loop all state is passed in and returned out as python values. The end result is also small and readible.

### No Dependencies

No non-standard libraries were used to make the project portable and limit install difficulties. They also weren't needed.
