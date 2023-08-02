def prompt(
    prompt_text,
    validate=lambda x: x if x else None,
    default=None,
):
    """Prompt the user for input.

    Parameters
    ----------
    prompt_text : str
        Text displayed when prompting user for input.
    validate : callable, f(val)
        Called to validate the input.  If this function raises or
        returns None, try again.
    default : any
        Accept empty user input, and return this value as a default.  Note
        that this value is not validated.

    """

    def valid(s):
        if isinstance(s, str):
            s = s.strip()

        if not s and (default is not None):
            return default

        try:
            value = validate(s)
        except Exception:
            value = None

        if value is None:
            print("Invalid input; please try again.")

        return value

    default_flag = f" [{default}]" if default is not None else ""
    while (answer := valid(input(f"{prompt_text}{default_flag}: "))) is None:
        pass

    return answer
