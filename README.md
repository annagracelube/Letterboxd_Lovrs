**Letterboxd Lovrs**

-	Jonathan Tran : jontrn

-	Rachel Prempeh : rprempeh

-	Anna Grace Lube  annagracelube

-	[Letterboxd Lovrs Repository](https://github.com/annagracelube/Letterboxd_Lovrs)

-	[Video Demo]()

---

*Problem*

We always find it difficult to settle on a movie to watch, whether in a group setting or alone. The indecisiveness, from what we know, is a universal feeling. Having so many options at the tip of our fingers is too overwhelming. Would it not be nice to have a curated list of movies chosen from thousands? This is possible with our new program : *Movie Matchers*! This program will help alleviate the stress of choosing the perfect movie for everyone.  

---

*Features Implemented*

Prompted with questions to narrow down the search, the user will choose three different types of genres, a range of movie lengths, and then a range of when the movie got released. Through this, our program will run through an algorithm, user’s choice, to curate the best five options for the user to choose from. It will also display which streaming platforms the movies are available on.

Given two different algorithm choices, a hash map function through C++ and then K nearest neighbors through machine learning with python, the user will be able to opt for either of those, and then the chosen algorithm, will run to get the five most relevant movies, according to user input.

With a movie library of 100k movies, we have available information of the types of genres, the year the movie was released, and runtime to trickle down the options to get the best suited list of movies for the user.

---

*Code Description*

Our k nearest neighbors, kNN, program, implemented with python, will take user input and compare it against all of the data in our dataset. This is a classification type of problem and so we will be able to print out the top five most relevant movies by adding the user input as a new point to the dataset and then finding out which movies are the closest neighbors to the point. 

With our C++ program, we have created the hash map algorithm to read in the dataset and add those points to the hash map. With the user input, we will compare it to each member of the hash map by adding a counter to the hash map class and adding to it when there is an overlap, outputting the top five movies with the highest counter. In the situation that there are more than five movies that best match the input, we will sort the movies by best rating and that will determine the movies.

---

*Distribution*

When we initially began the project, we allocated the different aspects of the project throughout the group of us. Actually executing the project, some of the jobs changed. Jonathan Tran ended up completing the hash map function and implementation by himself and he also contributed to the GUI of our program. Rachel Prempeh amended the dataset to include new columns and add more datapoints to get the dataset to 100,000. She also contributed to the GUI as well as aided with the machine learning kNN program. Anna Grace Lube was assigned the machine learning part, with Rachel Prempeh, as well as completed the report aspect of the project. We all researched and contributed creatively to the assignment, asking and answering questions for how we wanted to execute each part of the assignment, as well as the development of the original idea itself.

---

*Analysis*

There were only a few things, when completing the project, we changed. We redistributed the roles, as stated previously, as well as a few other things. We added some things: the list of different streaming websites the user can find the movies, as well as had to reformat some of the parameters for the dataset. We wanted to provide more information about the movies themselves, after receiving the top list by giving them access to how the user could watch whichever movie, with streaming platforms making more movies accessible and saving the user a google search. Giving the user a chance to see how reviewers thought that had watched the movie also gives more insight to an overall, succinct, public opinion. We decided to omit the movie poster of the most relevant movie due to the fact that storing 100,000 photos of the movie posters would be inefficient when it came to running the actual program.

---

*Reflection*

Overall, our group found the experience a positive one. We were able to meet multiple times throughout when the project was assigned and until it was due, bouncing ideas back and forth between each other, and working on our parts of the project, individually, on our own time. It was a very open space and there was plenty of positive feedback running throughout our group, everyone being able to freely share what they thought would be best, as well as any changes that could work. We were all very open about issues we ran into and lifted each other up whenever we could.

There were not many challenges we ran into, other than sometimes being a little too ambitious about what was possible with our GUI, given the amount of time and resources that we had. Time was probably the most challenging aspect of this. With us officially starting the project a little later than what we all would have liked with all of us having busy and conflicting schedules, we all agree we could have spread our workload for this project a little better over a longer period of time.

Recompleting this assignment, we all would have liked to begin a little sooner than we did. We would have created the same quality of work had we started earlier, but the amount that we worked would have been more spaced out. We also might think to use a different machine learning algorithm, due to the fact that kNN has a very bad time complexity. There were also different ways to implement kNN which could have also decreased the time complexity that we could have tested out.

- *Jonathan Tran* : I was able to enhance and better understand how to utilize GitHub to improve my projects and learn how to work in a collaborative project. I also have a better grasp on how to implement hash maps and manipulate them for easier use

- *Rachel Prempeh* : 

- *Anna Grace Lube* : I learned the importance of communication through group work and how important GitHub is to group assignments for an easier transfer of information between the group members when working individually.
