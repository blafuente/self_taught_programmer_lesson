# st = open("st.txt","w")
# st.write("hi from python")
# st.close()

# with open([file_path],[ mode]) as [variable_name]:
#     [your_code]

# To write a file
# with open("st.txt","w") as f:
#     f.write("hi from Python!")

#To read a file
# with open("st.txt","r") as f:
#     print(f.read())

# import csv
# with open("C:/Users/loulafuente/Developement/selfTaughtProgram/st.csv","w")
#     write = csv.writer(f,delimiter=",")
#     write.wrtierwo(["one","two","three"])
#     write.writerow(["four","five","six"])

import csv 
with open("st.csv", "w") as f:
    write = csv.writer(f,delimiter=",")
    write.writerow(["one","two","three"])
    write.writerow(["four","five","six"])

with open("st.csv", "r") as f:
    r = csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))