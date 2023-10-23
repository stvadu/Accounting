from application.db.people import get_employees
def calculate_salary(salary,db):
    print('calculating salary...')
    all_salary = salary*len(get_employees(db))
    print('calculating salary done')
    return all_salary

