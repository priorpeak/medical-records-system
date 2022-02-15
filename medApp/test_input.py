import input
import json

def test_input():
    json_object = input.main(test=True)

    input_dict = json.loads(json_object)

    assert 'UID' in input_dict and 'birth_date' in input_dict \
        and 'pcp' in input_dict and 'sex' in input_dict