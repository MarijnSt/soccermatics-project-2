# Soccermatics Pro - Project 2

This project was built as part of the Soccermatics Pro course I did. It's a machine learning project where I calculate an "Expected Danger" metric to analyse passes in the Premier League 2024/2025 season. 

Data was provided by Wyscout.

## Streamlit app
You can find a hosted version of the streamlit app [here](https://expected-danger.streamlit.app/)

## Linkedin post
Presenting data analysis to people who don't understand it can be tricky. I like to keep it as simple as possible and post a mini report on Linkedin as I would present it to coaches. You can find my post about this project [here](https://www.linkedin.com/in/marijn-stammeleer/)

## Technologies used
- **Scikit-learn** for danger pass and xG models
- **Streamlit** to create and host the app
- **Matplotlib** to make visualisations in notebooks
- **Plotly** for the interactive visualisation in the streamlit app

## Important files in this repository
[./expected_danger.ipynb](notebooks/expected_danger.ipynb)
- Contains code for models and summary data

[./streamlit_app.py](streamlit_app.py)
- Contains code for streamlit app

## Project assignment
Create an Expected Danger model
- Write code to identify all the passes made within 15 seconds of a shot
- Use logistic regression to look at how start and end coordinates of these passes determines the probability that it will be followed by a shot. Think about how to transform the variables and use non-linear transformations of the variables when fitting the model
- Use linear regression to look at how the start and end coordinates of the pass determine the probability of the shot being a goal
- Combine these to give probability of a goal given the start and end coordinates of a pass
- Rank players (grouped by position) in terms of their Expected Danger per 90. Compare that ranking to the number of danger passes made per 90