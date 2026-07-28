# Coders-of-Andhra-Pradesh
Python Data Analysis &amp; Recommendation System
# Code Explanation

## Overview

This project is implemented using **pure Python** and demonstrates how structured JSON data can be loaded, cleaned, analyzed, and used to generate recommendations. The program is divided into small functions, where each function performs a specific task, making the code modular and easy to understand.

---

## 1. Loading the Data

The `load_data()` function is responsible for reading the JSON file.

* It opens the JSON file in read mode.
* Uses Python's built-in `json.load()` function to convert the JSON data into Python dictionaries and lists.
* Returns the loaded data so that it can be processed by the remaining functions.

This acts as the entry point of the project.

---

## 2. Displaying the Data

The `display_data()` function is used to print the contents of the dataset in a readable format.

For every user, it displays:

* User ID
* Name
* Friends list
* Liked pages

It also prints all available pages with their corresponding IDs.

This function is mainly useful for verifying that the dataset has been loaded correctly.

---

## 3. Data Cleaning

Before performing any analysis, the dataset is cleaned using the `cleaned_data()` function.

The cleaning process consists of four steps:

### Remove Empty User Names

Users whose names are empty are removed from the dataset.

### Remove Duplicate Friends

Each user's friends list is converted into a **set** to eliminate duplicate friend IDs and then converted back into a list.

### Remove Invalid Users

Users who have neither friends nor liked pages are removed because they do not contribute any useful information.

### Remove Duplicate Pages

A dictionary is created using page IDs as keys. Since dictionary keys are unique, duplicate page entries are automatically removed.

The cleaned dataset is then returned for further processing.

---

## 4. People You May Know

The `friend_suggestions()` function generates friend recommendations.

### Step 1

A dictionary is created where:

* Key → User ID
* Value → Set of friend IDs

Using sets allows fast searching and efficient comparison.

### Step 2

The function retrieves all direct friends of the selected user.

### Step 3

For every direct friend, the program examines their friends.

These are considered **friends of friends**.

### Step 4

If a friend of a friend

* is not the current user, and
* is not already a direct friend,

then that user becomes a recommendation.

### Step 5

Every occurrence increases the recommendation score.

Users having more mutual friends receive higher scores.

### Step 6

Finally, recommendations are sorted in descending order of their scores and only the user IDs are returned.

This algorithm is based on **mutual friend analysis**, which is commonly used in recommendation systems.

---

## 5. Pages You Might Like

The `pages_recomendation()` function recommends pages based on common interests.

### Step 1

A dictionary is created where

* Key → User ID
* Value → Set of liked pages

### Step 2

For every other user, the program calculates the common liked pages using the `intersection()` method.

The more pages two users have in common, the more similar they are considered.

### Step 3

The pages liked by similar users—but not already liked by the current user—are selected as recommendations.

### Step 4

Each recommendation receives a score equal to the number of shared pages.

Therefore, pages suggested by multiple similar users receive higher scores.

### Step 5

The pages are sorted according to their scores and returned as recommendations.

This follows the basic concept of **collaborative filtering**, where users with similar interests are used to recommend new content.

---

## 6. Main Program

The main section of the program controls the execution.

It performs the following operations in sequence:

1. Loads the JSON dataset.
2. Cleans the dataset.
3. Prints a confirmation message.
4. Selects a user ID for testing.
5. Generates "People You May Know" recommendations.
6. Generates "Pages You Might Like" recommendations.
7. Displays the final output.

---

## Data Structures Used

* **Dictionary** – Stores users, pages, and recommendation scores.
* **List** – Stores users, pages, and final recommendation results.
* **Set** – Removes duplicates and performs fast membership checking and intersection operations.

---

## Algorithms Used

* JSON Parsing
* Data Cleaning and Preprocessing
* Duplicate Removal
* Graph-Based Mutual Friend Recommendation
* Similarity-Based Page Recommendation
* Sorting using Recommendation Scores

---

## Time Complexity

| Function              | Complexity |
| --------------------- | ---------- |
| Load Data             | O(n)       |
| Data Cleaning         | O(n)       |
| Friend Recommendation | O(F × M)   |
| Page Recommendation   | O(U × P)   |

Where:

* **n** = Total records
* **F** = Number of direct friends
* **M** = Average friends of each friend
* **U** = Number of users
* **P** = Average liked pages per user

---

## Conclusion

This project demonstrates how recommendation systems and data analysis can be implemented using only Python's built-in libraries. It combines data preprocessing, graph traversal, similarity analysis, and ranking techniques to generate meaningful recommendations while maintaining a modular and efficient code structure.

