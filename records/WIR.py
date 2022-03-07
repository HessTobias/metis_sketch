def WIR(REC_dict, add_par):
    f = add_par["file"]
    wafer_id = str(REC_dict["WAFER_ID"])

    f.create_group(add_par["type"]+"/"+add_par["stdf_name"]+"/"+wafer_id)
    for k in REC_dict.keys():
        f[add_par["type"]+"/"+add_par["stdf_name"]+"/"+str(wafer_id)].attrs[k]=REC_dict[k]

    add_par["active_wafer_with_head_as_key"][REC_dict["HEAD_NUM"]] = wafer_id


    return add_par