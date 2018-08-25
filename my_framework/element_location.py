
def location_element(da,location):
    """

    :param da:
    :param location: 'elemm=>traits/ONE_HAND',文件名+=>+位置
    :return:
    """
    element_file_name = location.split('=>')[0]
    print(element_file_name)
    locations = location.split('=>')[1]
    if '/' in locations:
        locations_list = locations.split('/')
        for i in locations_list:
            da = da[i]
        return print(da)
    else:
        return da[locations]

if __name__ == '__main__':
    #实列
    da = {'name': 'Silenthand Olleander',
            'race': 'Human',
            'traits': {'ONE_HAND':'beijing'}
            }
    a = 'elemm=>traits/ONE_HAND'
    location_element(da,a)
