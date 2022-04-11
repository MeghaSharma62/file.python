my_file=open("file-questions3.txt","w")
# my_file.write()

banks_list = ["Kotak","\n","HDFC","\n","RBL","\n","SBI","\n","Bank of Baroda"]
i=0
while i<len(banks_list):
        # print(banks_list[i])
        # i+=1
        my_file.write(banks_list[i])
        my_file.write('/n')
        i+=1
my_file.close()
