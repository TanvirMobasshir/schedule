import json


def user_input():
    total_courses = int(input("Total Courses: "))
    courses = {}
    for course in range(total_courses):
        course_code = input(f"Course Code({course + 1}): ")
        total_day = int(input(f"Total classes in a week of {course_code}: "))
        total_section = int(input(f"Total Section(s) of {course_code}: "))
        section_dict = {}
        for section in range(total_section):
            section_number = int(
                input(f"{section + 1}. Section number of {course_code}: "))
            days_dict = []
            for days in range(total_day):
                day = input("Day: ")
                start_time = input("Start Time: ")
                end_time = input("End Time: ")
                temp_dict = {day: [start_time, end_time]}
                days_dict.append(temp_dict)
            section_dict[section_number] = days_dict
        courses[course_code] = section_dict

    return courses


if __name__ == '__main__':

    main_dict = user_input()

    print(json.dumps(main_dict, indent=4))
