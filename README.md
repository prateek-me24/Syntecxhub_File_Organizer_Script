## Syntecxhub_File_Organizer_Script

Task 2 Project 3


----------------------------------------------------------------------

## File Organizer Script (Python Automation)

A Python automation tool that scans a folder and organizes files into subfolders based on their file extensions.  
It supports name collision handling, dry-run mode, logging, and can be scheduled to run automatically using
Windows Task Scheduler.

This project is perfect for desktop cleanup and demonstrates real-world Python automation skills.

---

## Features

-  Organizes files by extension (PDF, JPG, MP3, TXT, etc.)
-  Handles duplicate file names safely (`file_1.txt`, `file_2.txt`, …)
-  Dry-run mode to preview actions without moving files
-  Logs all actions into a log file
-  Can be scheduled using Windows Task Scheduler for full automation

---

## Example

### Before:

-  test_files/
    -  resume.pdf
    -  photo.jpg
    -  song.mp3

### After:

-  test_files/
    -  PDF/
        -  resume.pdf
    -  JPG/
        -  photo.jpg
    -  MP3/
        -  song.mp3

---

## Technologies Used

-  Python
-  os module
-  shutil module
-  logging module
-  Windows Task Scheduler

---

## How to Run

1. Clone this repository:
```bash
git clone https://github.com/prateek-me24/Syntecxhub_File_Organizer_Script.git
```

2. Navigate into the folder:
cd Syntecxhub_File_Organizer_Script

3. Run the script:
python main.py

---

## Dry Run Mode

Dry-run shows what would happen without actually moving files.

Set:
    DRY_RUN = True

Output:
    [DRY RUN] Would move: resume.pdf -> PDF/resume.pdf

---

## Logging

All actions are saved in:

    file_organizer.log

Example:
    2026-01-29 22:41:10 - Moved: photo.jpg -> JPG/photo.jpg

---

## Scheduling With Windows Task Scheduler

1. Open Task Scheduler
2. Click Create Basic Task
3. Choose Trigger: Daily
4. Action: Start a Program
5. Program:
    D:\Path\To\Python\python.exe
6. Arguments
    D:\Path\to\main.py
7. Start in:
    D:\Path\to\ProjectFolder

Test anytime by:
    Right Click Task -> Run

---

## Main Focus of This Project

Key areas covered in this project

-  File organization automation using Python
-  Working with the file system (os and shutil)
-  Preventing data loss with dry-run functionality
-  Maintaining logs for transparency and debugging
-  Scheduling scripts for automatic execution

Best suited for:

-  Python learners and interns
-  Automation and scripting practice
-  Real-life desktop cleanup use cases

------------------------------------------------------------------

### Author

# NAME - PRATEEK METHWANI
# Python & Automation Enthusiast
