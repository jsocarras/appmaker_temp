# Dice Roll Simulator User Manual

## Introduction

The Dice Roll Simulator is a Python script that allows users to simulate rolling dice in a web application. It can be integrated into a Streamlit web application and provides the functionality to select the number of dice and display the result of each roll.

## Installation

To use the Dice Roll Simulator, you need to install the required dependencies. You can do this by running the following command:

```
pip install -r requirements.txt
```

This will install the necessary version of Streamlit.

## Usage

To use the Dice Roll Simulator, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where the `main.py` file is located.

3. Run the following command to start the Streamlit web application:

   ```
   streamlit run main.py
   ```

4. A web application will open in your default browser.

5. On the left sidebar, you will see a "Dice Count" section. Use the slider to select the number of dice you want to roll (between 1 and 6).

6. Click the "Roll Dice" button to simulate rolling the dice.

7. The result of each roll will be displayed below the button.

8. You can change the number of dice and roll them again by adjusting the slider and clicking the "Roll Dice" button.

9. To exit the web application, close the browser tab or press `Ctrl+C` in the terminal or command prompt.

## Session State Management

The Dice Roll Simulator uses session state management to maintain the dice count and dice objects between interactions. This means that the selected number of dice and the dice objects will be preserved even if you refresh the web application or navigate to a different page.

## Customization

If you want to customize the Dice Roll Simulator, you can modify the `main.py` file and the `dice.py` file.

- In the `main.py` file, you can change the minimum and maximum values of the dice count slider, as well as the range of possible dice roll results.

- In the `dice.py` file, you can modify the `Dice` class to add more properties or methods to the dice objects.

## Conclusion

The Dice Roll Simulator provides a simple and interactive way to simulate rolling dice in a web application. It can be easily integrated into a Streamlit web application and allows users to select the number of dice and see the result of each roll. The session state management ensures that the selected dice count and dice objects are maintained between interactions.