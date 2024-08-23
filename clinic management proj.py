import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Lochana81#",database="clinic")
cursor=con.cursor()
def appointment():
     d=input("enter date of appointment(dd/mm/yyyy)")
     t=input("enter time of appointment(hour:minute)")
     dd=input("enter department of doctor")
     print("appointment booked")
def patients():
     pid=int(input("enter the ID of the patient"))
     pname=input("enter the name of the patient")
     y=pname.replace(" ","")
     n=y.isalpha()
     while n==False:
         print("name invalid")
         pname=input("enter the name of the patient")
         n=pname.isalpha()
     page=int(input("enter the age of the patient"))
     while page<0 or page>120:
         print("age invalid")
         page=int(input("enter the age of the patient"))
     pwt=float(input("enter the weight of patient in kg"))
     pht=float(input("enter the height of patient in ft"))
     pprob=input("brief description of problem faced by patient")
     pphno=input("enter the phone number of patient")
     l=len(pphno)
     while l!=10:
         print("phone no invalid")
         pphno=input("enter the phone number of patient")
         l=len(pphno)
     pbg=input("enter the bloodgroup of patient")
     s1="INSERT INTO patients(pid,pname,page,pwt,pht,pprob,pphno,pbg) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
     v1=(pid,pname,page,pwt,pht,pprob,pphno,pbg)
     cursor.execute(s1,v1)
     con.commit()
     print("data entered successfully")
def doctors():
     did=int(input("enter the ID of the doctor"))
     dname=input("enter the name of the doctor")
     n=dname.isalpha()
     while n==False:
         print("name incorrect")
         dname=input("enter the name of the doctor")
         n=dname.isalpha()
     ddept=input("enter the name of the department")
     x=ddept.isalpha()
     while x==False:
         print("name incorrect")
         ddept=input("enter the name of the department")
         x=ddept.isalpha()
     dtime=input("enter the time doctor is available(hours:mins")
     dphno=input("phone number of doctor")
     l=len(dphno)
     while l!=10:
         print("phone no invalid")
         pphno=input("enter the phone number of doctor")
         l=len(dphno)
     s2="INSERT INTO doctors(did,dname,ddept,dtime,dphno) VALUES(%s,%s,%s,%s,%s)"
     v2=(did,dname,ddept,dtime,dphno)
     cursor.execute(s2,v2)
     con.commit()
     print("data entered successfully")
def update():
    c=input("enter whose details should we update(doctors/patients)")
    if c=="patients":
        i1=int(input("enter the patient id of the patient whose details are to edited"))
        a=input("enter the detail to be edited(age,wt,ht,phno)")
        if a=="age":
            npage=int(input("enter updated age of the patient"))
            s="UPDATE patients SET page={} WHERE pid={}".format(npage,i1)
            cursor.execute(s)
            con.commit()
        elif a=="wt":
            npwt=float(input("enter updated weight of patient"))
            s="UPDATE patients SET pwt={} WHERE pid={}".format(npwt,i1)
            cursor.execute(s)
            con.commit()
        elif a=="ht":
            npht=float(input("enter updated height of patient"))
            s="UPDATE patients SET pht={} WHERE pid={}".format(npht,i1)
            cursor.execute(s)
            con.commit()
        elif a=="phno":
            npphno=int(input("enter updated phone number of patient"))
            s="UPDATE patients SET pphno={} WHERE pid={}".format(npphno,i1)
            cursor.execute(s)
            con.commit()
        else:
            print("invalid choice")
    elif c=="doctors":
        i2=int(input("enter the doctor id of the doctor whose details are to edited"))
        b=input("enter the detail to be edited(dphno)")
        if b=="dphno":
            ndphno=int(input("enter updated phone number of doctor"))
            t="UPDATE doctors SET dphno={} WHERE did={}".format(ndphno,i2)
            cursor.execute(t)
            con.commit()
        else:
            print("invalid choice")
def displaydoc():
     q="select * from doctors"
     cursor.execute(q)
     data=cursor.fetchall()
     print("DOCTOR DETAILS")
     for i in data:
         print("doctorid:",i[0],"\ndoctor name:",i[1],"\ndoctor department:",i[2],"\ndoctor's available time:",i[3],"\nphone number",i[4])
         print("______________________________________________________________________________________________________________________________________________________")
def displaypat():
     q="select * from patients"
     cursor.execute(q)
     data=cursor.fetchall()
     print("PATIENT DETAILS")
     for i in data:
         print("patientid:",i[0],"\npatient name:",i[1],"\npatient age:",i[2],"\npatient weight:",i[3],"\npatient height",i[4],"\nbrief problem description:",i[5],"\nphone number:",i[6],"\nblood group:",i[7])
         print("____________________________________________________________________________________________________________________________________________________")
while True:
     print("1:book appointment\n2:enter patients details\n3:enter doctor details\n4:update patient/doctor details\n5.display doctor details\n6.display patient details\n7.exit")
     ch=int(input("enter your choice"))
     if ch==1:
          appointment()
     elif ch==2:
          patients()
     elif ch==3:
          doctors()
     elif ch==4:
          update()
     elif ch==5:
          displaydoc()
     elif ch==6:
          displaypat()
     elif ch==7:
          break
     else:
          print("invalid choice")
con.close()
