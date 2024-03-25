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

## Development steps

1. Firstly, I needed to gather the lyrics of the Smiths' songs for a future dataset. The lyrics were taken from https://www.diegocaponera.com/the-smiths-complete-lyrics using requests and bs4, then put in the .csv file with pandas.
2. I compiled the lyrics in a .txt file, then used it to preprocess the texts and get tokens. Those tokens were 'fed' to word2vec model for its training.
3. For each line in the .txt file I calculated the average of words' vectors within the line. After estimating the optimal number of clusters with the elbow method I trained a k-means clustering model. Then I created a dictionary where keys are cluster labels IDs and values are lists of lines associated with each cluster.
4. The next step was to design response generation. Again, I made a function that calculates vectors' average but for a user's input. It takes vectors that are familiar to the word2vec model. The next function determines similarity between the user's vectors' average and each cluster centroid with the cosine similarity and picks a cluster with the greatest similarity. After that it chooses a random line associated with this cluster to send it to the user as a response. In case there are no familiar vectors in a user's input, it will fail to find a suitable cluster and the user will get a relevant message.
5. Finally it was time to create a bot. I made:
    1. handlers for basic commands like /start, /help and /info
    2. handlers for response generation. When a user presses the relevant command, it activates a finite-state machine. It is needed to keep generation as long as the user wants and eliminate the inconvenience of entering the command each time one tries to get a new response.
6. The last part is making a main.py which runs the bot. It also connects to a pythonanywhere deployment site using proxy. 
