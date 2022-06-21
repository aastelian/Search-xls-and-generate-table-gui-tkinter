from mainscript import MainApp, Complaint
import tkinter as tk


class App:
    
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("1300x800")
        self.root.title("Registrul de reclamatii")
        
        self.tl = tk.Label(self.root,text="Registrul de reclamatii")
        self.tl.grid(row=1,column=2)
        
        self.numberL=tk.Label(self.root,text="Nr. reclamatie:")
        self.numberL.grid(row=2,column=1)
        self.numberE=tk.Entry(self.root)
        self.numberE.grid(row=2,column=2)
        
        self.dateL=tk.Label(self.root,text="Data reclamatie:")
        self.dateL.grid(row=3,column=1)
        self.dateE=tk.Entry(self.root)
        self.dateE.grid(row=3,column=2)
        
        self.productL=tk.Label(self.root,text="Denumire produs:")
        self.productL.grid(row=4,column=1)
        self.productE=tk.Entry(self.root)
        self.productE.grid(row=4,column=2)
        
        self.clientL=tk.Label(self.root,text="Denumire client:")
        self.clientL.grid(row=5,column=1)
        self.clientE=tk.Entry(self.root)
        self.clientE.grid(row=5,column=2)
        
        self.supplierL=tk.Label(self.root,text="Furnizor:")
        self.supplierL.grid(row=6,column=1)
        self.supplierE=tk.Entry(self.root)
        self.supplierE.grid(row=6,column=2)
        
        self.statusL=tk.Label(self.root,text="Status reclamatie:")
        self.statusL.grid(row=7,column=1)
        self.statusE=tk.Entry(self.root)
        self.statusE.grid(row=7,column=2)
        
        b=tk.Button(self.root,text="Cauta Reclamatia",command=lambda:self.search())
        b.grid(row=8,column=2)
        
        self.f = tk.Frame(self.root,width = 1300, height = 40)
        self.f.grid(row=9,column=1,columnspan=2)
        self.f2 = tk.Frame(self.root,width = 1300, height = 5)
        self.f2.grid(row=10,column=1,columnspan=2)
        
        self.root.mainloop()
        
    def search(self):
        number=str(self.numberE.get())
        product=str(self.productE.get())
        supplier=str(self.supplierE.get())
        self.numberE.delete(0,"end")
        self.productE.delete(0,"end")
        self.supplierE.delete(0,"end")
        if number == product == supplier == "":
            pass
        else:
            result=MainApp().search_in_dict(number=number,product=product,supplier=supplier)        #returns a list of dictionaries that respect the input
            
            if str(result) != "[]":
                for n in result:
                    for key,value in n.items():
                        print(str(key)+": "+str(value))
                    print("\n")  
                self.generate_table_top()
                x=1
                result_index = 0
                self.result_length = len(result)     #numarul de reclamatii extrase
                # try:
                    # for i in range(20):
                        # nL.destroy()
                # except:
                    # pass
                self.myWidth = 20
                self.p=7
                self.myHeight = 7
                
               
                self.nr = 5
                
                try:
                    for n in range((self.nr-5),self.nr):
                        nL=tk.Label(self.f,text=result[n]["number"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
                        nL.grid(row=x,column=1)
                        dL=tk.Label(self.f,text=result[n]["date"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
                        dL.grid(row=x,column=2)
                        prodL=tk.Label(self.f,text=result[n]["product_name"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
                        prodL.grid(row=x,column=3)
                        lotL=tk.Label(self.f,text=result[n]["product_lot"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
                        lotL.grid(row=x,column=4)
                        quantL=tk.Label(self.f,text=result[n]["product_quantity"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
                        quantL.grid(row=x,column=5)
                        compL=tk.Label(self.f,text=result[n]["description"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
                        compL.grid(row=x,column=6)
                        clL=tk.Label(self.f,text=result[n]["client"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
                        clL.grid(row=x,column=7)
                        supL=tk.Label(self.f,text=result[n]["supplier"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
                        supL.grid(row=x,column=8)
                        statL=tk.Label(self.f,text=result[n]["status"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
                        statL.grid(row=x,column=9)
                        x+=1
                       
                except:
                    pass
                    
                previous_B = tk.Button(self.f2,text = "Previous page",command = lambda c=result : self.goBackwards(param = c))
                previous_B.grid(row=1,column = 1)
                forward_B = tk.Button(self.f2,text = "Forward page",command = lambda c=result: self.goForwards(param=c))
                forward_B.grid(row=1,column=2)
                
    def goBackwards(self,param):
        if self.nr-5 >=5:
            self.nr -= 5
        else:
            self.nr -= self.nr -5
         
        
        
            
        try:
            for widget in self.f.winfo_children():
                widget.destroy()
        except:
            pass
        
        x=1
        self.add_table_top()
        for n in range(self.nr-5,self.nr):
            nL=tk.Label(self.f,text=param[n]["number"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            nL.grid(row=x,column=1)
            dL=tk.Label(self.f,text=param[n]["date"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            dL.grid(row=x,column=2)
            prodL=tk.Label(self.f,text=param[n]["product_name"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            prodL.grid(row=x,column=3)
            lotL=tk.Label(self.f,text=param[n]["product_lot"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            lotL.grid(row=x,column=4)
            quantL=tk.Label(self.f,text=param[n]["product_quantity"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            quantL.grid(row=x,column=5)
            compL=tk.Label(self.f,text=param[n]["description"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            compL.grid(row=x,column=6)
            clL=tk.Label(self.f,text=param[n]["client"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            clL.grid(row=x,column=7)
            supL=tk.Label(self.f,text=param[n]["supplier"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            supL.grid(row=x,column=8)
            statL=tk.Label(self.f,text=param[n]["status"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            statL.grid(row=x,column=9)
            x+=1
            
        
    
    def goForwards(self,param):
        start = self.nr
        if self.nr+5 <= self.result_length:
            self.nr += 5
            
        else:
            self.nr += self.result_length-self.nr
            
        
        
        try:
            for widget in self.f.winfo_children():
                widget.destroy()
        except:
            pass
        x=1
        self.add_table_top()
        for n in range(start,self.nr):
            nL=tk.Label(self.f,text=param[n]["number"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            nL.grid(row=x,column=1)
            dL=tk.Label(self.f,text=param[n]["date"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            dL.grid(row=x,column=2)
            prodL=tk.Label(self.f,text=param[n]["product_name"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            prodL.grid(row=x,column=3)
            lotL=tk.Label(self.f,text=param[n]["product_lot"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            lotL.grid(row=x,column=4)
            quantL=tk.Label(self.f,text=param[n]["product_quantity"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            quantL.grid(row=x,column=5)
            compL=tk.Label(self.f,text=param[n]["description"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            compL.grid(row=x,column=6)
            clL=tk.Label(self.f,text=param[n]["client"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            clL.grid(row=x,column=7)
            supL=tk.Label(self.f,text=param[n]["supplier"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            supL.grid(row=x,column=8)
            statL=tk.Label(self.f,text=param[n]["status"],borderwidth = 1, relief = "solid",width=self.myWidth,wraplength = self.myWidth*self.p,height=self.myHeight)
            statL.grid(row=x,column=9)
            x+=1
        
    def generate_table_top(self):
        try:
            for widget in self.f.winfo_children():
                widget.destroy()
        except:
            pass
        self.myWidth = 20
        self.myHeight = 2
        numberTop=tk.Label(self.f,text="Nr. reclamatie:",borderwidth = 1, relief = "solid",width=self.myWidth,height=self.myHeight)
        numberTop.grid(row=0,column=1)
        dateTop=tk.Label(self.f,text="Data reclamatie:",borderwidth = 1, relief = "solid",width=self.myWidth,height=self.myHeight)
        dateTop.grid(row=0,column=2)
        productTop=tk.Label(self.f,text="Denumire produs:",borderwidth = 1, relief = "solid",width=self.myWidth,height=self.myHeight)
        productTop.grid(row=0,column=3)
        lotTop=tk.Label(self.f,text="Lot/bbd:",borderwidth = 1, relief = "solid",width=self.myWidth,height=self.myHeight)
        lotTop.grid(row=0,column=4)
        quantityTop=tk.Label(self.f,text="Cantitate:",borderwidth = 1, relief = "solid",width=self.myWidth,height=self.myHeight)
        quantityTop.grid(row=0,column=5)
        complaintTop=tk.Label(self.f,text="Descrierea reclamatiei:",borderwidth = 1, relief = "solid",width=self.myWidth,height=self.myHeight)
        complaintTop.grid(row=0,column=6)
        clientTop=tk.Label(self.f,text="Client:",borderwidth = 1, relief = "solid",width=self.myWidth,height=self.myHeight)
        clientTop.grid(row=0,column=7)
        supplierTop = tk.Label(self.f,text="Furnizor:",borderwidth = 1, relief = "solid",width=self.myWidth,height=self.myHeight)
        supplierTop.grid(row=0,column=8)
        statusTop = tk.Label(self.f,text="Statusul reclamatiei:",borderwidth = 1, relief = "solid",width=self.myWidth,height=self.myHeight)
        statusTop.grid(row=0,column=9)
    
    def add_table_top(self):
        self.TTmyWidth = 20
        self.TTmyHeight = 2
        numberTop=tk.Label(self.f,text="Nr. reclamatie:",borderwidth = 1, relief = "solid",width=self.TTmyWidth,height=self.TTmyHeight)
        numberTop.grid(row=0,column=1)
        dateTop=tk.Label(self.f,text="Data reclamatie:",borderwidth = 1, relief = "solid",width=self.TTmyWidth,height=self.TTmyHeight)
        dateTop.grid(row=0,column=2)
        productTop=tk.Label(self.f,text="Denumire produs:",borderwidth = 1, relief = "solid",width=self.TTmyWidth,height=self.TTmyHeight)
        productTop.grid(row=0,column=3)
        lotTop=tk.Label(self.f,text="Lot/bbd:",borderwidth = 1, relief = "solid",width=self.TTmyWidth,height=self.TTmyHeight)
        lotTop.grid(row=0,column=4)
        quantityTop=tk.Label(self.f,text="Cantitate:",borderwidth = 1, relief = "solid",width=self.TTmyWidth,height=self.TTmyHeight)
        quantityTop.grid(row=0,column=5)
        complaintTop=tk.Label(self.f,text="Descrierea reclamatiei:",borderwidth = 1, relief = "solid",width=self.TTmyWidth,height=self.TTmyHeight)
        complaintTop.grid(row=0,column=6)
        clientTop=tk.Label(self.f,text="Client:",borderwidth = 1, relief = "solid",width=self.TTmyWidth,height=self.TTmyHeight)
        clientTop.grid(row=0,column=7)
        supplierTop = tk.Label(self.f,text="Furnizor:",borderwidth = 1, relief = "solid",width=self.TTmyWidth,height=self.TTmyHeight)
        supplierTop.grid(row=0,column=8)
        statusTop = tk.Label(self.f,text="Statusul reclamatiei:",borderwidth = 1, relief = "solid",width=self.TTmyWidth,height=self.TTmyHeight)
        statusTop.grid(row=0,column=9)
        
        
        
        
App()