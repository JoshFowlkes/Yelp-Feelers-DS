# Data Science - Spotifier
This is the Data Science portion for an Application that uses Machine Learning to build a Yelp Adjusted Ratings App based on a User's  text review which is then put through a rigorous Sentiment Analysis.

You can visit the application here: [Yelp_Feelers]('http://fixthislinkwheneverythingisdone.com')

## Flowchart
![Alt text]('./FlowChart.png')

## Project Info
For the Data Science portion of this application, we used this Kaggle [Yelp](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/6#yelp_business.csv) Dataset. Within it you will find a number of reviews from Yelp Users on a variety of places ranging from restaurants and bars to salons and plumbers. For the sake of this project, we were tasked with analyzing taco restaurants due to the sheer volume of observations in the dataset(5 million + rows). We used a variety of tools such as  Pandas, Gensim, and Sklearn for our simpler models. We used TensorFlow for experimentation with neural networks on our data. Our primary strategy was Sentiment Analysis using A Vectorizer, a scaler, then both regression/classification models. We found regression to be the best approach for our particular problem, and we trained the tokenized/vectorized data on a our target(the yelp stars). We found the linear model actually worked nicely in this case because it gives a more accurate sentiment rating because of the weights that certain words used. Whereas something highly accurate like a neural net did perform incredibly well, but our goal wasn't to perfectly predict what the star ratings were, it was to give an adjusted rating that was a better representation of the actual true rating of a restaurant based on what the user said. 
From there, we worked extensively with our back-end architect to get the data in a format that he could easily work with. After some trials we finally got it nailed down a nice a succint method of getting our data to the back end, and from there we could easily tinker with and adjust data as the rest of the team needed.

## Logs

October 21, 2019 Exploratory Data Analysis & Initial Modeling, Mock Data To Backend
October 22, 2019 Optimize Model for better accuracy, Set up End points for Backend 
October 23, 2019 Done with the bulk of both MVP and Strech Requirments. Form here just further optimzation & on standby incase our team needs help with anything.
October 24, 2019 Final day, just standing by incase our team needs us. Otherwise we're making little tweaks here and there, improving what can be improved upon, and otherwise just allow the rest of the areas of our team to do what they do best. 

## Contributing
Pull requests are welcome. However for major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
