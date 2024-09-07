#### Game "Tic Tac Toe".

##### Goal: Write a simulator for the game "Tic Tac Toe".

##### Requirements:

- The application should simulate the game "Tic Tac Toe" without user input, i.e., player moves should be determined by a random number generator.
- When using a random number generator, it is necessary to use a remote service to which the application should make HTTP requests and receive a response, based on which the next player's move should be determined. It is also necessary to support a random number generator that works in the interpreter's memory through the random module.
- The application should have a CLI or WEB interface for launching the application and its initial configuration.
- The type of algorithm for determining player moves - a remote random number generator or random within the interpreter - should be accepted by the application from the user through the CLI or WEB interface when launching the application (during the initial configuration of the application).
- The game should stop if a winner is determined after the player's next move. At this point, the name of the winning player should be returned (displayed), as well as the game board with cells on which the result of the game would be visible.
- The written code should be covered with unit tests.
- The application, during its operation, should write logs of the level (info, debug, ...) that the user will set when launching the application through the CLI or WEB interface.
- The application should depend on a minimum number of external libraries (libraries installed from the PyPI repository), or not depend on external libraries at all and use only the standard Python library.
- The application should have a structured readme file with all the necessary information about the project.

##### The solution to the task will be evaluated according to the following criteria/directions:

- Functionality (everything described in the requirements is implemented)
- Code cleanliness, best practices, and architecture (the code is easy to read, understand, and expand)
- Tests (everything described in the requirements is covered by tests)
