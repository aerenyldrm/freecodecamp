def ConvertIntoSnakeCase(CamelOrPascalCase):
    snake_case_character_list = ['_' + character.lower() if character.isupper() else character for character in CamelOrPascalCase ]
    return "".join(snake_case_character_list).strip('_')

def Main():
    print(ConvertIntoSnakeCase("ALongAndComplexString"))

Main()