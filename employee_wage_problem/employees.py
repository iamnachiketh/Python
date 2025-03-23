import random

class Employee:
    FULL_TIME_HOURS = 8
    PART_TIME_HOURS = 4
    WAGE_PER_HOUR = 20
    WORKING_DAYS_PER_MONTH = 20
    MAX_WORKING_HOURS = 100

    def __init__(self, name):
        self.name = name
        self.total_wage = 0
        self.total_working_days = 0
        self.total_working_hours = 0

    def check_attendance(self):
        return random.choice(["Present", "Absent", "Part-time"])

    def calculate_daily_wage(self, hours):
        return hours * self.WAGE_PER_HOUR

    def get_work_hours(self, attendance):
        if attendance == "Present":
            return self.FULL_TIME_HOURS
        elif attendance == "Part-time":
            return self.PART_TIME_HOURS
        else:
            return 0


    def get_wage_for_day(self, attendance):
        switch = {
            "Present": self.FULL_TIME_HOURS,
            "Part-time": self.PART_TIME_HOURS,
            "Absent": 0
        }
        hours = switch.get(attendance, 0)
        return self.calculate_daily_wage(hours)


    def calculate_monthly_wage(self):
        for day in range(1, self.WORKING_DAYS_PER_MONTH + 1):
            attendance = self.check_attendance()
            hours = self.get_work_hours(attendance)
            daily_wage = self.calculate_daily_wage(hours)

            print(f"Day {day}: {attendance} - Hours: {hours} - Wage: ${daily_wage}")
            
            self.total_wage += daily_wage
            self.total_working_days += 1
            self.total_working_hours += hours

        print("\nMonthly Summary:")
        print(f"Total Wage: ${self.total_wage}")
        print(f"Total Working Days: {self.total_working_days}")
        print(f"Total Working Hours: {self.total_working_hours}\n")


    def calculate_wage_till_condition(self):
        self.total_wage = 0
        self.total_working_days = 0
        self.total_working_hours = 0

        while self.total_working_days < self.WORKING_DAYS_PER_MONTH and self.total_working_hours < self.MAX_WORKING_HOURS:
            attendance = self.check_attendance()
            hours = self.get_work_hours(attendance)
            
            if self.total_working_hours + hours > self.MAX_WORKING_HOURS:
                hours = self.MAX_WORKING_HOURS - self.total_working_hours

            daily_wage = self.calculate_daily_wage(hours)

            print(f"Day {self.total_working_days + 1}: {attendance} - Hours: {hours} - Wage: ${daily_wage}")

            self.total_wage += daily_wage
            self.total_working_days += 1
            self.total_working_hours += hours

        print("\nCondition Summary:")
        print(f"Total Wage: ${self.total_wage}")
        print(f"Total Working Days: {self.total_working_days}")
        print(f"Total Working Hours: {self.total_working_hours}")



emp = Employee("John Doe")

print("\n Monthly Wage Calculation:")
emp.calculate_monthly_wage()

print("\nWage Calculation till Condition Reached:")
emp.calculate_wage_till_condition()
