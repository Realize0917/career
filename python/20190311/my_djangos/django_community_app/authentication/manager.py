from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **kwargs):
        user = self.create_user(
            username, email, password, **kwargs
        )
        # 定义superuser特有的字段
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


