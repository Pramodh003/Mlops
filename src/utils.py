import sys

def error_message_handling(error,error_detail:str):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error has occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    return error_message    
    )
    
class CUstomMessage(Exception):
    def __init__(self,error_message,error_detail:str):
        super.__init__(error_message)
        self.error_message=error_message_handling(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message    