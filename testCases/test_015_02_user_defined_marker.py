import pytest

class Test_016_02_user_marker():
    @pytest.mark.customer
    def test_add_customer(self):
        print("\n CUSTOMERS ADDED SUCCESSFULLY\n")

    @pytest.mark.customer
    def test_del_customer(self):
        print("\n CUSTOMER DELETED SUCCESSFULLY \n")

    @pytest.mark.product
    def test_add_product(self):
        print("\n PRODUCT ADDED SUCCESSFULLY \n")

    @pytest.mark.product
    def test_del_product(self):
        print("\n PRODUCT DELETED SUCCESSFULLY \n")

    @pytest.mark.bill
    def test_add_bill(self):
        print("\n BILL ADDED SUCCESSFULLY\n")

    @pytest.mark.bill
    def test_del_bill(self):
        print("\n BILL DELETED SUCCESSFULLY \n")

    @pytest.mark.regression
    @pytest.mark.patient
    def test_add_patient(self):
        print("\n PATIENT ADDED SUCCESSFULLY\n")

    @pytest.mark.sanity
    @pytest.mark.patient
    def test_del_patient(self):
        print("\n PATIENT DELETES SUCCESSFULLY\n")
