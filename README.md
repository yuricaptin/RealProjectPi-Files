# RealProjectPi-Files
This repository contains the files necessary for the creation and training of the model.

As I have said in the AlphaPi repository README file, people with darker skin tones will have a harder time being recognized by the model. There are times when they are correctly recognized. These only happen when there is a substantial amount of light being reflected on the face lightening the skin tone. This was from my own analysis after training the model multiple times throughout the day. Do note that this model is not a RNN, so it will not improve from multiple times of training due to the lack of short-term memory. This model does not utilize transfer-learning either.

The conversion of this model into .tflite format mixes up the input and output tensors and makes it difficult to pinpoint the exact cause of the error. From what I have seen on various github and StackOverflow QA's the rebuild of the model to fit the tflite model when converted is usually recommended. Due to time constraints I was not able to implement that. 

Note: THERE ARE FALSE POSITIVES AND FALSE NEGATIVES WHEN TESTING THE MODEL. DUE TO LACK OF A NVIDIA GPU THAT IS CAPABLE OF EFFICIENTLY TRAINING THE MODEL AND DUE TO THE SMALL DATA SAMPLE SIZE THERE ARE INSTANCES OF THESE OUTCOMES HAPPENING.

## Siamese Neural Network and Training for the Smart Home Security with Facial Recognition using Raspberry Pi

This github repo is for the creation and training of the Siamese Neural Network. Most of the files here will be included. You
will still have to create an anchor and positive folder to fill your images with.

### Table of Contents 

  - [**Code Lineup**](#codelineup)
  - [**Usage**](#usage)
  - [**Contributing**](#contributing)
  - [**License**](#license)
  
  
### Code Lineup

This section describes the files included in this repo and what order you should execute them in

- `RealProject.py`: This file contains the code for the creation of the Siamese Neural Network as well as the necessary information needed
- `RPTraining.py` : This file contains the code for training the model and testing the model yourself.
- `RPDataAugmentation.py` : This file contains the code for augmenting the dataset for both the anchor and positive folders.

### Usage

This section provides instructions on how to use the code in this repository:

1. Clone the repository:
2. Create an anchor folder and a positive folder in the `Image` folder
3. Make the modifications to the `RealProject.py` code then run that
4. Run the `RPTraining.py` script to train and test the model.

### Contributing

This section describes how to contribut to the project. 

Because of this project being a Senior Capstone Project, please send me an email if you would like to continue working on this.

ly01256@georgiasouthern.edu


### License

This section describes the license for the code in this repository. (Replace `LICENSE.md` with the appropriate license file for your project.)

This project is licensed under the terms of the [MIT license](LICENSE.md).
