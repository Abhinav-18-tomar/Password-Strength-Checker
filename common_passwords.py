

def common(usrInput):
    f=open("CommonPassword_list.py")
    data=f.read().splitlines()
    f.close()
    if usrInput in data:
        return True
    else:
        return False
    
