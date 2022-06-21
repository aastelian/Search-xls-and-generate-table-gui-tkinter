from config.definitions import ROOT_DIR
from config.definitions import NET_DIR
import os,xlrd
from tkinter import messagebox

class MainApp:
    
    def read_excel(self):
        self.r_wb = xlrd.open_workbook(os.path.join(NET_DIR,"Registru reclamatii calitate final.xls"))
        r_ws = self.r_wb.sheet_by_index(0)
        return r_ws
        
    def get_dict(self):
        
        register = self.read_excel()
        no_of_rows = register.nrows
        self.register_dict = {}
        for n in range(2,no_of_rows):
            complaint = Complaint()
            
            complaint.number = str(int(register.cell_value(n,0)))
            date=register.cell_value(n,1)
            complaint.date = str(xlrd.xldate_as_tuple(date,self.r_wb.datemode)[2])+"."+str(xlrd.xldate_as_tuple(date,self.r_wb.datemode)[1])+"."+str(xlrd.xldate_as_tuple(date,self.r_wb.datemode)[0])
            complaint.product_name=str(register.cell_value(n,2))
            complaint.product_lot=register.cell_value(n,3)
            complaint.product_quantity=register.cell_value(n,4)
            complaint.description=register.cell_value(n,5)
            complaint.client=register.cell_value(n,6)
            complaint.supplier=register.cell_value(n,7)
            complaint.status=register.cell_value(n,8)
            
            self.register_dict[complaint.number] = complaint
        
        # for key,value in self.register_dict[400].__dict__.items():
            # print(value)
            
    def search_in_dict(self,number="",product="",supplier=""):
        self.get_dict()
        searched_list = []
        product=product.upper()
        supplier=supplier.upper()
        
        if number != "":
            try:
                searched_list.append(self.register_dict[number].__dict__)
            except:
                messagebox.showinfo("Atentie!",f"Reclamatia {number} nu exista!")
                
        else:
            for key,value in self.register_dict.items():
                if product in value.__dict__["product_name"] and supplier in value.__dict__["supplier"]:
                    
                    searched_list.append(value.__dict__)
                    
        return searched_list
            
                
        
        
            
class Complaint:
    
    def __init__(self):
        self.number = 0
        self.date = 0
        self.product_name = 0
        self.product_lot = 0
        self.product_quantity = 0
        self.description = 0
        self.client = 0
        self.supplier = 0
        self.status = 0
        
