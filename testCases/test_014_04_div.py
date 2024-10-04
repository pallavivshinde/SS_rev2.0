class Test_014_division():

    def test_04_div2no(self):

        a=100
        b=50
        div=int(a/b)
        if(div==2) :
            print("\n---------DIVISION IS SUCCESSFUL----------\n")
            print("DIVISION=",div)
            assert True ;

        else:
            print("\n---------SOPRRY, INVALID OPERATION\n")
            assert False ;
