#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *

root=Tk()

width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

#FRAME 1 AKA HEADING 
frame1=Frame(root,bd=9,bg="coral",relief=RIDGE)
frame1.grid(row=0,column=0)
titlelabel=Label(frame1,text="BUDGET MANAGER",bg="#CCCCFF").grid(row=0,column=0,columnspan=5)


# FRAME 2
#sources of revenue
frame2=Frame(root,bd=7,bg="#D5A5FB",relief=RIDGE)
frame2.grid(row=1,column=0)

label1=Label(frame2,text="sources of revenue ",padx=160).grid(row=0,column=0,columnspan=4)
list1=["income","sidehustle","add_revenue"] 
count=1
list2=[]
for i in range(len(list1)):
    a="l_"+list1[i]
    b="e_"+list1[i]
    a=Label(frame2,text=list1[i]).grid(row=count,column=0)
    b=Entry(frame2,width=50)
    b.grid(row=count,column=1,columnspan=2)
    list2.append(b)
    count+=1   
l=Label(frame2,text="total: 0000000 " ,padx=30).grid(row=4,column=2)

#computing sum 
def sumrevenue():
    sumrev=0
    for i in list2:
        d=i.get()
        sumrev+=int(d)
    l=Label(frame2,text="total: " +str(sumrev),padx=30).grid(row=4,column=2)
b_totalrevenue=Button(frame2,text="submit",command=sumrevenue,padx=40,bg="#A8F847")
b_totalrevenue.grid(row=4,column=1)


#FRAME 3
frame3=Frame(root,bd=7,bg="#D5A5FB",relief=RIDGE)
frame3.grid(row=2,column=0)
label1=Label(frame3,text="expenditure ",padx=180).grid(row=0,column=0,columnspan=5)


dictexp={"household bills":0,"living costs":0,"banking":0,"children & pets":0,"leisure spending":0}


        #function1 household bills 
def func1():
    whb=Toplevel()
    whb.geometry('440x220+0+253')
    
    listhb1=["rent", "maintenance","insurance","car","electricity","water","phone","internet","additional"]
    count=0
    listhb2=[]
    for i in range(len(listhb1)):
            a=Label(whb,text=listhb1[i]).grid(row=count,column=0)
            b=Entry(whb,width=50)
            b.grid(row=count,column=1,columnspan=2)
            listhb2.append(b)
            count+=1
    sum_hb=Label(whb,text="total: 0000000 " ,padx=30).grid(row=count,column=2)
    def sumhousehold():
            sumhb=0
            for b in listhb2:
                d=b.get()
                sumhb+=int(d)
            dictexp.update({"household bills":sumhb})
            l=Label(whb,text="total: " +str(sumhb),padx=30).grid(row=count,column=2)
    b_totalhousehold=Button(whb,text="submit",command=sumhousehold,padx=40,bg="#A8F847")
    b_totalhousehold.grid(row=count,column=1)
    

            #function2 living costs 

def func2():
    wlc=Toplevel()
    wlc.geometry('440x220+0+253')
    listlc1=["groceries","laundry","clothes","toiletries","health","medicines","heathcare","domestic_help","additional"]
    count=0
    listlc2=[]
    for i in range(len(listlc1)):
            a=Label(wlc,text=listlc1[i]).grid(row=count,column=0)
            b=Entry(wlc,width=50)
            b.grid(row=count,column=1,columnspan=2)
            listlc2.append(b)
            count+=1
    sum_lc=Label(wlc,text="total: 0000000 " ,padx=30).grid(row=count,column=2)
    
    def sumlivingcost():
            sumlc=0
            for b in listlc2:
                d=b.get()
                sumlc+=int(d)
            dictexp.update({"living costs":sumlc})
            l=Label(wlc,text="total: " +str(sumlc),padx=30).grid(row=count,column=2)
    b_totallivingcost=Button(wlc,text="submit",command=sumlivingcost,padx=40,bg="#A8F847")
    b_totallivingcost.grid(row=count,column=1)
    
                         #function3 banking

def func3():
    wbk=Toplevel()
    wbk.geometry('440x220+0+253')
    listbk1=["bank_account_fees","loan","credit_card_payment","additional"]
    count=0
    listbk2=[]
    for i in range(len(listbk1)):
            a=Label(wbk,text=listbk1[i]).grid(row=count,column=0)
            b=Entry(wbk,width=50)
            b.grid(row=count,column=1,columnspan=2)
            listbk2.append(b)
            count+=1


    sum_lc=Label(wbk,text="total: 0000000 " ,padx=30).grid(row=count,column=2)
    def sumbank():
            sumbk=0
            for b in listbk2:
                d=b.get()
                sumbk+=int(d)
            dictexp.update({"banking":sumbk})
            l=Label(wbk,text="total: " +str(sumbk),padx=30).grid(row=count,column=2)
    b_totalbank=Button(wbk,text="submit",command=sumbank,padx=40,bg="#A8F847")
    b_totalbank.grid(row=count,column=1)
    
                         #function4 children and pets 

def func4():
    wch=Toplevel()
    wch.geometry('440x220+0+253')
    listch1=["childcare","school_fees","club_activities","toy","babysitting","vet","pet_insurance","additional"]
    count=0
    listch2=[]
   
    for i in range(len(listch1)):
            a=Label(wch,text=listch1[i]).grid(row=count,column=0)
            b=Entry(wch,width=50)
            b.grid(row=count,column=1,columnspan=2)
            listch2.append(b)
            count+=1


    sum_ch=Label(wch,text="total: 0000000 " ,padx=30).grid(row=count,column=2)
    def sumchild():
            sumch=0
            for b in listch2:
                d=b.get()
                sumch+=int(d)
            dictexp.update({"children & pets":sumch})
            l=Label(wch,text="total: " +str(sumch),padx=30).grid(row=count,column=2)
    b_totalchild=Button(wch,text="submit",command=sumchild,padx=40,bg="#A8F847")
    b_totalchild.grid(row=count,column=1)
    
    
                     #function5 liesure spending  

def func5():
    wli=Toplevel()
    wli.geometry('440x220+0+253')
    listli1=["hobbies","day_outs","cinema","books_and_games","newsletter","birthdays","festive_spending","holidays"]
    count=0
    listli2=[]
    for i in range(len(listli1)):
            a=Label(wli,text=listli1[i]).grid(row=count,column=0)
            b=Entry(wli,width=50)
            b.grid(row=count,column=1,columnspan=2)
            listli2.append(b)
            count+=1
    sum_ch=Label(wli,text="total: 0000000 " ,padx=30).grid(row=count,column=2)
    def sumliesure():
            sumli=0
            for b in listli2:
                d=b.get()
                sumli+=int(d)
            dictexp.update({"leisure spending":sumli})
            l=Label(wli,text="total: " +str(sumli),padx=30).grid(row=count,column=2)
    b_totalliesure=Button(wli,text="submit",command=sumliesure,padx=40,bg="#A8F847")
    b_totalliesure.grid(row=count,column=1)
    
    
    
    
        #expenditure buttons for the 5 above functions
        
b_housebill=Button(frame3,text="household bills",command=func1)
b_housebill.grid(row=1,column=0)
b_livingcost=Button(frame3,text="living cost ",command=func2)
b_livingcost.grid(row=1,column=1)
b_bank=Button(frame3,text="banking ",command=func3)
b_bank.grid(row=1,column=2)
b_child=Button(frame3,text="children & pets",command=func4)
b_child.grid(row=1,column=3)
b_liesure=Button(frame3,text="leisure spending",command=func5)
b_liesure.grid(row=1,column=4)



root.mainloop()


# In[ ]:




