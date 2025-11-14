PRODUCT BACKLOG - VERSION 1:
1. A simple csv file with world countries and capitals.
2. Load the csv file into a dataframe.
3. A 7x3 Bingo grid generator with random numbers (no blank spaces).
4. Tests to make sure we did the greed and the uploaded de csv file correctly.

In the first version of the backlog, we focused on building the technical foundations of the project. This included creating the CSV file with countries and capitals, loading it into a DataFrame, generating the 7x3 Bingo grid, and running basic validation tests.
At this stage, the main goal was to ensure the game’s data and core structure worked properly, without yet addressing the user interface, difficulty levels, or additional features, hence we decided to add this to the product backlog



PRODUCT BACKLOG - VERSION 2:
1. A simple csv file with world countries and capitals.
2. Load the csv file into a dataframe.
3. A 7x3 Bingo grid generator with random numbers (no blank spaces).
4. Tests to make sure we did the greed and the uploaded de csv file correctly.
5. Load dataframe
6. Unit tests for data
7. Create Gitignore
8. Create attempts
9. Create different levels
10. Implement draw_capitals test

In this version, we expanded the backlog with new features related to project structure, version control, and gameplay logic, such as implementing a .gitignore file, adding limited attempts, and introducing different difficulty levels.
We realized that using the entire world capitals dataset made the game too difficult, especially for younger players. To make the learning experience more progressive, we decided to include multiple difficulty levels, starting with an easier set of European capitals for Level 1. We also added a unit test for the draw_capitals module, to verify that countries and capitals were being selected correctly and that the quiz logic worked consistently.


PRODUCT BACKLOG - FINAL VERSION: 
1. Create CSV file with countries and capitals
2. Load CSV data into a pandas DataFrame.
3. Generate bingo cards (7x3 grid)
4. Implement unit tests for data and grid validation.
5. Begin version control setup (GitHub repository, .gitignore…).
6. Improve project structure (folders, __init__.py, and requirements.txt).
7. Implement a basic user interface in the terminal.
8. Integrate DataFrame reading and number display logic.
9. Create attempts (5).
10. Exit conditions (q).
11. Detect numbers in card and mark them when found.
12. Add win condition detection (full Bingo)
14. Testing and debugging
15. Avoid repeating Capitals
16. Make more visual the crossing of the number in the bingo card.
17. Create different levels of difficulty
18. Display instructions of game

In the final backlog version, we included enhancements to make the game more engaging, educational, and user-friendly.
We added a feature to avoid repeating capitals, ensuring players always get new learning opportunities in each session.
The visual representation of crossed-out numbers on the Bingo card was improved — instead of using brackets, numbers are now clearly marked to make the game state easier to follow. Finally, we included on-screen instructions so players can easily understand how to play, and reinforced the testing and debugging phase to guarantee a stable and fully functional final product.



| Priority | Product Backlog Item | User Stories | Sprint | Status |
|----------|---------------------|--------------|--------|--------|
| **1** | Create CSV file with countries and capitals | *As a developer, I want to create a database (CSV file) containing all countries and their capitals so that the game can generate random questions efficiently.* |**Sprint 1**| ✅ Done |
| **2** | Load CSV data into a pandas DataFrame | *As a developer, I want to be able to use the content of the CSV in the Python files.* | **Sprint 1** | ✅ Done |
| **3** | Generate bingo cards (7x3 grid) | *As a user, I want to be able to see my drawn numbers in an intuitive and typical "Bingo" way.* | **Sprint 1** | ✅ Done |
| **4** | Implement unit tests for data and grid validation | *As a developer, I want to ensure there are no mistakes in the implementation of the data and grid creation.* | **Sprint 1** | ✅ Done |
| **5** | Begin version control setup (GitHub repository, .gitignore…) | *As a developer, I want to be able to actively work with my team, sharing a same virtual workspace and saving changes along the way.* | **Sprint 2** | ✅ Done |
| **6** | Improve project structure (folders, __init__.py, and requirements.txt) | *As a developer, I want to make my project as structured and clear as possible in order for it to be maintainable and easy to change.* | **Sprint 2** | ✅ Done |
| **7** | Implement a basic user interface in the terminal | *As a developer, I want to create a first user interface to be able to test the functionality.* | **Sprint 2** | ✅ Done |
| **8** | Integrate DataFrame reading and number display logic | *As a developer, I want to display a random number if the capital is guessed correctly.* | **Sprint 2** | ✅ Done |
| **9** | Create attempts (5) | *As a user, I want to have several attempts before the game is over.* | **Sprint 2** | ✅ Done |
| **10** | Exit conditions (q) | *As a user, I want to be able to quit the game at any time.* | **Sprint 2** | ✅ Done |
| **11** | Detect numbers in the card and mark them when found | *As a user, I want the system to automatically mark numbers on my bingo card when I answer correctly so that gameplay feels smooth and interactive.* | **Sprint 3** | ✅ Done |
| **12** | Add win condition detection (full Bingo) | *As a user, I want the game to automatically detect when the entire card is completed so that I immediately know when I win.* | **Sprint 3** | ✅ Done |
| **13** | Testing and debugging | *As a developer, I want to make sure my code works efficiently and does not contain any errors.* | **Sprint 3** | ✅ Done |
| **14** | Avoid repeating capitals | *As a user, I do not want to be asked the same capital more than once in each round as I want to learn as many capitals as possible.* | **Sprint 3** | ✅ Done |
| **15** | Make the user interface more visual | *As a developer, I want to make the user interface as simple and aesthetically pleasing as possible.* | **Sprint 3** | ✅ Done |
| **16** | Create different levels of difficulty | *As a user, I want to be able to choose between difficulty levels to make the game more challenging and engaging.* | **Sprint 3** | ✅ Done |
| **17** | Display instructions of game | *As a user, I want to know clearly how to play the game correctly.* | **Sprint 3** | ✅ Done |
| **18** | Update and complete all test files except the load-data CSV test | *As a developer, I want all unit tests to be updated so the project is fully validated and stable after major feature changes.* | **Sprint 4** | Pending |

