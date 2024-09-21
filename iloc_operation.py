# Description: This file contains the ILOCOperation class which is used to represent an ILOC operation.
class ILOCOperation:
    def __init__(self, line_number, opcode, reg1 = None, reg2=None, reg3=None):
        self.line_number = line_number  # Line
        self.opcode = opcode            # Opcode
        
        # Operand 1
        self.reg1_sr = reg1  
        self.reg1_vr = None   
        self.reg1_pr = None      
        self.reg1_nu = None
        
        # Operand 2
        self.reg2_sr = reg2     
        self.reg2_vr = None     
        self.reg2_pr = None     
        self.reg2_nu = None     
        
        # Operand 3
        self.reg3_sr = reg3    
        self.reg3_vr = None     
        self.reg3_pr = None    
        self.reg3_nu = None      

    def __repr__(self):
        # Format the operands using the format methods
        reg1 = self.format_op1(self.reg1_sr)
        reg2 = self.format_op2(self.reg2_sr)
        reg3 = self.format_op3(self.reg3_sr)

        # Format the operation into the desired style
        return (f"{self.opcode}\t"
                f"[ {reg1} ], "
                f"[ {reg2} ], "
                f"[ {reg3} ]")

    def format_op1(self, register):
        '''
        Format the first operand
        '''
        if register is None:
            return ''
        if self.opcode in ['loadI', 'output']:
            return f"val {register}"
        else:
            return f"sr{register}"
        
    def format_op2(self, register):
        '''
        Format the second operand
        '''
        if register is None:
            return ''
        else:
            return f"sr{register}"
    
    def format_op3(self, register):
        '''
        Format the third operand
        '''
        if register is None:
            return ''
        else:
            return f"sr{register}"
    