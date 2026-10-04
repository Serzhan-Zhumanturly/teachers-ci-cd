"""Simple teacher list application for DevOps coursework."""

teachers = [
    {"id": 1, "name": "Айдос Қасымов", "subject": "Ақпараттық жүйелер"},
    {"id": 2, "name": "Меруерт Сәрсенова", "subject": "Бағдарламалау"},
    {"id": 3, "name": "Ерлан Нұрбеков", "subject": "Деректер базасы"},
]


def get_teachers():
    """Return all teachers."""
    return teachers.copy()


def find_teacher(name):
    """Find teachers whose name contains the given text."""
    return [teacher for teacher in teachers if name.lower() in teacher["name"].lower()]


def add_teacher(name, subject):
    """Add a new teacher and return the created record."""
    teacher = {
        "id": len(teachers) + 1,
        "name": name,
        "subject": subject,
    }
    teachers.append(teacher)
    return teacher
