
library(dplyr)
library(reticulate)

source_python('C:/Users/Administrador/Documents/TESIS/omnilogikd/webscrap.py')

carros <- readxl::read_excel("C:/Users/Administrador/Documents/TESIS/omnilogikd/placas.xlsx", sheet = 1)

# res_fec <- py_run_string("ruta_fecha('200001617', '2022-10-03')")

res <- list(0)
res_fec <- list(0)


for(i in carros$`NUMERO SAP`){
        for(fec in seq.Date(as.Date("2022-01-01"), as.Date("2022-10-31"))){
                res_fec[[j]] <- py_run_string(paste0("ruta_fecha('",i,"', 
                                     '",j,"')"))
        }
        res[[i]] <- do.call(rbind,res_fec)
}