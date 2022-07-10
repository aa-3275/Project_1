import logging as lg
class ineuron:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
    lg.basicConfig(filename="../student_record.log", level=lg.INFO, format='%(levelname)s %(name)s %(asctime)s %(message)s')
    try:
        def chat_with_agent(self):
            '''You can write you query and our agent will contact you within 10 minutes'''
            message= "How can I help you Mr. "+ self.name + "\n" + "You will received a call on your registered number with in 5 minutes.\n \n \n Thanks You for contacting Us!!"
            print(message)
            info_detail = self.name + "\n" + self.email + "\n" + self.phone_number
            lg.info(message)
            lg.info(info_detail)
    except Exception:
        error="Not able to connect due to heavy demand"
        info_detail= self.name + "\n" + self.email + "\n" + self.phone_number
        print(error)
        lg.info(info_detail)

