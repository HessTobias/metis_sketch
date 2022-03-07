def GDR(REC_dict, add_par):

    f = add_par["file"]

    REC_dict["GEN_DATA"] = str(REC_dict["GEN_DATA"])

    i = 0
    b = True 
    while b:
        try: 
            f.create_group(add_par["type"]+"/"+add_par["stdf_name"]+"/GDR-"+str(i))
            b = False
        except:
            i = i + 1
    
    for k in REC_dict.keys():
        f[add_par["type"]+"/"+add_par["stdf_name"]+"/GDR-"+str(i)].attrs[k]=REC_dict[k]

    
    return add_par