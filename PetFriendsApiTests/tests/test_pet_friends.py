from api import PetFriends
from settings import valid_email, valid_password
import os
from settings import notvalid_email, notvalid_password


pf = PetFriends()

def test_get_api_key_for_novalid_email(email=notvalid_email, password=valid_password):
    status, result = pf.get_api_key(email,password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_novalid_password(email=valid_email, password=notvalid_password):
    status, result = pf.get_api_key(email,password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_novalid_email_password(email=notvalid_email, password=notvalid_password):
    status, result = pf.get_api_key(email,password)
    assert status == 200
    assert 'key' in result

def test_get_list_of_pets_with_filter(filter='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_post_add_new_pet_without_name(animal_type='camel', age='5', pet_photo='images/soft.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['animal_type'] == animal_type

def test_post_add_new_pet_big_age(name='Mynton', animal_type='camel', age='54544897984561211516584845', pet_photo='images/soft.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_put_update_pet_without_age(name='Минтон', animal_type='верблюд'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) > 0:
        status, result = pf.put_update_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception('There is no my pets')

def test_put_update_pet_wrong_auth_key(name='Минтон', animal_type='верблюд', age=6):
    _, auth_key = pf.get_api_key(valid_email, notvalid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) > 0:
        status, result = pf.put_update_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception('There is no my pets')

def test_delete_pet_with_wrong_id():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    pet_id = my_pets['pets'][5]['id']
    status, _ = pf.delete_pet(auth_key,pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    assert status == 200
    assert pet_id not in my_pets.values()

def test_delete_pet_with_last_id():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    pet_id = my_pets['pets'][-1]['id']
    status, _ = pf.delete_pet(auth_key,pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    assert status == 200
    assert pet_id not in my_pets.values()
