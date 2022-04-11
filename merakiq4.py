my_file=open("delhi.txt","x")
my_file=open("shimla.txt","x")
my_file=open("others.txt","x")
my_file=open("question3.txt","r")
for i in my_file:
        if "delhi" in i:
                f = open("delhi.txt", "a")
                f.write(i)
        elif "shimla" in i:
                g=open("shimla.txt","a")
                g.write(i)
        else:
                n=open("others.txt","a")
                n.write(i)
my_file.close()