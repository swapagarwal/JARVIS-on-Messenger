import modules

def test_calculator():
    
    input = ""
    entities = {}
    
    #case 1: addition & substration
    entities['operator'] = '+'
    entities['operand'] = [0, 0]
    entities['operand'][0] = 32.34
    entities['operand'][1] = -32.34
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(0 == output)
    entities['operator'] = '-'
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(64.68 == output)
    
    #case 2: multiply & division
    entities['operator'] = '/'
    entities['operand'] = [0, 0]
    entities['operand'][0] = 32.34
    entities['operand'][1] = -32.34
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(-1 == output)
    entities['operator'] = '*'
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(-1045.8756 - output < 0.001)
    
    #case 3: pow & sqrt
    entities['operator'] = 'pow'
    entities['operand'] = [0, 0]
    entities['operand'][0] = 3
    entities['operand'][1] = 0
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(1 == output)
    entities['operator'] = 'sqrt'
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(1.732 - output < 0.001)
    
    #case 4: sin & asin
    entities['operator'] = 'asin'
    entities['operand'] = [0, 0]
    entities['operand'][0] = 0.5
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(math.pi/6 - output < 0.001)
    entities['operator'] = 'sin'
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(0.4794 - output < 0.001)
    
    #case 5: cos & acos
    entities['operator'] = 'cos'
    entities['operand'] = [0, 0]
    entities['operand'][0] = math.pi/3
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(0.5 - output < 0.001)
    entities['operator'] = 'acos'
    entities['operand'][0] = 0.5
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(1.047 - output < 0.001)
    
    #case 6: tan & atan
    entities['operator'] = 'tan'
    entities['operand'] = [0, 0]
    entities['operand'][0] = math.pi/4
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(1 - output < 0.001)
    entities['operator'] = 'atan'
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(0.6658 - output < 0.001)
    
    #case 7: ln & log
    entities['operator'] = 'ln'
    entities['operand'] = [0, 0]
    entities['operand'][0] = math.e
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(1 - output < 0.001)
    entities['operator'] = 'log'
    entities['operand'][1] = math.e
    result = process(input, entities)
    success = result['success']
    output = result['output']
    assert(True == success)
    assert(1 == output)
    
    #case 8: invalid input
    entities['operator'] = 'invalid'
    entities['operand'] = [0, 0]
    result = process(input, entities)
    success = result['success']
    assert(False == success)
    
    print("all tests passed")
