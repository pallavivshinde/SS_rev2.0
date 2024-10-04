
class Test_014_subtraction:
    def test_014_sub(self):
        a= 100
        b= 50
        sub = a-b
        if(sub == 50):
            print("\n------------SUBSTRATION IS SUCCESSFUL----------\n") ;
            print("SUBSTARCTION=", sub);
            assert True;
        else:
            print("\n----------SORRY,INVALID OPERATION-----------\n");
            assert False;


