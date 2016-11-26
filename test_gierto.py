import gierto


def test_convert_to_browser_url():
    convert = gierto.convert_to_browser_url
    assert (
        convert('git@github.com:suzaku/gierto.git') ==
        'https://github.com/suzaku/gierto'
    )
    assert (
        convert('https://my_github.com/suzaku/gierto.git') ==
        'https://my_github.com/suzaku/gierto'
    )
    assert (
        convert('https://my_github.com/suzaku/gierto') ==
        'https://my_github.com/suzaku/gierto'
    )
