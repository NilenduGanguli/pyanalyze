from src1.test_c1 import test1
from src2.test2 import *
from src1.test_m1 import test_m1
from src2.test_c1_cpy import test1 as test1_cpy

if __name__=="__main__":
    print("Executing...")
    test1_obj=test1()
    test1_obj.show(indent=2)