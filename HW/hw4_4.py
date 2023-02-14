def get_grade(key):
    grades_five = {
        "F": 1,
        "FX": 2,
        "E": 3,
        "D": 3,
        "C": 4,
        "B": 5,
        "A": 5,
    }
    print(grades_five.get(key, None))
    # for grad, five in grades_five.items():
    #     if key in grad:
    #         return five


def get_description(key):
    grades_expl = {
        "F": "Unsatisfactorily",
        "FX": "Unsatisfactorily",
        "E": "Enough",
        "D": "Satisfactorily",
        "C": "Good",
        "B": "Very good",
        "A": "Perfectly",
    }
    print(grades_expl.get(key, None))
    # for grad, expl in grades_expl.items():
    #     if key in grad:
    #         return expl


get_grade("FX")
get_description("A")
