## Student Record Management System  
*A simple CLI tool written in plain Python*

---

### ✨ Features
| Action | What it does |
|--------|--------------|
| **Add**    | Store a new student’s **Name**, **ID**, **Department**, and **CGPA** |
| **Read**   | List all saved student records in a neat table |
| **Update** | Edit any field (Name / ID / Dept / CGPA) for an existing student |
| **Delete** | Remove a student’s record by ID |

---



### 🚀 Quick start
1. **Clone**
   ```bash
   git clone https://github.com/Somaiya-0/Python_Learning.git
   cd Python-Learning/Student_record_management_system

   ```

2. **Run**
   ```bash
   python simple_student_record_management.py
   ```

3. **Follow the menu** – choose **A**dd, **R**ead, **U**pdate, or **D**elete when prompted.

---
### Inside the code (quick view)
* **Data store** – a plain Python list held in memory while the script runs.  
* **Menu loop** – keeps asking for a choice until you quit.  
* **Functions** – `add_student()`, `show_record()`, `update_student()`, `delete_student()` keep things tidy.  
* **Validation** – basic checks for unique ID and CGPA in the 0–4 range (edit as you like).

---

### 📚 Example session
```
======== Student Record Management System ========
1. Add Student Record
2. Show Students Record
3. Show specific student's record
4. Update record of a student
5. Delete rocord of a student
6. Exit

Enter your choice (1-6): 1


-------- Adding student's information to the record --------
Enter student name : Somaiya
Enter Somaiya's id : 10
Emter Somaiya's department: CSE
Enter Somaiya's cg : 3.95
Record for Somaiya has been added.
Add more student?(y/n) : n

Enter your choice (1-6): 2


-------- Showing Record --------
+---------+-------+-------+------+
| Name    | ID    | Dept  | CGPA |
+---------+-------+-------+------+
| Somaiya | 10    | CSE   | 3.95 |
+---------+-------+-------+------+

Enter your choice (1-6): 6
Program Finished!
```
