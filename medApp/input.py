import uuid
import json

def main(test=False):
    input_dict = dict()

    # For unit testing:
    if test == True:
        input_dict['UID'] = str(uuid.uuid4())
        input_dict['birth_date'] = 'xx-xx-xxxx'
        input_dict['pcp'] = 'Aetna'
        input_dict['sex'] = 'M'
    elif test == False:
        input_dict['UID'] = str(uuid.uuid4())
        input_dict['birth_date'] = input('Enter birth date as xx-xx-xxxx: ')
        input_dict['pcp'] = input('Enter PCP: ')
        input_dict['sex'] = input('Enter sex: ')

    json_object = json.dumps(input_dict, indent=4)

    return json_object

if __name__ == '__main__':
    main(test=False)