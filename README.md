# 📝 To-Do CLI App with JSON, Colorama & Timestamps

A beginner-friendly yet feature-rich **Python CLI To-Do List App** built as part of my #50DaysOfPython challenge (Day 2). It supports colored output in the terminal, timestamped tasks, and stores data persistently in a JSON file.

## 📌 Features

- ✅ Add new tasks with timestamps
- 🗂️ View all tasks (completed/pending)
- 🟢 Mark tasks as complete
- 🧠 Colored CLI output using `colorama`
- 💾 Save and load tasks using `JSON`
- ⏳ Timestamp support for every task added

---

## 🛠️ Modules Used

- `colorama` – for colored terminal output  
- `json` – for storing and reading data  
- `datetime` – for timestamps  
- `os` – for checking if data file exists


## 📷 Demo (CLI Preview)

```bash
$ python todo.py
📝 Welcome to Your To-Do List
----------------------------------
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Exit
```
## 🗃 Sample data.json
```bash
[
  {
    "task": "Finish Python homework",
    "timestamp": "2025-08-05 16:30:22",
    "completed": false
  },
  {
    "task": "Read about JSON handling",
    "timestamp": "2025-08-05 17:20:11",
    "completed": true
  }
]
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/sunil-rajpurohit/todo-cli-json-colorama.git
cd todo-cli-json-colorama


```

### 2. Install Dependencies
```bash
pip install colorama
```

## 🤝 Contributing
This is a beginner project for learning purposes. Feel free to fork, modify, and create pull requests if you want to improve or add features.

## 👨‍💻 Author
Sunil Rajpurohit
Python Enthusiast | Aspiring Developer
Follow my journey on [LinkedIn](www.linkedin.com/in/sunil-rajpurohit)

## 💬 Developer Note
This project was NOT easy. I got stuck multiple times.
It took over 5 hours, many errors, and loads of Googling — but that’s the beauty of learning.
If you're reading this and struggling too, just keep going. We all start somewhere
