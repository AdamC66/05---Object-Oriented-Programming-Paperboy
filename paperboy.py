# Start a new project (create a new subfolder) and add a new file called "paperboy.py". Run your program and commit your work after each step.

# Each paperboy should have several attributes:
# Name
# Experience (the number of papers they've delivered)
# Earnings (amount of money they've earned)
# Every day, each paperboy is given a house number to start at and a house number to finish at. They get paid $0.25 for every paper they deliver 
# and $0.50 for every paper over their quota. If at the end of the day they haven't met their quota, they lose $2.
class Paperboy:
    def __init__(self, name, experience=0, earnings=0):
        self.name = name
        self.experience = experience
        self.earnings = earnings
        # self.house_start = house_start
        # self.house_end = house_end
# The minimum number of papers to deliver is 50. The quota is calculated as half of your experience added to the minimum. 
# So the first time a paperboy makes a delivery, the quota is 50. The next time, the quote is 50 plus half the number of papers that the 
# paperboy has delivered in the past. In this way the quota should increase after every delivery the paperboy makes.

# Each paperboy should have at least these methods:
# __str__
    def __str__(self):
        return('I\'m {}, I\'ve delivered {} papers and I\'ve earned ${} so far!'.format(self.name, self.experience, self.earnings))
# quota
# This method should calculate and return the paperboy's quota for his next delivery
    def quota(self):
        if self.experience == 0:
            return 50
        else:
            return 50 + (self.experience/2)
# deliver(self, start_address, end_address)
# This method will take two house numbers and return the amount of money earned on this delivery as a floating point number. It should also update the paperboy's experience!
    def deliver(self, start_address, end_address):
        if end_address-start_address < self.quota():
            print(f"{self.name} you did not meet your quota today, you have lost $2")
            self.earnings += (0.25*(end_address-start_address+1))
            self.earnings -= 2.0
            self.experience += (end_address-start_address+1)
        elif end_address-start_address == self.quota():
            self.earnings += (0.25*(end_address-start_address+1))
            self.experience += (end_address-start_address+1)
        else:
            self.earnings += (0.25*(end_address-start_address+1))
            self.earnings += (0.25*(end_address-start_address-self.quota()+1))
            self.experience += (end_address-start_address+1)
# Let's assume that the start_address is always a smaller number than the end_address
# As a stretch exercise you can figure out how to ensure it still works if the above assumption isn't met!
    def report(self):
        return('I\'m {}, I\'ve delivered {} papers and I\'ve earned ${} so far!'.format(self.name, self.experience, self.earnings))
# report
# This method should return a string about the paperboy's performance
# e.g. "I'm Tommy, I've delivered 90 papers and I've earned $38.25 so far!"

tommy = Paperboy('Tommy')
print(tommy.quota())
tommy.deliver(101,160)
print(tommy.earnings)
print(tommy.report())

print(tommy.quota())
tommy.deliver(1,75)
print(tommy.earnings)
print(tommy.report())





