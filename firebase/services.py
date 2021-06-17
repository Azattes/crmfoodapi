from firebase_admin import auth


class UserService:

    @staticmethod
    def create(phone: str):
        try:
            user = auth.get_user_by_phone_number(phone_number=phone)
        except auth.UserNotFoundError:
            user = auth.create_user(phone_number=phone)
            print('Sucessfully created new user: {0}'.format(user.uid))
