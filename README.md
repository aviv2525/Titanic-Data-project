# 🚢 Titanic-Data-project

A Python-based interactive ticket system for the Titanic, built using real passenger data. The system validates user input, assigns a ticket class based on fare, generates a unique ticket, saves it to a file, and calculates the user's survival chances based on historical data.

---

## 📋 Features

- Input validation for name, age, fare, and sex
- Automatic ticket class assignment (1st, 2nd, or 3rd) based on fare ranges derived from real data
- Unique 6-digit ticket number generation
- Ticket saved to a formatted `.txt` file
- Survival probability calculation based on passenger class and sex

---

## 🗂️ Project Structure

```
Titanic-Data-project/
│
├── titanic.py        # Main script
├── titanic.csv       # Dataset
├── ticket.txt        # Generated ticket (created on run)
└── README.md
```

---

## ▶️ How to Run

1. Make sure you have Python 3 and pandas installed:
   ```bash
   pip install pandas
   ```

2. Place `titanic.csv` in the same directory as `titanic.py`

3. Run the script:
   ```bash
   python titanic.py
   ```

---

## 📥 Input

The program prompts the user for the following:

| Field | Type   | Validation                                      |
|-------|--------|-------------------------------------------------|
| Name  | String | Stripped of leading/trailing spaces             |
| Age   | Float  | Must be between 0 and 130                       |
| Fare  | Float  | Must be between the min and max fare in dataset |
| Sex   | String | Must be `male` or `female`                      |

---

## 🎫 Ticket Output

A formatted ticket is saved to `ticket.txt`. Example:

```
 ----------------------------------------------------------- 
 | ticket: 482910         |   fare: 27                     |
 ----------------------------------------------------------- 
 | age: 24                |   class: 2                     |
 ----------------------------------------------------------- 
 | sex: male              |   name: John Smith             |
 ----------------------------------------------------------- 
```

---

## 📊 Survival Chances

After generating the ticket, the program calculates the survival rate of passengers with the same class and sex from the dataset, and displays:

```
Dear John, your chances to die on our trip are 83.0%. Enjoy your trip 😊
```

---

## 📁 Dataset

The project uses the [Titanic dataset](https://www.kaggle.com/datasets/brendan45774/test-file), which contains real passenger information including class, fare, sex, age, and survival status.

---

## 🛠️ Requirements

- Python 3.x
- pandas
