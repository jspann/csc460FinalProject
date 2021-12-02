# CSC 460 Final Project - AugUR

By Ilene Kang and James Spann.

## Overview
This is a project to demonstrate and show the effects of climate change in certain affected areas. We do this with a website interface that allows users to see a photo they have selected as an augmented climate-affected landscape.

# Website Overview
The website uses the React Javascript library to create a beautiful interface that users can use to step through their understandings of climate change.

# Photo-realistic climate change model
This has two parts: the Segmentation model and the Inpainting model. Both of these models, along with some computational photo editing, allows for these photo-realistic climate change images to be generated. We use the segmentation model to find climate-related attributes of a photo (sky, vegetation, terrain, etc). This model was trained on the "CityScapes" dataset which we had to clean and repurpose for this task. We originally started with a resnet50 model implementation in PyTorch but later moved to a DeepLabv3+ mobilenet architecture. For the inpainting model we used a pretrained version of NVIDIA's "Image Inpainting for Irregular Holes Using Partial Convolutions" model to support our task. Once the relevant image parts have been found, we augment them for our task. After that is completed, we use Python's cv2 library to add smoke effects (based on the percieved future level of smoke in the area).

## How to set up the project
0. Install npm 
1. Clone the directory
2. cd into the project directory


To start the augUR flask model server:

3. cd 'augur/api'

4. run `python3 -m venv venv` to create a virtual environment for the flask server
5. run `source venv/bin/activate` to activate the virtual enviornment that was just created
6. run `pip install flask python-dotenv torch torchvision tqdm opencv-python visdom sklearn tensorflow==1.5.0` to add support for flask and the climate model
7. run `cd ..` to move up a directory (should now be in 'augur')
8. run `yarn start-api` to start the flask server

To Start the React server (in a second terminal window):

9. cd 'augur' and run `npm install` followed by `npm start`


## Future Work
- Improve the visualizations from the climate model
- Add more climate-based features into the model generated photo (i.e. photo-realistic increased population densities, water stress indicators)
