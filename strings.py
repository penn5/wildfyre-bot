from babel import Locale

STRINGS = {"en_GB":
    {
      "start": "Welcome to the Wildfyre bot. It's still in beta, so please report all bugs with /bug",
      "auth": "To log in, please blah blah blah",
      "bug": "Bug has been reported to developers.",
    }
    
  }

def get(message, string):
    requested_locale = [str(message.from_user.locale), "en_GB"]
    available_locales = list(filter(lambda x: string in STRINGS[x].keys(), STRINGS.keys()))
    chosen_locale = Locale.negotiate(requested_locale, available_locales)
    return STRINGS[str(chosen_locale)][string]
