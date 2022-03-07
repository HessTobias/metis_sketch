def SDR(REC_dict, add_par):
    f = add_par["file"]
    grp = REC_dict["SITE_GRP"]

    f.create_group(add_par["type"]+"/"+add_par["stdf_name"]+"/SDR-"+str(grp))
    for k in REC_dict.keys():
        f[add_par["type"]+"/"+add_par["stdf_name"]+"/SDR-"+str(grp)].attrs[k]=REC_dict[k]

    
    return add_par