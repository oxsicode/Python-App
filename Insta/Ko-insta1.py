from instagrapi import Client

cl = Client()

try:
    cl.login('ilangovetri@outlook.com', '@mana7')
    info = cl.account_info()
    pk = info.pk
    followers = cl.user_followers('51036093600').keys()
    if pk in followers:
        print('Success')
    else:
        cl.account_edit(username='my_1life_z0e0r0.my_0rule.1', full_name='Mukesh')
        cl.account_set_biography('நீ Bio வில் போட்ட Caption யை நான் தவறாக புரிந்து கொண்டேன். \n Sorry Kowshika.')
        cl.account_change_picture('/home/mana/Upload/gray.jpg')
        cl.user_unfollow(51036093600)
        cl.user_follow(51036093600)
        
except Exception as e:
    print(e)
