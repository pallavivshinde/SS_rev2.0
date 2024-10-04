

class Test_014_01_Add():
    def test_01_add2n0(self):
        a=100
        b =50
        add=a+b
        if(add == 150):
            print("\n addition is done ")
            print("\n ADDITION",add)
            assert True

        else:
            print("\n-----------SORRY, INVALID OPERTAION\n")
            assert False
