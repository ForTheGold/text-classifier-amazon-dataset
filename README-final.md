# Project One - Artificial Meat Review Predictions

### Group Three Members 
 - Tamar Brand-Perez
 - Tiffany Price
 - Ben Tubbs
 - Jose Santos

## Topic

The topic of our project involves artificial meat review predictions.  

## The Why

We selected this topic because the artificial meat industry is becoming increasingly popular as of late.  We find it the industry very interesting and want to understand how consumer experience and resulting reviews can predict ratings. After pulling and cleaning our data set from Amazon, we used the Natural Language Processing machine learning model to train a sentiment classifier. During the cleaning process, both five and one star reviews will be maintained, while two, three and four star ratings will be removed.  Next, we will pull reviews without ratings and direct the machine to predict the ratings based on the analysis of the reviews.  

## Source Data

Our data set was pulled from the Amazon Grocery and Gourmet Food section (http://deepyeti.ucsd.edu/jianmo/amazon/index.html).  We scraped Amazon's website to pull reviews and ratings for our visualization. 

## Goals

In this project we will use a Natural Language Processing machine learning model to train a sentiment classifier on an Amazon dataset of Grocery and Gourmet Food reviews (https://jmcauley.ucsd.edu/data/amazon/) containing over 1 million reviews.  

The goal of this classifier is to predict user sentiment (positive or negative) for fake meat products.  Upon having ratings predicted based on the reviews through NLP, We believe this analysis will help store owners identify which fake meat brands to sell. Having access to a model to predict ratings will allow the stakeholder to understand how reviews affect ratings and, in turn, impact future sales of fake meat products.

## Database NEED TO ADD SCREEN SHOTS AND COMPLETE SECTION

Link to Google doc:

groceries_trimmed.csv:

https://drive.google.com/file/d/1RrqXXbHTOJ8rPADNauFVRPBzMXwekjYP/view?usp=sharing

The mockup database format for now is:

columns:

index, overall, reviewText

the overall is the rating number between one and five. We are focusing on 1 and 5 only. The review Text is the review content that we will analyze using NLP.

## Algorithm

The algorithm uses a bag of words model and a Naive Bayes classifier.  

### Machine Learning

The data was cleaned and exported to this csv file ( https://drive.google.com/file/d/1gEXXLB23iYxTxxyPFyhmQ-dfvjoEhTOl/view?usp=sharing ).  

The file was read and data was stored in an array, and the header was subsequently removed.  The data was cleaned for better processing, which included the removal of “stop words” which are words that do not add a lot of meaning to the content such as words like “the”, “in”, “at”, etc.  The data was also normalized by converting everything to lowercase.

Next, the data was tokenized which means splitting it by word and then a list of tuples was created which contains two items.  The first item is the list of strings of words contained within the text, and the second item is either the string “pos” or the string “neg”.  We worked with a large dataset of Amazon reviews; to help increase the processing speed, five star reviews were maintained as positive and one star reviews were maintained as negative.  All of the two, three and four star reviews were removed during the preprocessing step.

The positive reviews were shuffled for randomness; the same number of positive and negative reviews were included in one giant list.  The large list was then shuffled, which contains 809,640 items, half of which are positive and half of which are negative reviews.  

The bag of words model with a Naive Bayes classifier was used to classify the texts.  We experienced 82% accuracy with this model.  

### Interactive Website/Dashboard

LINK WEBSITE OR ADD SCREENSHOTS ESPECIALLY OF INTERACTIVE PORTIONS


## Visualizations
ADD TABLEAU SCREENSHOTS

## Presentation
A copy of the draft slides has been uploaded to our repository.  You can also link to the presentation here ADD LINK

### Conclusion
#### Results
In conclusion, our hope is to facilitate increased sales of artificial meat products by way of empowering store owners in their decision making process of which products/brands to sell.  Our ML model predicts the sentiment of user entered reviews with approximately 82% accuracy.  We have seen a range of 80-84% depending on which data is used to train the model.

Also, through use of our interactive website, stakeholders have the ability to understand customer sentiment upon testing reviews.
Finally, from the word clouds and the table analysis of the reviews, the stakeholder will be able to associate specific product description words with the respective brand. This allows for a deeper understanding of how customers choose to comment about a specific product and brand. 

#### Limitations
The limitations we experienced during our analysis include:
•	Our time frame was rushed; as were learning about the limitations of our data set, we were already using it. 
•	Since our initial data set was limited, we were not necessarily focused on the best data set available.  We operated with what we had and made the most of it due to time and resource constraints, including but not limited to, computer capacity and also eventually being blocked by Amazon during our web scraping.
•	Finally, the algorithm does not consider the order of words (ie food tastes great v great tasting food).

#### Further Analysis
If we were to continue future analysis, we would:
•	Include more interactive visualizations for the end user.
•	Scrape in a larger data set, as available.
•	Pull in location data of reviews to further enable stakeholders’ insight into consumer sentiment by location. This would allow for more market focused guidance. 

#### Ways to Improve Project
•	We would search for a more accurate algorithm
•	We would have our algorithm consider word order
•	Finally, we would host our website on a server
