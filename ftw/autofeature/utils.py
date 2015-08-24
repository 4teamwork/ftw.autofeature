from path import Path


def find_package_by_module(module):
    egg_info = get_egg_info_path_by_module(module)
    if not egg_info:
        return None

    pkg_info = egg_info.joinpath('PKG-INFO')
    assert pkg_info.isfile(), '{0} is missing'.format(pkg_info)

    names = filter(lambda line: line.startswith('Name: '),
                   pkg_info.lines())
    assert names, 'No "Name: " in {0}'.format(pkg_info)
    return names[0].split(':')[1].strip()


def get_egg_info_path_by_module(module):
    path = Path(module.__file__)
    while path != '/':
        egg_info = get_egg_info_path_in_path(path)
        if egg_info:
            return egg_info

        path = path.parent

    return None


def get_egg_info_path_in_path(path):
    egg_infos = path.glob('*.egg-info') + path.glob('EGG-INFO')
    if egg_infos:
        return egg_infos[0]
    else:
        return None
