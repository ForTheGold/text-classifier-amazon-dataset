# Week 1 - Possible Visualizations in Dashboard

1. Analysis of distribution of positive and negative reviews based on number words in review (TRAINING SET versus PREDICTION SET;  number of words (x-axis) vs number of positive reviews)

![](/Resources/distribution-based-on-number-words.png)
https://medium.com/plotly/nlp-visualisations-for-clear-immediate-insights-into-text-data-and-outputs-9ebfab168d5b


2. Positive / negative reviews by product


3. Positive and negative reviews by date – progression in time of sentiment
![](/Resources/word_size-dashboard.PNG)

https://avantopy.com/blog/analyze-texts-in-dashboards/

4. Plot of products with the most negative and positive reviews.
5. N-grams to show the most frequently used words (tokens) in positive and negative reviews (compare TRAINING SET versus PREDICTION SET).

![](/Resources/treemap.PNG)
https://medium.com/plotly/nlp-visualisations-for-clear-immediate-insights-into-text-data-and-outputs-9ebfab168d5b

![](/Resources/bubble-chart.PNG)
https://medium.com/plotly/nlp-visualisations-for-clear-immediate-insights-into-text-data-and-outputs-9ebfab168d5b

# Week 2 - Dashboard Template

Agreed to a template for the dashboard that would show the comparison of two brands of fake meat products, selected from the drop down menu.  The 2 slide dashboard shall contain the following graphics:

First a comparison of the word frequence used to describe reviews that are predicted to be positive, and those that are negative:

![](/Resources/Dashboard-1.PNG)

then a slide showing how the sentiment for the brand changes with time by depicting the number of positive reviews (upward bar) and negative reviews (downward bar)

![](/Resources/Dashboard-2.PNG)

# Week 3  & 4 - Dashboard Template

Will use scraping data from 5 different brands to generate figures for dashboard - scrapping data from an average of 3 products per brand:

![](/Resources/project-list.PNG)

Decided to create three template visualizations: 
1. Word cloud to show 10 most frequent used words in negative and positive reviews per brand:

    ![](/Resources/Boca-BYM-neg.PNG)

    ![](/Resources/BYM-pos-neg.PNG)

    ![](/Resources/Boca-pos-neg.PNG)

    ![](/Resources/Gardein-pos-neg.PNG)

    ![](/Resources/Quorn-pos-neg.PNG)

    ![](/Resources/Tofurky-pos-neg.PNG)


2. Table to show frequency with which top 10 words appeared in all product negative and positve reviews per brand.  

    ![](/Resources/top10-neg.PNG)

    ![](/Resources/top-10-pos.PNG)

3. Plot of average price and average rating evolution over time (per year) - Tiffany designed this:

    ![](/Resources/Review-price-evolution.PNG)

Created word cloud by taking text of reviews in csv format (obtained from Tiffany) - ~1000 total reviews (~200 per) - note that there were 834 positive reviews and only 173 negative reviews - and converting text to columns.  

Then filtered out CSV file to only contain 1) reviews with ratings of 1 or 2 (negative reviews) and 2) reviews with ratings of 4 or 5 (positive reviews) to create two new CSV files.

     ![](r1-2-scraped_reviews-text-to-columns.csv)

     ![](r4-5-scraped_reviews-text-to-columns.csv)

Next each csv file was saved as unicode text and imported as a data source into tableau.  

All figures were created in tableau.

Stop words were filtered out using a list of words taken from: http://xpo6.com/list-of-english-stop-words/

Then a filter was applied to only show the top 10 most frequent words for each brand.

