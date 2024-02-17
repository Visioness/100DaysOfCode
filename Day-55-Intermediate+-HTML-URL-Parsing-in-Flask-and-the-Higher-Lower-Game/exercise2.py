class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(func):
    def wrapper_function(*args, **kwargs):
        new_user = kwargs.get('user')
        if new_user.is_logged_in == True:
            func(user=new_user)
    return wrapper_function


@is_authenticated_decorator
def create_blog_post(user):
    print(f'This is {user.name}\'s new blog post.')


if __name__ == '__main__':
    new_user = User('Aygun')
    new_user.is_logged_in = True
    create_blog_post(user=new_user)