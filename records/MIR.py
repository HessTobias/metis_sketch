import h5py

def MIR(REC_dict, add_par):
    f = h5py.File(add_par["path"]+REC_dict["LOT_ID"]+".hdf5", "a")
    f.create_group(add_par["type"])
    f.create_group(add_par["type"]+"/"+add_par["stdf_name"])

    f.create_group(add_par["type"]+"/"+add_par["stdf_name"]+"/MIR")
    for k in REC_dict.keys():
        f[add_par["type"]+"/"+add_par["stdf_name"]+"/MIR"].attrs[k]=REC_dict[k]

    add_par["file"] = f
    return add_par