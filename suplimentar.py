suma=int(input("introduceti suma:"))
print\
    ("aveti nevoie de",suma//1000,"bancnote de 1000 lei,",suma%1000//500,"de 500 lei,",suma%1000%500//200,"de 200 lei,",suma%1000%500%200//100,"de 100 lei,",\
    suma%1000%500%200%100//50,"de 50 lei,",suma%1000%500%200%100%50//20,"de 20 lei,",suma%1000%500%200%100%50%20//10,"de 10 lei,",\
     suma%1000%500%200%100%50%20%10//5,"de 5 lei,",suma%1000%500%200%100%50%20%10%5//2, "de 2 lei si",suma%1000%500%200%100%50%20%10%5%2//1, "de 1 leu.")