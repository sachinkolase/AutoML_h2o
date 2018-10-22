# AutoML_h2o
AutoML is a function in H2O that automates the process of building large number of models, with the goal of finding the “best” model without any prior knowledge
The implementation is available in both R and Python API and the current version of AutoML (in H2O 3.20 ) performs:

Trains and cross-validates a default Random Forest (DRF), an Extremely Randomized Forest (XRT), a random grid of Gradient Boosting Machines (GBMs), a random grid of Deep Neural Nets, a fixed grid of GLMs.

AutoML then trains two Stacked Ensemble models.

First ensemble containing all the models and second ensemble containing just the best performing model from each algorithm class.

AutoML is here to stay. I am eager to see the direction where it goes to further advancements in data science. A single automated mixer certainly cannot outperform a human creative mind when it comes to feature engineering but in my experience, AutoML is worth exploring.

Although AutoML alone won’t get you top spot in machine learning competitions, it is definitely worth considering as an addition alongside your blended and stacked models.
