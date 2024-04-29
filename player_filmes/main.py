from dotenv import find_dotenv, dotenv_values
from telas import login, filmOrSerie


if __name__ == '__main__':
    if not find_dotenv():
        login()
    env_vars = dotenv_values('.env')
    
    email = env_vars.get('EMAIL')
    password = env_vars.get('PASSWORD')

    filmOrSerie(email, password)

    