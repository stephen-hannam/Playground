def get_country(iso_code=None):
    if type(iso_code) != str:
        raise TypeError('iso_code needs to be a string')
    elif len(iso_code) != 2:
        raise TypeError('iso_code needs to be 2 chars')
    country_dict = {
        "DK":{
            "name": "Denmark"
        }
    }
    if iso_code in country_dict:
        return True, country_dict[iso_code]
    else:
        return False, None
