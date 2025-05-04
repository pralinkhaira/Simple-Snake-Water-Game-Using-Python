
# Snake Water Gun Game

A modern implementation of the classic Snake Water Gun game with a graphical user interface (GUI) built using Python and Tkinter.

## Features

- 🎮 Interactive GUI with buttons for easy gameplay
- 📊 Score tracking for both player and computer
- 💾 Automatic score saving between sessions
- 🔄 New Game functionality
- 🎯 Clear visual feedback for each round
- 🎨 Modern and clean user interface

## Game Rules

The game follows the classic Snake Water Gun rules:
- Snake beats Water
- Water beats Gun
- Gun beats Snake

## How to Play

1. Run the game using Python:
   ```bash
   python main.py
   ```

2. Choose your move by clicking one of the three buttons:
   - Snake
   - Water
   - Gun

3. The computer will make its choice automatically
4. The result will be displayed in a popup window
5. Your score will be updated automatically
6. Use the "New Game" button to reset scores
7. Use the "Exit Game" button to quit

## Score System

- Update by [Pralin Khaira](https://github.com/pralinkhaira)
- Converted from command-line to modern GUI interface
- Added all core game features and functionality

## Score System

- Wins are tracked for both player and computer
- Scores are automatically saved to `game_score.json`
- Scores persist between game sessions
- You can start a new game at any time to reset scores

## Technical Details

- Built with Python 3.x
- Uses Tkinter for the GUI
- Implements JSON for score persistence
- Features error handling for file operations

## Requirements

- Python 3.x
- Tkinter (usually comes with Python installation)

## File Structure

- `main.py` - Main game file
- `game_score.json` - Score persistence file (created automatically)
- `README.md` - This documentation file

## Recent Updates

- Converted from command-line to GUI interface
- Added score tracking and persistence
- Implemented new game and exit functionality
- Added visual feedback for game results
- Improved user interface with modern design
- Added confirmation dialogs for important actions

## Future Improvements

Potential future enhancements could include:
- Adding sound effects
- Implementing different difficulty levels
- Adding animations for choices
- Creating a high score system
- Adding multiplayer support

## Contributing

Feel free to fork this repository and submit pull requests for any improvements you'd like to make.

## License

This project is open source and available for anyone to use and modify.