from firebase_admin import auth


class UserService:

    @staticmethod
    def create(phone: str):
        user = auth.create_user(phone_number=phone)
        print('Sucessfully created new user: {0}'.format(user.uid))
