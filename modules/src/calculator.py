from templates.text import TextTemplate


# Evaluation function
def evaluate(sum):
    if '(' in sum:
        return evaluate(str(evaluate(sum.split('(', 1)[1].split(')', 1)[0])) + sum.split('(', 1)[1].split(')', 1)[1])
    elif '-' in sum:
        if sum[0] == '-':
            return evaluate(sum[1:]) * -1
        return evaluate(sum.split('-', 1)[0]) - evaluate(sum.split('-', 1)[1])
    elif '+' in sum:
        return evaluate(sum.split('+', 1)[0]) + evaluate(sum.split('+', 1)[1])
    elif '*' in sum:
        return evaluate(sum.split('*', 1)[0]) * evaluate(sum.split('*', 1)[1])
    elif 'x' in sum:
        return evaluate(sum.split('x', 1)[0]) * evaluate(sum.split('x', 1)[1])
    elif '/' in sum:
        return evaluate(sum.split('/', 1)[0]) / evaluate(sum.split('/', 1)[1])
    else:
        return float(sum)


def process(input, entities=None):
    # Create output structure
    output = {}

    try:
        # Extract sum from entities
        sum = entities['sum'][0]['value']

        sum_result = evaluate(sum)

        output['input'] = input
        output['output'] = TextTemplate('The answer is: '+ str(sum_result)).get_message()
        output['success'] = True

    except:
        output['success'] = False

    return output
