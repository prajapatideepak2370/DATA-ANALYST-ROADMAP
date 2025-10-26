#PRIVATE ATTRIBUTES

class bank:
    __Acc_no = 34563 # private the class attribute

    def __acc_pass(self):
        num = 3453
        print("Your Account Password: ", num)

    def youpswd(self):
        self.__acc_pass()


s1 = bank()
print(s1.youpswd())