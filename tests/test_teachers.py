from src.teachers import add_teacher, find_teacher, get_teachers


def test_get_teachers_returns_list():
    teachers = get_teachers()
    assert isinstance(teachers, list)
    assert len(teachers) >= 3


def test_find_teacher_by_name():
    result = find_teacher("Айдос")
    assert len(result) == 1
    assert result[0]["subject"] == "Ақпараттық жүйелер"


def test_add_teacher():
    teacher = add_teacher("Саят Омаров", "DevOps")
    assert teacher["name"] == "Саят Омаров"
    assert teacher["subject"] == "DevOps"
