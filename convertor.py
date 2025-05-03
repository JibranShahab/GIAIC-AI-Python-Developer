# coverter App
# first create a function

# set parameters
def converter_kg(value: float, unit_from:str, unit_to:str):
    print("value", value)
    print("unit_from", unit_from)
    print("unit_to", unit_to)
#  set arguivment

    if unit_from == "kilometer" and unit_to == "meter":
        return value*1000
    elif unit_from =="meter" and unit_to == "kilometer":
        return value * 0.001
    elif unit_from == "kilogram" and unit_to == "gram":
        return value *1000
    elif unit_from == "gram" and unit_to == "kilogram":
        return value *0.001

    

# 1 kilometer = 1000 meter
# 1 meter =0.001 kilogram
# 1 kilogram = 1000grm
# 1 gram = 0.001 kilogram

result = converter_kg(1.5,"kilometer","meter")
print("Result value is",result)

result_1 = converter_kg(10,"meter","kilometer")
print("Result value is",result_1)

result_2 = converter_kg(1,"kilogram","gram")
print("Result value is",result_2)

result_3 = converter_kg(300,"gram","kilogram")
print("result value is" ,result_3)