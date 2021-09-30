import json

course1 = {
    'code': 'CSE251',
    'section1': {
        'sec_num': 2,
        'day1': {
            'day': 'mon',
            'start': 11.40,
            'end': 1.20
        },
        'day2': {
            'day': 'wed',
            'start': 11.40,
            'end': 1.20
        },
        'day3': {
            'day': 'thur',
            'start': 4.50,
            'end': 6.50
        }
    },
    'section2': {
        'sec_num': 2,
        'day1': {
            'day': 'mon',
            'start': 11.40,
            'end': 1.20
        },
        'day2': {
            'day': 'wed',
            'start': 11.40,
            'end': 1.20
        },
        'day3': {
            'day': 'thur',
            'start': 4.50,
            'end': 6.50
        }
    }
}


if __name__ == '__main__':

    course_number = int(input())
    courses = []
    for i in range(course_number):
        course_code = input("Course Code: ")
        courses.append({course_code: course1})

    print(json.dumps(courses, indent=4))
