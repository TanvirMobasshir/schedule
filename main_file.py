import json
# from datetime import datetime


if __name__ == '__main__':

    total_courses = int(input("Total Courses: "))
    courses = {}
    for course in range(total_courses):
        course_code = input(f"Course Code({course + 1}): ")
        total_day = int(input(f"Total classes in a week of {course_code}: "))
        total_section = int(input(f"Total Section of {course_code}: "))
        section_dict = {}
        for section in range(total_section):
            section_number = int(input(f"{section+1}. Section number of {course_code}: "))
            days_dict = {}
            for days in range(total_day):
                day = input("Day: ")
                start_time = input("Start Time: ")
                end_time = input("End Time: ")
                days_dict[day] = [start_time, end_time]
            section_dict[section_number] = days_dict
        courses[course_code] = section_dict

    print(json.dumps(courses, indent=4))
