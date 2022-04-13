import re

number_of_employee = int(input())

for _ in range(number_of_employee):
    text = input()

    pattern = r'(?P<employee_name>[A-Z][a-z]{2,}\s[A-Z][a-z]{2,})#+(?P<job_position>([A-Z][a-z]+)(\&([A-Z][a-z]+))*)\d{2}(?P<company_name>[A-Z]\w+\s(JSC|Ltd.))'

    matches = re.finditer(pattern,text)

    for match in matches:
        employee_name = match.group('employee_name')
        job_position = match.group('job_position')
        company_name = match.group('company_name')
        if '&' in job_position:
            job_position = job_position.replace('&',' ')
            print(f"{employee_name} is {job_position} at {company_name}")
        else:
            print(f"{employee_name} is {job_position} at {company_name}")

dict(name='aasd', age=22)
