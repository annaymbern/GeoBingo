PRODUCT BACKLOG - VERSION 1:
1. A simple csv file with world countries and capitals.
2. Load the csv file into a dataframe.
3. A 7x3 Bingo grid generator with random numbers (no blank spaces).
4. Tests to make sure we did the greed and the uploaded de csv file correctly.

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


<table>
  <thead>
    <tr>
      <th>Priority</th>
      <th>Product Backlog Item</th>
      <th>User Stories</th>
      <th>Sprint</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>1</b></td>
      <td>Create CSV file with countries and capitals</td>
      <td><i>As a developer, I want to create a database (CSV file) containing all countries and their capitals so that the game can generate random questions efficiently.</i></td>
      <td style="background-color:#FFF8B3;">1</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>2</b></td>
      <td>Load CSV data into a pandas DataFrame</td>
      <td><i>As a developer, I want to be able to use the content of the CSV in the Python files.</i></td>
      <td style="background-color:#FFF8B3;">1</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>3</b></td>
      <td>Generate bingo cards (7x3 grid)</td>
      <td><i>As a user, I want to be able to see my drawn numbers in an intuitive and typical “Bingo” way.</i></td>
      <td style="background-color:#FFF8B3;">1</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>4</b></td>
      <td>Implement unit tests for data and grid validation</td>
      <td><i>As a developer, I want to ensure there are no mistakes in the implementation of the data and grid creation.</i></td>
      <td style="background-color:#FFF8B3;">1</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>5</b></td>
      <td>Begin version control setup (GitHub repository, .gitignore…)</td>
      <td><i>As a developer, I want to be able to actively work with my team, sharing a same virtual workspace and saving changes along the way.</i></td>
      <td style="background-color:#C8F7C5;">2</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>6</b></td>
      <td>Improve project structure (folders, __init__.py, and requirements.txt)</td>
      <td><i>As a developer, I want to make my project as structured and clear as possible in order for it to be maintainable and easy to change.</i></td>
      <td style="background-color:#C8F7C5;">2</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>7</b></td>
      <td>Implement a basic user interface in the terminal</td>
      <td><i>As a developer, I want to create a first user interface to be able to test the functionality.</i></td>
      <td style="background-color:#C8F7C5;">2</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>8</b></td>
      <td>Integrate DataFrame reading and number display logic</td>
      <td><i>As a developer, I want to display a random number if the capital is guessed correctly.</i></td>
      <td style="background-color:#C8F7C5;">2</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>9</b></td>
      <td>Create attempts (5)</td>
      <td><i>As a user, I want to have several attempts before the game is over.</i></td>
      <td style="background-color:#C8F7C5;">2</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>10</b></td>
      <td>Exit conditions (q)</td>
      <td><i>As a user, I want to be able to quit the game at any time.</i></td>
      <td style="background-color:#C8F7C5;">2</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>11</b></td>
      <td>Detect numbers in the card and mark them when found</td>
      <td><i>As a user, I want the system to automatically mark numbers on my bingo card when I answer correctly so that gameplay feels smooth and interactive.</i></td>
      <td style="background-color:#CDEAFF;">3</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>12</b></td>
      <td>Add win condition detection (full Bingo)</td>
      <td><i>As a user, I want the game to automatically detect when the entire card is completed so that I immediately know when I win.</i></td>
      <td style="background-color:#CDEAFF;">3</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>13</b></td>
      <td>Testing and debugging</td>
      <td><i>As a developer, I want to make sure my code works efficiently and does not contain any errors.</i></td>
      <td style="background-color:#CDEAFF;">3</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><b>14</b></td>
      <td>Avoid repeating capitals</td>
      <td><i>As a user, I do not want to be asked the same capital more than once in each round as I want to learn as many capitals as possible.</i></td>
      <td style="background-color:#CDEAFF;">3</td>
      <td>🕓 Pending</td>
    </tr>
    <tr>
      <td><b>15</b></td>
      <td>Make the user interface more visual</td>
      <td><i>As a developer, I want to make the user interface as simple and aesthetically pleasing as possible.</i></td>
      <td style="background-color:#EEEEEE;">Not Assigned</td>
      <td>-</td>
    </tr>
    <tr>
      <td><b>16</b></td>
      <td>Create different levels of difficulty</td>
      <td><i>As a user, I want to be able to choose between difficulty levels to make the game more challenging and engaging.</i></td>
      <td style="background-color:#EEEEEE;">Not Assigned</td>
      <td>-</td>
    </tr>
    <tr>
      <td><b>17</b></td>
      <td>Display instructions of game</td>
      <td><i>As a user, I want to know clearly how to play the game correctly.</i></td>
      <td style="background-color:#EEEEEE;">Not Assigned</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
