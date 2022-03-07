def WCR(REC_dict, add_par):

    f = add_par["file"]
    f.create_group(add_par["type"]+"/"+add_par["stdf_name"]+"/WCR")
    for k in REC_dict.keys():
        f[add_par["type"]+"/"+add_par["stdf_name"]+"/WCR"].attrs[k]=REC_dict[k]
    
    return add_par