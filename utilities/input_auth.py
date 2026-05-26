class InputAuth:

    @staticmethod
    def has_digit(user_input: str) -> bool:
        for ch in user_input:
            if ch.isdigit():
                return True

        return False

    @staticmethod
    def has_letter(user_input: str) -> bool:
        for ch in user_input:
            if ch.isalpha():
                return True

        return False

    @staticmethod
    def has_space(user_input: str) -> bool:
        for ch in user_input:
            if ch.isspace():
                return True

        return False

    @staticmethod
    def has_spec_char(user_input: str) -> bool:
        for ch in user_input:
            if not ch.isalnum() and not ch.isspace():
                return True

        return False


