# Domowa biblioteczka/Home library
Simple API project to view and update the home book inventory. 


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)



## General Information
The purpose of the project is to store data of books in home bookcase. It provides such information as book title, author, genre, number of pages and whether the book is already read. The user can add new book and update or remove existing element.


## Technologies Used
- Python - version 3.10



## Features
- Viewing book resource
- Adding new element
- Updating exisitng element
- Removing existing element

## Setup
Project requirements included in respository as 'requirements.txt'.


## Usage
Code examples:
- view content: 

```python
GET http://localhost/api/v1/library
Content-Type: application/json
```

- add new book:

```python
POST http://localhost/api/v1/library/
Content-Type: application/json

{
    "title": "Ostatnie życzenie",
    "author": "Sapkowski",
    "genre": "Fantastyka",
    "pages": 332
}
```

- update book with adequate id:

```python
PUT http://localhost/api/v1/library/1
Content-Type: application/json
{
    "author": "Andrzej Sapkowski"
}
```
- delete book with adequate id:

```python
DELETE http://localhost/api/v1/library/4
Content-Type: application/json
```














<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
