#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def show(ab) :
    print("student",'\t',"Name",'\t',"Midterm",'\t',"Final",'\t',"Average","Grade")
    print("----------------------------------------------------------------")
    for i in ab : 
        print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5])
        

def search(stu_list):
    c = input("Student ID:")
    n = 0
    for i in range(len(stu_list)):
        if c in stu_list[i][0] :       
            print("Student ID : %s"%c)
            print("----------------------------------------------------------------")
            print(stu_list[i][0],'\t',stu_list[i][1],'\t',stu_list[i][2],'\t',stu_list[i][3],'\t',stu_list[i][4],'\t',stu_list[i][5])     
            n += 1
            break
    if n == 0:
        print("NO SUCH PERSON")
        
        
        
def calc(avg):
    if avg>= 90:
        return 'A'
    elif avg>=80:
        return 'B'
    elif avg>=70:
        return 'C'
    elif avg>=60:
        return 'D'
    else:
        return 'F'
        


def changescore(stu_list):
    
    aa = input("Student ID :")
    
    for i in range (len(stu_list)):
        if (aa not in stu_list[i][0]):
            print("NO SUCH PERSON.")
        else:

            e = input("Mid/Final?").upper()
            if e == "MID" :
                ns = int(input("Input new score:"))
                if (ns>100 or ns<0) :
                    print(" ") 
                    break
                else : 
                    print_bar()
                    print(stu_list[i][0],'\t',stu_list[i][1],'\t',stu_list[i][2],'\t',stu_list[i][3],'\t',stu_list[i][4],'\t',stu_list[i][5])
                    stu_list[i][2] = ns
                    print("score changed.")
                    stu_list[i][4]=(stu_list[i][2]+stu_list[i][3])/2
                    stu_list[i][5]=calc(stu_list[i][4])
                    print(stu_list[i][0],'\t',stu_list[i][1],'\t',stu_list[i][2],'\t',stu_list[i][3],'\t',stu_list[i][4],'\t',stu_list[i][5])
                    break

            elif e == "FINAL" :
                ns = int(input("Input new score:"))
                if (ns>100 or ns<0) :
                    print(" ") 
                    break
                else : 
                    print_bar()
                    print(stu_list[i][0],'\t',stu_list[i][1],'\t',stu_list[i][2],'\t',stu_list[i][3],'\t',stu_list[i][4],'\t',stu_list[i][5])
                    stu_list[i][3] = ns
                    print("score changed.")
                    stu_list[i][4]=(stu_list[i][2]+stu_list[i][3])/2
                    stu_list[i][5]=calc(stu_list[i][4])
                    print(stu_list[i][0],'\t',stu_list[i][1],'\t',stu_list[i][2],'\t',stu_list[i][3],'\t',stu_list[i][4],'\t',stu_list[i][5])
                    break
            else :
                print("  ")
                break
                
def print_bar():
    print("student",'\t',"Name",'\t',"Midterm",'\t',"Final",'\t',"Average","Grade")
    print("----------------------------------------------------------------")
                    
                
def add(stu_list):

    length = len(stu_list)
    ff = input("Student ID:")
    
    tmp=[]
    
    for i in range(len(stu_list)):
            tmp.append(stu_list[i][0])
    
    if ff in tmp:
        print("ALREADY EXISTS.")
        
    else:
        stu_list.append([])
        stu_list[length].append(ff) 
        stu_list[length].append(input("Name"))
        stu_list[length].append(int(input("Midterm Score")))
        stu_list[length].append(int(input("Final Score")))
        print("Student added.")


        stu_list[length].append((stu_list[length][2]+stu_list[length][3])/2)
        avg = stu_list[length][4]

        stu_list[length].append(calc(avg))                

        
def searchgrade(stu_list):
    list = ["A","B","C","D","F"]
    cc = input("Grade to search:")
    
    tmp=[]
    for i in range(len(stu_list)):
        tmp.append(stu_list[i][5])
    
    if cc not in list:
        print("")
        return
    
    if cc not in tmp:
        print("NO RESULTS.")

    
    
    print("student",'\t',"Name",'\t',"Midterm",'\t',"Final",'\t',"Average","Grade")
    print("----------------------------------------------------------------")
    
    for i in range(len(stu_list)):
        if cc in stu_list[i][5] :       
            
            print(stu_list[i][0],'\t',stu_list[i][1],'\t',stu_list[i][2],'\t',stu_list[i][3],'\t',stu_list[i][4],'\t',stu_list[i][5])             
        

def remove(stu_list):
    m = 0
    delist = []
    delnum = input("Student ID:")
    for i in range(len(stu_list)):
        if delnum == stu_list[i][0]:
            m += 1
            delist.append(i)
    if m == 1:
        stu_list.remove(stu_list[delist[0]])
        print("Student removed.")
    else :
        print("NO SUCH PERSON.")
    if len(stu_list) == 0:
        print("List is empty.")        
        
        
def quit(stu_list):
    a = input("Save data?[yes/no]")
    
    if a == "yes" :
        file_name = input("File name")
        f = open(file_name,"w")
        
        for i in range(len(stu_list)):
            data = str(stu_list[i][0])+"\t"+stu_list[i][1]+"\t"+str(stu_list[i][2])+"\t"+str(stu_list[i][3])+"\n"
            f.write(data)
        f.close()
        return 0
    
    else :
        return  0       
        

def main():
    
    stu_list = []
    f = open("students.txt","r")

    data = f.readlines()
    for i in data:
        stu_list.append(i.strip().split("\t"))


    for i in range(5):
        stu_list[i][2]=int(stu_list[i][2])
        stu_list[i][3]=int(stu_list[i][3])
        stu_list[i].append((stu_list[i][2]+stu_list[i][3])/2)

        avg = stu_list[i][4]

        if avg>= 90:
            grade = 'A'
        elif avg>=80:
            grade = 'B'
        elif avg>=70:
            grade = 'C'
        elif avg>=60:
            grade = 'D'
        else:
            grade = 'F'

        stu_list[i].append(grade)

    stu_list.sort(key = lambda e : e[4], reverse = True)
    show(stu_list)
    
    bool_re = 1
    while bool_re==1:
        order = input("").upper()
        if order == "SHOW": show(stu_list)
            
        elif order == "SEARCH": search(stu_list)
            
        elif order == "CHANGESCORE": changescore(stu_list)
            
        elif order == "SEARCHGRADE": searchgrade(stu_list)
            
        elif order == "ADD": add(stu_list)
            
        elif order == "REMOVE": remove(stu_list)
            
        elif order == "QUIT": 
            bool_re = quit(stu_list)
            
        else :
             print(" ")
                
                
                
                
                
if __name__ == '__main__':
    main()

