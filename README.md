
# IntroCS-Ex12-Boggle

As part of The Hebrew University of Jerusalem course *"67101 - Introduction to Computer Science"* we have been requested to make the known Boggle game.

Boggle is a word game invented by Allan Turoff. 
For more information about the game see https://en.wikipedia.org/wiki/Boggle.

For the game instruction run the game localy.


![build](https://img.shields.io/badge/build-passing-brightgreen)

![platform](https://camo.githubusercontent.com/fb4912e741e566f3089bd8ca3561a536cc352ecfae75127d2fab3e1852e2234d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706c6174666f726d2d6c696e75782532302537432532306d61636f7325323025374325323077696e646f77732d6c6967687467726579) 

## Features

- Click and drag mechanism
- Instractions page
- Hint helper (see **API Reference** for more details)
- Cross platform

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/OrrMatzkin/IntroCS-Ex12-Boggle.git
```

Go to the project directory

```bash
  cd IntroCS-Ex12-Boggle
```

Start the game, run the *boggle.py* file

```bash
  python3 boggle.py
```

  
## Screenshots

![main Screenshot](https://github.com/OrrMatzkin/IntroCS-Ex12-Boggle/blob/main/project_extras/Screenshot%202021-10-02%20at%2022.59.41.png?raw=true)
![game Screenshot](https://github.com/OrrMatzkin/IntroCS-Ex12-Boggle/blob/main/project_extras/Screenshot%202021-10-02%20at%2023.03.16.png?raw=true)

## API Reference

**`find_length_n_words(num, board, words)`**

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `n` | `int` | **Required**. The desired word length |
|  `board` | `List[List[str]]` | **Required**. The entire letters board |
| `words` | `dict` | **Required**. The word bank |


The function can return 2 different sub-functions for finding a random hint word: a recursive function and a combinations based function.

The recursive function preforms better for higher *n* values, while the combination based function has very good performance for lower *n* values, and a very bad runtime.

**Results of our runtime analysis:**

![2 functions](https://github.com/OrrMatzkin/IntroCS-Ex12-Boggle/blob/main/project_extras/combinations_based_vs_recursive.png?raw=true)
analysis of ~300 runs of the combination based and recursive functions.

The use of 2 separate sub-functions is neccesry becuase we needed the hints words to be found in a very fast pace so the player wont feel any delay.

## Demo

![App gif](https://github.com/OrrMatzkin/IntroCS-Ex12-Boggle/blob/main/project_extras/boggle_gif.gif?raw=true)
