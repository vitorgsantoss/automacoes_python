def save_date(email,password):
    
    with open('.env','w') as arquivo:
        arquivo.write(f'EMAIL={email}\nPASSWORD={password}')
        return email, password


    