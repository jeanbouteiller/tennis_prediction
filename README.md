# A Machine Learning Approach of Tennis Gambling
## Past results

A few years ago, I worked on a project to use ML models to predict the winner of a tennis game, and hence design a betting strategy. We used exisiting datasets (online csv files) and ran models locally. Based on tennis expertise, we created innovative features to consider past players performances, as well as games specific aspects. We then defined Machine Learning models to find the likelihood of player A winner agains player B. We used ensemble methods to combine the power of different models & features and to benetif from the group's different approaches. We finally used these odds to define a gambling strategy (based on the welsh ratio from the financial world). This lead to a theoretical profit of +40% per game (for 1$ invested, we make on average 1.4$ or revenue). Excited by theoretical results, I decided to move forward and to be confronted to the challenges of productionisation. 

## Project Description

We can summarize the project by mentionning the following main items: 
1. _Data Collection from different sources_: we are designing python jobs to run every day/week and collect relevant data directly on the ATP website. We create raw csv files that update every day/week.
2. _Data aggregation and cleaning_: we are cleaning the above mentioned data and merging them by identifying relevant unique keys. Python script are running in the backend. 
3. _Feature Engineering_: Using the dataset above mentioned, we can transform them to perform ML predictions and create relevant features
4. _Model deployment and testing_: using the features above mentioned, we want to develop ML models and test them live to measure performance.
5. _Design of a betting strategy_: using the odds of the model above, we will define a budget allocation strategy and apply it to future games. Betting is manual. 

## Folder Organisation

Here, we want to give further details about the organisation of this repo, introducing the reader to the different folders. Component of each folder will be detailed in the local readme. 

1. [data](https://github.com/jeanbouteiller-ds/tennis_prediction/tree/main/data) contains all dataset used in this project, organized in different subfolders
2. [reports](https://github.com/jeanbouteiller-ds/tennis_prediction/tree/main/reports) contains documents used to assess the quality of the different steps of the project. It will be used to collect test results when those will be in production.
3. [functions](https://github.com/jeanbouteiller-ds/tennis_prediction/tree/main/functions) contains all pieces of codes that are used across notebooks. It defined functions that are imported at the beginning of each script.
4. [workflow_notebooks](https://github.com/jeanbouteiller-ds/tennis_prediction/tree/main/workflow_notebooks] contains all notebooks that are scheduled to run in the different workflows.
5. [.github/workflows](https://github.com/jeanbouteiller-ds/tennis_prediction/tree/main/.github/workflows) contains yml files needed to automate the execution of the scripts.

This project also contains the following documents: 
- password.txt contains the identification to my gihub key. It is read by the notebooks to access the different piecs of the project.
- [Table initialisation](https://github.com/jeanbouteiller-ds/tennis_prediction/tree/main/Table_initialization) is a one-time run notebook that initiates the tables used in this project. These tables are then updated by the workflows mentioned above. 
