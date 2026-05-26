from utilities import input_auth as auth

class StudentService:

    def __init__(self):
        pass

    @staticmethod
    def name_is_valid(name: str) -> bool:
        return (not auth.InputAuth.has_spec_char(name)
                and not auth.InputAuth.has_digit(name)
                )

    @staticmethod
    def email_is_valid(email: str) -> bool:
        domain = '@pnhs.edu.ph'

        if len(email) < 23:
            cut = len(email) - len(domain)

            return (not auth.InputAuth.has_space(email[:cut])
                    and not auth.InputAuth.has_spec_char(email[:cut])
                    and email.endswith(domain)
                    )

        return (not auth.InputAuth.has_space(email[:len(domain)])
                and not auth.InputAuth.has_spec_char(email[:len(domain)])
                and email.endswith(domain)
                )

    @staticmethod
    def password_is_valid(password: str) -> bool:
        return (auth.InputAuth.has_letter(password)
                and auth.InputAuth.has_digit(password)
                and auth.InputAuth.has_spec_char(password)
                and not auth.InputAuth.has_space(password)
                and 8 < len(password) < 20
                )