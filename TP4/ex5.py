from datetime import datetime
def ver_date(input_date):
    try:
        date = datetime.strftime(input_date, "%d%m%y")
        if date > datetime.now():
            raise valerror("/!\ date invalide/!\: la dateest pas valide")
        return True
    except valerror as e:
        print(str(e))
        return False
    except:
        print("/!\ DATE INVALIDE /!\.Veuillez entrezla date au format jjmmaaaa"
    return False

date_input - input("Selectionner un date sous le format : 'j}mmaaaa*: ")
 if  ver_date(date_input):

        print(f"La date (date_ input) est valide.")

 else:
        print(f"/!\ La date{date_input} est invalide. /!\" )