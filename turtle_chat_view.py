#2016-2017 PERSONAL PROJECTS: TurtleChat!
#WRITE YOUR NAME HERE!
"""
Shira Struminski
"""

#####################################################################################
#                                   IMPORTS                                         #
#####################################################################################
#import the turtle module
import turtle
from turtle_chat_client import Client
from turtle_chat_widgets import Button,TextInput
#import the Client class from the turtle_chat_client module
#Finally, from the turtle_chat_widgets module, import two classes: Button and TextInput
#####################################################################################
#####################################################################################

#####################################################################################
#                                   TextBox                                         #
#####################################################################################
#Make a class called TextBox, which will be a subclass of TextInput.
#Because TextInput is an abstract class, you must implement its abstract
#methods.  There are two:
class TextBox(TextInput):
    def draw_box(self):
        self.pos=(-100,-135)
        screen= turtle.Screen()
        background="C:/Users/User/Desktop/GitHub/meet201617YL1cs-chat/the.gif"
        screen.bgpic(background)
        drawing=turtle.clone()
        drawing.penup()
        drawing.goto(self.pos)
        drawing.pendown()
        e=drawing.goto(self.pos[0]+self.width,self.pos[1])
        g=drawing.goto(self.pos[0]+self.width,self.pos[1]+self.height)
        l=drawing.goto(self.pos[0],self.pos[1]+self.height)
        drawing.goto(self.pos)
        drawing.hideturtle()
        turtle.hideturtle()
        

    def write_msg(self):
        self.writer.clear()
        self.writer.penup()
        self.writer.goto(-95,-60)
        self.writer.write(self.new_msg, font=("Ashcan BB",16,"normal"))

        '''
       in here add the range for the text, if the range
       of the rectangle reached, open new line.
       '''

#draw_box
#write_msg
#
#Hints:
#1. in draw_box, you will draw (or stamp) the space on which the user's input
#will appear.
#
#2. All TextInput objects have an internal turtle called writer (for example, self will
#   have something called writer).  You can write new text with it using code like
#
#   self.writer.write(a_string_variable)
#
#   and you can erase that text using
#
#   self.writer.clear()
#
#3. If you want to make a newline character (for example, go to the next line), just add
#   \r to your string.  Test it out at the Python shell for practice
#####################################################################################
#####################################################################################

#####################################################################################
#                                  SendButton                                       #
#####################################################################################
#Make a class called SendButton, which will be a subclass of Button.
#Button is an abstract class with one abstract method: fun.
<<<<<<< HEAD
#fun gets called whenever the button is clicked.  It's jobs will be to


class SendButton(Button):
    def __init__(self,the_view):
        image= "C:/Users/User/Desktop/GitHub/meet201617YL1cs-chat/i.gif"
        super(SendButton,self).__init__(pos = (0,-170),shape=image)
        self.the_view=the_view
        
    def fun(self,x=None,y=None):
        self.the_view.send_msg()


=======
#fun gets called whenever the button is clicked.  Its jobs will be to
#
>>>>>>> refs/remotes/meet-projects/master
# 1. send a message to the other chat participant - to do this,
#    you will need to call the send method of your Client instance
# 2. update the messages that you see on the screen
#
#HINT: You may want to override the __init__ method so that it takes one additional
#      input: view.  This will be an instance of the View class you will make next
#      That class will have methods inside of it to help
#      you send messages and update message displays.
#####################################################################################
#####################################################################################


##################################################################
#                             View                               #
##################################################################
#Make a new class called View.  It does not need to have a parent
#class mentioned explicitly.



#Read the comments below for hints and directions.
##################################################################
##################################################################
class View:
    _MSG_LOG_LENGTH=5 #Number of messages to retain in view
    _SCREEN_WIDTH=300
    _SCREEN_HEIGHT=600
    _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))

    def __init__(self,username='Me',partner_name='Partner'):
        '''
        :param username: the name of this chat user
        :param partner_name: the name of the user you are chatting with
        '''
        turtle.setup(width= self._SCREEN_WIDTH, height= self._SCREEN_HEIGHT)
        ###
        #Store the username and partner_name into the instance.
        ###
        self.username=username
        self.partner_name=partner_name
        ###
        #Make a new Client object and store it in this instance of View
        #(for example, self).  The name of the instance should be my_client
        ###
        my_client=Client()
        self.my_client=my_client
        ###
        #Set screen dimensions using turtle.setup
        #You can get help on this function, as with other turtle functions,
        #by typing
        #
        #   import turtle
        #   help(turtle.setup)
        #
        #at the Python shell.
        ###

        ###
        #This list will store all of the messages.
        #You can add strings to the front of the list using
        #   self.msg_queue.insert(0,a_msg_string)
        #or at the end of the list using
        #   self.msg_queue.append(a_msg_string)
        self.msg_queue=[]
        ###
        ###
        #Create one turtle object for each message to display.
        #You can use the clear() and write() methods to erase
        #and write messages for each
        ###
        self.t1=turtle.clone()
        self.t2=turtle.clone()
        self.t3=turtle.clone()
        self.t4=turtle.clone()
        self.t5=turtle.clone()
        self.turtles=[self.t1,self.t2,self.t3,self.t4,self.t5]
        
        ###
        #Create a TextBox instance and a SendButton instance and
        #Store them inside of this instance
        ###
        self.m=TextBox()
        self.k=SendButton(self)
        ###
        #Call your setup_listeners() function, if you have one,
        #and any other remaining setup functions you have invented.
        ###
        #self.setup_listeners()

    def send_msg(self):
        '''
        You should implement this method.  It should call the
        send() method of the Client object stored in this View
        instance.  It should also update the list of messages,
        self.msg_queue, to include this message.  It should
        clear the textbox text display (hint: use the clear_msg method).
        It should call self.display_msg() to cause the message
        display to be updated.
        '''
        self.my_client.send(self.m.new_msg)
        self.msg_queue.append(self.username+" says:\r" +self.m.new_msg)
        ##self.m.write_msg(self.new_msg)
        self.m.writer.clear()
        self.m.new_msg=''
        self.display_msg()
    def get_msg(self):
        return self.textbox.get_msg()

    

    def setup_listeners(self):
        '''
        Set up send button - additional listener, in addition to click,
        so that return button will send a message.
        To do this, you will use the turtle.onkeypress function.
        The function that it will take is
        self.send_btn.fun
        where send_btn is the name of your button instance

        Then, it can call turtle.listen()
        '''
        pass

    def msg_received(self,msg):
        '''
        This method is called when a new message is received.
        It should update the log (queue) of messages, and cause
        the view of the messages to be updated in the display.

        :param msg: a string containing the message received
                    - this should be displayed on the screen
        '''
        print(msg) #Debug - print message
        show_this_msg=self.partner_name+' says:\r'+ msg
        #Add the message to the queue either using insert (to put at the beginning)
        #or append (to put at the end).
        #
        #Then, call the display_msg method to update the display
        self.msg_queue.append(show_this_msg)
        #self.msg_queue.append(msg)
        self.display_msg()
    def display_msg(self):
        '''
        This method should update the messages displayed in the screen.
        You can get the messages you want from self.msg_queue
        '''
        ###hiding the annoying turtles
        self.t1.hideturtle()
        self.t2.hideturtle()
        self.t3.hideturtle()
        self.t4.hideturtle()
        self.t5.hideturtle()
        ###pen uping
        self.t1.penup()
        self.t2.penup()
        self.t3.penup()
        self.t4.penup()
        self.t5.penup()
        ### starting actuall writing
        self.t1.clear()
        self.t1.goto(-100,220)
        self.t1.write(self.msg_queue[-1], font=("Escalope Crust Three",17,"normal"))
        if len(self.msg_queue)>=2: 
            self.t2.clear()
            self.t2.goto(-100,160)
            self.t2.write(self.msg_queue[-2], font=("Escalope Crust Three",17,"normal"))
        if len(self.msg_queue)>=3:
            self.t3.clear()
            self.t3.goto(-100,100)
            self.t3.write(self.msg_queue[-3], font=("Escalope Crust Three",17,"normal"))
        if len(self.msg_queue)>=4:
            self.t4.clear()
            self.t4.goto(-100,40)
            self.t4.write(self.msg_queue[-4], font=("Escalope Crust Three",17,"normal"))
        if len(self.msg_queue)>=5:
            self.t5.clear()
            self.t5.goto(-100,-20)
            self.t5.write(self.msg_queue[-5], font=("Escalope Crust Three",17,"normal"))
    def get_client(self):
        return self.my_client
##############################################################
##############################################################


###########################################################
#For now, leave the code below alone - you can play around#
#with it once you have a working view, trying to run your #
#chat view in different ways.                             #
###########################################################
if __name__ == '__main__':
    my_view=View()
    _WAIT_TIME=200 #Time between check for new message, ms
    def check() :
        #msg_in=my_view.my_client.receive()
        msg_in=my_view.get_client().receive()
        if not(msg_in is None):
            if msg_in==Client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) #Check recursively
    check()
    turtle.mainloop()



##m=TextBox()
##m.draw_box()
##a=SendButton()
##a.fun()
