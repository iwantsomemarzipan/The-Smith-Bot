# The Smiths Bot

## Project description

Here is a project of a telegram bot that responds to a user’s message with a line from a song by The Smiths.
The main feature is that the line is selected based on semantic resemblance between word embeddings which is calculated with cosine similarity.

Bot id in telegram: @iluvthesmiths500_bot

Bot hosting on pythonanywhere: https://cfauh.pythonanywhere.com/

## Repository structure

**root directory**

stores the following files:
- example of a .env variable
- config file
- main.py that runs the bot
- readme
- requirements.txt

**data**

stores:
- crawler from which the data was compiled
- .csv dataset
- .txt files with lyrics
 
**word2vec_training**

stores:
- notebook with the model training
- the model itself

**sklearn_training**

stores:
- .pkl file of the gensim model
- .pkl file of the clustering model
- file where training of the clustering model is described
- script with response generation
- .png file of the elbow method graphic

**tg/handlers**

stores:
- start handler
- help and info handlers
- handlers for the response generation

**tg/lexicon**

stores:
- bot messages for handlers
