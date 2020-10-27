# MovieData
This project is about how we can use REST API for interacting with time.

How it Works ?
-> We have a data in json file
-> Loaded data in the models (tables)
-> Through URL with paramter as name of the movie we can filter out the movies containing the parametric value

To handle this:
URL calls the respective which further calls serializer and interacts with the model for fetching the data.

DataBase used is SQLLite3

Project is deployed on Heroku also:
Link :  https://imdbtaskapp.herokuapp.com/api/MovieApp
