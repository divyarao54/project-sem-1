from tkinter import *
import customtkinter
customtkinter.set_default_color_theme("dark-blue")  



root=customtkinter.CTk()
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

#FRAME1
frame1 = customtkinter.CTkFrame(master=root,
                               width=1240, height=50,
                            
                               
                               corner_radius=10)
frame1.grid(row=0,column=0,padx=20, pady=20,sticky="n")
label = customtkinter.CTkLabel(frame1, text="BUDGET MANAGER",
                               
                               fg_color=("transparent"),
                               font=('Helvetica', 34), text_color='white'
                               )
label.place(relx=0.5, rely=0.5,anchor=customtkinter.CENTER)


#FRAME2
frame2=customtkinter.CTkFrame(master=root,width=400,height=50,corner_radius=10)
frame2.grid(row=1,column=0,padx=20,pady=10)

label1=customtkinter.CTkLabel(frame2,text="SOURCES OF REVENUE",font=('Helvetica',20),text_color='#00BFFF',padx=160).grid(row=0,column=0,columnspan=4,pady=20,padx=20)
list1=["Income","Side Hustle","Additional Revenue"] 
count=1
list2=[]
for i in range(len(list1)):
    a="l_"+list1[i]
    b="e_"+list1[i]
    a=customtkinter.CTkLabel(frame2,text=list1[i]).grid(row=count,column=1)
    b=customtkinter.CTkEntry(frame2, width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
    b.grid(row=count,column=2,columnspan=2)
    list2.append(b)
    count+=1   
l=customtkinter.CTkLabel(frame2,text="TOTAL: 0000000 " ,padx=30).grid(row=5,column=2)

#computing sum 
def sumrevenue():
    sumrev=0
    for i in list2:
        d=i.get()
        sumrev+=int(d)
    l=customtkinter.CTkLabel(frame2,text="TOTAL: " +str(sumrev),pady=20,padx=20).grid(row=5,column=2)
b_totalrevenue=customtkinter.CTkButton(frame2,text="SUBMIT",command=sumrevenue)
b_totalrevenue.grid(row=5,column=1,pady=20,padx=20)

#FRAME3

frame3=customtkinter.CTkFrame(master=root,width=900,height=200,corner_radius=10)
frame3.grid(row=2,column=0,padx=20,pady=20)
label2=customtkinter.CTkLabel(frame3,text="EXPENDITURE",font=('Helvetica',20),text_color='#00BFFF',padx=180).grid(row=0,column=0,columnspan=5,pady=20,padx=20)
'''
1
1
1
'''
dictexp={"Household Bills":0,"Living Costs":0,"Banking":0,"Children & Pets":0,"Leisure Spending":0}


        #function1 household bills 
def func1():
    whb=customtkinter.CTkToplevel()
    whb.geometry('440x220+0+253')
    
    
    listhb1=["rent", "maintenance","insurance","car","electricity","water","phone","internet","additional"]
    count=0
    listhb2=[]
    for i in range(len(listhb1)):
            a=customtkinter.CTkLabel(whb,text=listhb1[i]).grid(row=count,column=0)
            b=customtkinter.CTkEntry(whb,width=50)
            b.grid(row=count,column=1,columnspan=2)
            listhb2.append(b)
            count+=1
    sum_hb=customtkinter.CTkLabel(whb,text="total: 0000000 " ,padx=30).grid(row=count,column=2)
    def sumhousehold():
            sumhb=0
            for b in listhb2:
                d=b.get()
                sumhb+=int(d)
            dictexp.update({"household bills":sumhb})
            l=customtkinter.CTkLabel(whb,text="total: " +str(sumhb),padx=30).grid(row=count,column=2)
    b_totalhousehold=customtkinter.CTkButton(whb,text="submit",command=sumhousehold,padx=40,bg="#A8F847")
    b_totalhousehold.grid(row=count,column=1)
    
    
    

            #function2 living costs 

def func2():
    wlc=customtkinter.CTkToplevel()
    wlc.geometry('440x220+0+253')
    listlc1=["groceries","laundry","clothes","toiletries","health","medicines","heathcare","domestic_help","additional"]
    count=0
    listlc2=[]
    for i in range(len(listlc1)):
            a=customtkinter.CTkLabel(wlc,text=listlc1[i]).grid(row=count,column=0)
            b=customtkinter.CTkEntry(wlc,width=50)
            b.grid(row=count,column=1,columnspan=2)
            listlc2.append(b)
            count+=1
    sum_lc=customtkinter.CTkLabel(wlc,text="total: 0000000 " ,padx=30).grid(row=count,column=2)
    
    def sumlivingcost():
            sumlc=0
            for b in listlc2:
                d=b.get()
                sumlc+=int(d)
            dictexp.update({"living costs":sumlc})
            l=customtkinter.CTkLabel(wlc,text="total: " +str(sumlc),padx=30).grid(row=count,column=2)
    b_totallivingcost=customtkinter.CTkButton(wlc,text="submit",command=sumlivingcost,padx=40,bg="#A8F847")
    b_totallivingcost.grid(row=count,column=1)
    
                         #function3 banking

def func3():
    wbk=customtkinter.CTkToplevel()
    wbk.geometry('440x220+0+253')
    listbk1=["bank_account_fees","loan","credit_card_payment","additional"]
    count=0
    listbk2=[]
    for i in range(len(listbk1)):
            a=customtkinter.CTkLabel(wbk,text=listbk1[i]).grid(row=count,column=0)
            b=customtkinter.CTkEntry(wbk,width=50)
            b.grid(row=count,column=1,columnspan=2)
            listbk2.append(b)
            count+=1


    sum_lc=customtkinter.CTkLabel(wbk,text="total: 0000000 " ,padx=30).grid(row=count,column=2)
    def sumbank():
            sumbk=0
            for b in listbk2:
                d=b.get()
                sumbk+=int(d)
            dictexp.update({"banking":sumbk})
            l=customtkinter.CTkLabel(wbk,text="total: " +str(sumbk),padx=30).grid(row=count,column=2)
    b_totalbank=customtkinter.CTkButton(wbk,text="submit",command=sumbank,padx=40,bg="#A8F847")
    b_totalbank.grid(row=count,column=1)
    
                         #function4 children and pets 

def func4():
    wch=customtkinter.CTkToplevel()
    wch.geometry('440x220+0+253')
    listch1=["childcare","school_fees","club_activities","toy","babysitting","vet","pet_insurance","additional"]
    count=0
    listch2=[]
   
    for i in range(len(listch1)):
            a=customtkinter.CTkLabel(wch,text=listch1[i]).grid(row=count,column=0)
            b=customtkinter.CTkEntry(wch,width=50)
            b.grid(row=count,column=1,columnspan=2)
            listch2.append(b)
            count+=1


    sum_ch=customtkinter.CTkLabel(wch,text="total: 0000000 " ,padx=30).grid(row=count,column=2)
    def sumchild():
            sumch=0
            for b in listch2:
                d=b.get()
                sumch+=int(d)
            dictexp.update({"children & pets":sumch})
            l=customtkinter.CTkLabel(wch,text="total: " +str(sumch),padx=30).grid(row=count,column=2)
    b_totalchild=customtkinter.CTkButton(wch,text="submit",command=sumchild,padx=40,bg="#A8F847")
    b_totalchild.grid(row=count,column=1)
    
    
                     #function5 liesure spending  

def func5():
    wli=customtkinter.CTkToplevel()
    wli.geometry('440x220+0+253')
    listli1=["hobbies","day_outs","cinema","books_and_games","newsletter","birthdays","festive_spending","holidays"]
    count=0
    listli2=[]
    for i in range(len(listli1)):
            a=customtkinter.CTkLabel(wli,text=listli1[i]).grid(row=count,column=0)
            b=customtkinter.CTkEntry(wli,width=50)
            b.grid(row=count,column=1,columnspan=2)
            listli2.append(b)
            count+=1
    sum_ch=customtkinter.CTkLabel(wli,text="total: 0000000 " ,padx=30).grid(row=count,column=2)
    def sumliesure():
            sumli=0
            for b in listli2:
                d=b.get()
                sumli+=int(d)
            dictexp.update({"leisure spending":sumli})
            l=customtkinter.CTkLabel(wli,text="total: " +str(sumli),padx=30).grid(row=count,column=2)
    b_totalliesure=customtkinter.CTkButton(wli,text="submit",command=sumliesure,padx=40)
    b_totalliesure.grid(row=count,column=2)
    
    
    
#expenditure buttons for the above functions
        
b_housebill=customtkinter.CTkButton(frame3,text="Household Bills",command=func1,width=10)
b_housebill.grid(row=1,column=0,pady= 20, padx= 20)
b_livingcost=customtkinter.CTkButton(frame3,text="Living Costs ",command=func2,width=10)
b_livingcost.grid(row=1,column=1,pady= 20, padx= 20)
b_bank=customtkinter.CTkButton(frame3,text="Banking ",command=func3,width=10)
b_bank.grid(row=1,column=2,pady= 20, padx= 20)
b_child=customtkinter.CTkButton(frame3,text="Children & Pets",command=func4,width=10)
b_child.grid(row=1,column=3,pady= 20, padx= 20)
b_liesure=customtkinter.CTkButton(frame3,text="Leisure Spending",command=func5,width=10)
b_liesure.grid(row=1,column=4,pady= 20, padx= 20)

#FRAME4
frame4=customtkinter.CTkFrame(master=root,width=900,height=200,corner_radius=10)
frame4.grid(row=3,column=0,padx=20,pady=20)

label4=customtkinter.CTkLabel(frame4,text="SAVINGS",font=('Helvetica',20),text_color='#00BFFF',padx=160,corner_radius=10).grid(row=0,column=0,columnspan=6,pady=20,padx=20)


lista=["Goal"] 
count=1
listb=[]
for i in range(len(lista)):
        x="l_"+lista[i]
        y="e_"+lista[i]
        x=customtkinter.CTkLabel(frame4,text=lista[i]).grid(row=count,column=1)
        y=customtkinter.CTkEntry(frame4, width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
        y.grid(row=count,column=2,columnspan=4)
        listb.append(y)
        count+=1
        goal=customtkinter.CTkLabel(frame4,text="Saving Goal for This Month: 0000000 " ,padx=30).grid(row=4,column=2)

def savings():
    save=0
    for i in listb:
        z=i.get()
        save+=int(z)
    goal=customtkinter.CTkLabel(frame4,text="Saving Goal for This Month: " +str(save),pady=20,padx=20).grid(row=4,column=2)
savesubmit=customtkinter.CTkButton(frame4,text="SUBMIT",command=savings)
savesubmit.grid(row=4,column=1,pady=20,padx=20)







root.mainloop()





