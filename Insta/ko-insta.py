from instagrapi import Client

cl = Client()

try:
    cl.login('jeyabaskar46@outlook.com', '@mana7')
    info = cl.account_info()
    pk = info.pk
    followers = cl.user_followers('51036093600').keys()
    if pk in followers:
        print('Success')
    else:
        cl.account_edit(username='jeya.basssk', full_name='Jeya Baskar')
        cl.account_set_biography('லூசு உன்னைய திட்டி திட்டியே எனக்கு உன் மேல காதல் வந்துருச்சு. இதுவரைக்கும் உன்னை விரட்டியதே content எழுதத்தான். இனிமேல் ........')
        cl.account_change_picture('/home/mana/Upload/gray.jpg')
        cl.user_unfollow(51036093600)
        cl.user_follow(51036093600)
        
except Exception as e:
    print(e)
    
else:
    print('Added info  Successfull to Instagram.')
