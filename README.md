# 🍽️ Restaurant Recommendation System

A simple command-line Python project that recommends restaurants based on the user's input of a food type.

---

## 🛠️ Project Structure
```
script.py                     # Main script
restaurantData.py             # Restaurant dataset
README.md                     # Project overview
LICENSE                       # MIT License file
```

## 🚀 Features

- Users can type in the beginning of a food type (e.g., "t" for "Thai", "i" for "Italian", and so on)  
- The script matches user input with available food types
- If there's more than one match, it prompts the user to narrow it down
- Once a match is found, it displays a list of relevant restaurant recommendations, if the user chooses to see this list

---

## 🧠 How It Works

- The program uses a list of food types and restaurants stored in a dataset.
- It uses user input to search for matches based on the beginning of a food type.
- Input and matches are case-insensitive.
- Matching results are printed to the terminal.

---

## 📦 Requirements

This project uses **only standard Python libraries**, so no extra installation is needed.

- Python 3.6+

---

## ▶️ How to Run

```bash
python script.py
```
---

## 📫 Contact
Created by Patrick Nguyen

---

## 🪪 License
This project is licensed under the MIT License.\
See the [LICENSE](./LICENSE) file for details.