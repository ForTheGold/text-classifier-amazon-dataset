# project-one

A group project

## Week 1

The data was cleaned and exported to this csv file ( https://drive.google.com/file/d/1gEXXLB23iYxTxxyPFyhmQ-dfvjoEhTOl/view?usp=sharing ) by Tamar.  I am currently reading the data from the file rather than the database because we are still working on getting the data in a database.

I read in the file and stored the data in an array, then removed the header.  I wanted to clean up the data for better processing, so I removed “stop words” which are words that do not add a lot of meaning to the content such as words like “the”, “in”, “at”, etc.  I also normalized the data by converting everything to lowercase.

Next I tokenized the data which means splitting it by word and then created a list of tuples which contains two items.  The first item is the list of strings of words contained within the text, and the second item is either the string “pos” or the string “neg”.  We are working with a dataset of Amazon reviews which is absolutely huge, so I am using five star reviews as positive and one star reviews as negative.  Tamar removed all of the two, three and four star reviews in her preprocessing step.

I then shuffled up the positive reviews for randomness and included the same number of positive and negative reviews in one giant list.  I then shuffled this giant list which contains 809,640 items half of which are positive and half of which are negative reviews.  We can see some of the list items in the file.

I plan to use a bag of words model with a Naive Bayes classifier for starters in order to classify the texts.  We will see what kind of accuracy we can get with that type of model.  We are going to scrape some data about fake meat products to classify as either positive or negative.