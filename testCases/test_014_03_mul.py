class Test_014_multiplication():
    def test_014_03_mul(self):
        a= 100
        b=50
        mul = 100*50
        if(mul == 5000):
            print("\n-----------MULTIPLICATION IS SUCCESSFUL----------\n")
            print("MULTIPLICATION=", mul)
            assert True
        else:
            print("\nSORRY, INVALID OPERATION\n")
            assert False;




