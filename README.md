# text-summarizer
*An AI application built over Google's BERT model that can produce an extractive summary of a text.*

### Table of Contents 


### Setup
Follow these steps to setup the application on your system - 

#### Docker 
* 1) Install Docker on your PC (https://docs.docker.com/engine/install/)
* 2) Host your choice of TensorFlow model using Docker (the preprocessing is done for the model - ExtractiveSummarizer_v1_40_words)
  * Create a variable in your terminal - in windows powershell - ```$ Set-Variable -Name MODEL_PATH -Value "path/to/model"```
  * Pull tensorflow/serving image  - `$ docker pull tensorflow/tensorflow`
  * Run the tensorflow/serving image - `$ docker run -t --rm -d -p 8501:8501 -v   "$MODEL_PATH:/models/ExtractiveSummarizer_v1_40_words" -e MODEL_NAME=ExtractiveSummarizer_v1_40_words tensorflow/serving`
  * For any further reference to Tensorflow Serving, check out the following link to Docker documentation (https://www.tensorflow.org/install/docker)

#### Python 
**Have Python installed on your system (if not installed, use this https://www.python.org/downloads/)
Install the following packages globally in python**
* json 
* os
* numpy 
* nltk
* tensorflow 


 
 
#### Nodejs

* 1) Have nodejs installed in your system
* 2) Run `$ node index.js`
* 3) The application will be hosted on localhost:5000

### AI in action


### Sources 
* 1) Guardian Article considered in [AI in Action](#ai-in-action) section (https://www.theguardian.com/world/2021/jul/18/uk-covid-cases-could-hit-200000-a-day-says-neil-ferguson-scientist-behind-lockdown-strategy-england)
* 2) Google BERT 
* 3) Repositories performing extractive summarization
* 4) Docker installation documentation (https://docs.docker.com/engine/install/)
* 5) Tensorflow Serving documentation (https://www.tensorflow.org/install/docker)
* 6) Python Installation (https://www.python.org/downloads/)
* 7) Tensorflow Installation (https://www.tensorflow.org/install)

