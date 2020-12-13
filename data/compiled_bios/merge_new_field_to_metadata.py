import os

field_name ='areas'
with open('metadata.dat', 'wb') as f_write:
    with open('temp/metadata.dat', 'rb') as f_old:
        with open(os.path.join('..', field_name), 'rb') as f_new:
            data_to_write = ['\t'.join([old.strip(), (new if new.strip() else 'None\n')
             ]) for old, new in zip(f_old.readlines(), f_new.readlines())]
            data_to_write[-1]=data_to_write[-1].strip()
            f_write.writelines(data_to_write)