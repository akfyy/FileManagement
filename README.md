
# 🗂️ Auto File Organizer (Python)

Automatically organizes files from your **Downloads** folder into categorized subfolders using Python and the `watchdog` library. The script runs in the background and detects new files or changes, then moves them into appropriate folders based on file type.

## 🛠️ Requirements

* Python 3.7+
* [watchdog](https://pypi.org/project/watchdog/)

Install with:

```bash
pip install watchdog
```

---
When you download or drop a file into your Downloads folder, the script will automatically move it to the right place.
---

## How to Use

1. Update the file paths in `FileManagement.py` to match your local directories:

```python
sourceDirectory = "C:/Users/yourname/Downloads"
dir_images = "C:/Users/yourname/Downloads/Downloaded Images"
...
```

2. Run the script:

```bash
python FileManagement.py
```

3. Download or add a new file to the source directory, the new file and the previously existing ones will get sorted automatically. 

---

## Customize

You can add support for:
* More file types (.exe, audios etc)
* Different destination folders

---


