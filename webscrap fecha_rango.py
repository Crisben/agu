from selenium import webdriver  
from datetime import timedelta
from datetime import datetime
import datetime
import time
import pandas as pd

# excel_data = pd.read_excel("C:/Users/Administrador/Documents/TESIS/omnilogikd/placas.xlsx",
# # sheetname='Custodio',
# dtype=str)
# data = pd.DataFrame(excel_data)

indic = []

# fecha_ini = datetime.date(2022, 10, 1)
# fecha_fin = fecha_ini#+timedelta(1)

hora_ini = datetime.time(0,0,0) 
hora_fin = datetime.time(23,59,59)

seg = 2

# for i in data["NUMERO SAP"]:
        
# sap = "200001617"  # PMA-7870
# fecha_ini="2022-10-03"
# fecha_fin="2022-10-06"

# datetime_str = '09/19/18'
# datetime.strptime(datetime_str, '%m/%d/%y')



def ruta_fecha_rango(sap, fecha_ini, fecha_fin):
        fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')+timedelta(1)
        fecha_fin = datetime.datetime.date(fecha_fin)

        remDr =  webdriver.Chrome()  
        remDr.get("http://69.64.40.175:8881/")  

        remDr.find_element("name","O3B").send_keys("EPMAPS")
        remDr.find_element("name","O2B").send_keys("120584")
        remDr.find_element("xpath",
        '/html/body/div[5]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr/td').click()
        time.sleep(4)
        
        remDr.find_element("name","OE1").send_keys(sap)
        time.sleep(8)
        
        # remDr.find_element("id","OE5_id").click()
        remDr.find_element("xpath",
        '/html/body/div[7]/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div[5]/div/div/div/div/div[4]/div/div/div/div/a').click()
        time.sleep(2)
        
        remDr.find_element("id","O120_id").click()
        time.sleep(2)
        
        # remDr.find_element("name","O490").send_keys("delete")

        # desde_rep = remDr.find_element("id",'O490_id')
        desde_rep = remDr.find_element("xpath",
        '/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[3]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div/div[1]/input')
        desde_rep.click()
        desde_rep.clear()
        desde_rep.send_keys(str(fecha))

        hasta_rep = remDr.find_element("xpath",
        '/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div[1]/input')
        hasta_rep.click()
        hasta_rep.clear()
        hasta_rep.send_keys(str(fecha_fin))

        # time.sleep(seg)
        # desde_h = remDr.find_element("xpath",'/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[3]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]')
        #                                       # /html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[3]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/input
        # desde_h.click()
        # desde_h.clear()
        # desde_h.send_keys(str(hora_ini))

        time.sleep(seg)
        # hasta_h = remDr.find_element("xpath",'/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]')
        # hasta_h = remDr.find_element("name",'O1E94')
        
        hasta_h = remDr.find_element("xpath",'/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        hasta_h.click()
        
        hasta_0 = remDr.find_element("xpath",'/html/body/div[12]/div[1]/ul/li[1]')
        hasta_0.click()
        
        
        gal = remDr.find_element("xpath", '/html/body/div[10]/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/label[3]').text
        km = remDr.find_element("xpath", '/html/body/div[10]/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/label[4]').text

        remDr.find_element("xpath", '/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[3]/div/div/div/div/a[1]/span/span').click()
        time.sleep(5)
        
        remDr.find_element("xpath", '/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[3]/div/div/div/div/a[7]/span').click()
        time.sleep(10)
        
        # tab = remDr.find_element("xpath", '/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[2]').text
        # tab = tab.split(datetime.date.strftime(fecha_ini, "%d/%m/%Y"))
        # tab = tab.splitlines()
        
        # tab = remDr.find_element("xpath", '/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[2]/table[1]').text
        # remDr.find_element("xpath", '/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[2]/table[2]').text
        # remDr.find_element("xpath", '/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[2]/table[2]').text
        # remDr.find_element("xpath", '/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[2]/table[30]').text
        
        #descarga csv
        remDr.find_element("xpath", '/html/body/div[10]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[3]/div/div/div/div/a[2]/span/span').click()
        time.sleep(seg)
        
        remDr.find_element("xpath", '/html/body/div[13]/div[2]/div/div/div/div/div/div/a[3]').click()
        time.sleep(seg)
        
        remDr.find_element("xpath", '/html/body/div[15]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[1]').click()
        time.sleep(seg)
        
        remDr.find_element("xpath", '/html/body/div[15]/div[2]/div[2]/div/div/a[1]/span').click()
        time.sleep(seg)
        
        remDr.find_element("xpath", '/html/body/div[13]/div[1]/div/div/div[2]').click()
        time.sleep(seg)
        
        remDr.find_element("xpath", '/html/body/div[10]/div[1]/div/div/div[4]').click()
        time.sleep(seg)
        
        indic_res = [sap, gal, km, str(fecha)]
        indic.append(indic_res)
        
        remDr.close()  
        print(indic_res)
        return  indic
        


# ruta_fecha_rango("200001617", "2022-10-03", "2022-10-20")

