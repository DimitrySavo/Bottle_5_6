import myform_mail
import unittest

mails_correct = ["test@mail.ru",
                 "dima@st.guap.ru",
                 "Emil@gmail.com",
                 "123@gmail.com",
                 "2___@gmail.com",
                 "2...@gmail.com",
                 "f@gmail.com"]
mails_uncorrect = ["",
                   " ",
                   "123123",
                   "qdqsfasf"
                   "asd@@@",
                   "@mail.com",
                   "dwqd @ sss.sd",
                   "@.ru",
                   "asdsd@@@@@mail.com",
                   ("s"*300) + "@gmail.com",
                   "s@" + ("g" * 65) + ".com",
                   "dima@gmail." + ("d" * 10),
                   "dima@gmail.r",
                   "dima@gmail..com"]

class MailTest(unittest.TestCase):
    def test_T_mail(self):
        for mail in mails_correct:
            self.assertTrue(myform_mail.check_mail(mail))
            
    def test_F_mail(self):
        for mail in mails_uncorrect:
            self.assertFalse(myform_mail.check_mail(mail))
            
if __name__ == "__main__":
    unittest.main()