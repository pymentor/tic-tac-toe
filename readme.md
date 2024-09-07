### Tic Taс Toe emulator - Interview problem solution.

- Solution's author: Artsiom Praneuski (artem.pronevskiy@gmail.com, @artempronevskiy)
- Last revision: 2024-09-07

#### Table of contents:

- [Description](#description)
- [Dependencies to run the app](#requirements-to-run-the-app)
- [Steps to run the app](#steps-to-run-the-app)
- [Dependencies to run tests](#dependencies-to-run-tests)
- [Steps to run tests](#steps-to-run-tests)
- [Note for developers](#note-for-developers)
- [Issue reporting](#issue-reporting)
- [License](#license)

#### Description:

- This is a simple Tic Tac Toe emulator which allows to play the game in CLI mode.
- There is no human input. Both player moves are simulated. Moves are determined using an external randomizer service or a local one.
- Game stops as soon as there is a winner and the winner and cells of the boards get printed.

##### Requirements to run the app:

- Python: app was developed and tested using **3.12** version, but it should work with 3.10+ version
- External python libraries: **no external** libraries are needed (Python 3 **stdlib** is used only)
- External library is needed only for remote randomizer service, but it's considered to be not a part of the application itself.

#### Steps to run the app:

- Install dependencies for remote randomizer service:
```bash
python3 -m pip install -r remote_randomizer/requirements.txt
```

- Run remote randomizer service (in non production mode):
```bash
python3 remote_randomizer/main.py
```

- Run the Tic Tac Toe emulator:
```bash
python3 src/main.py
```

- To get more detailed information about the app's flow, set log level to `debug`:
```bash
python3 src/main.py --log-level debug
```

- To use local randomizer service, set `--randomizer-type` parameter to `local`:
```bash
python3 src/main.py --randomizer-type local
```

- See CLI help to get information about available commands:
```bash
python3 src/main.py --help
```

#### Dependencies to run tests:

- Python: app was developed and tested using **3.12** version, but it should work with 3.10+ version
- External python libraries: `pytest` package is needed to run tests

#### Steps to run tests:

- Install `pytest` package:
```bash
python3 -m pip install pytest
```

- Run tests:
```bash
export PYTHONPATH=src:tests
pytest tests
```

#### Note for developers:

- Application is developed using Clean Architecture approach with Onion architecture. There are the following layers with strict hierarchy and dependencies direction (shown by arrows):
```
                presenter
                    |
                    v
              infrastructure
                    |
                    v
                 service
                    |
                    v
                  domain
```
- Each layer has its own responsibilities and dependencies.
  - `presenter` layer is responsible for interaction with the user (CLI in this case).
  - `infrastructure` layer is responsible for low level components and interaction with external services (Randomizer service in this case).
  - `service` layer is responsible for game rules (use case).
  - `domain` layer is responsible for business logic and entities.
- All dependencies are injected into the components on `presenter` layer.
- Each layer is supposed to have its own tests.
- In order to keep modules structure and code clean - please use linters and formatters:
  - `black` for code formatting
  - `flake8` for code style checking
  - `mypy` for static type checking
  - `isort` for imports sorting

#### Issue reporting:

If you have found any issues or have any suggestions, please report them in the project's issue tracker.

#### License:

This project is licensed under the MIT License.
