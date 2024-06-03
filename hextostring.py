hex_values = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d" 
byte_values = bytes.fromhex(hex_values)
result_string = byte_values.decode('utf-8')
 
print(result_string)
print(type(result_string))
