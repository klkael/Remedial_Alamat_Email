email = input('Masukan Email yang Ingin Di-cek : ')

emailll = email.split('@')
# print(email)
asd = emailll[1].split('.')
# print(asd)
emailll.append(asd)
print(emailll)

alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
angka = [1,2,3,4,5,6,7,8,9]

def cek_email(email):
    email = email.replace('@', ' ')
    email = email.replace('.', ' ')
    split = email.split(' ')

    if len(split) != 3: 
        return 'tidak valid_1'
    else:
        x = emailll[0]
        y = emailll[2][0]
        z = emailll[2][1]
        if z.isalpha() == False or len(z) > 5:
            return 'tidak valid_2'    
        else:
            if y.isalnum():
                if x.isalnum() == True or '-' in x or '_' in x:
                    return 'valid_1'
                else:
                    return 'valid_2'
            else:
                return 'tidak valid_3'

#Angka di sebelah valid / tidak valid untuk cek error dan jalan dimana

print(cek_email(email))