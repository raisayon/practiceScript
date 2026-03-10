# The code above will read the data from the CSV file csv_file.txt and print the following information for each row:
# Name
# Phone number
# Role
# Example output:
# Name: Sabrina Green, Phone: 802-867-5309, Role: System Administrator
# Name: Eli Jones, Phone: 684-3481127, Role: IT specialist

import csv
 f = open("csv_file.txt")
 csv_f = csv.reader(f)
 for row in csv_f:
     name, phone, role = row
     print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()
