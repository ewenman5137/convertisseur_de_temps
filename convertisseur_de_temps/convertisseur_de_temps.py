#==========================================================================================================#
# Cette fonction sert à retourner le temps d'exécution converti pour éviter de faire la conversion.        #
# Elle prend en paramètre le temps d'exécution et retourne directement la phrase avec le temps et l'unité. #
#==========================================================================================================#

def converti_le_temps(temps):
    temps = int(temps)
    if temps > 1:
        if temps > 60:
            # minute
            if temps > 3600:
                # heure
                if temps > 86400:
                    # jours
                    if temps > 2_592_000:
                        # mois 
                        if temps > 31_104_000:
                            #années
                            temps = f"{temps //31_104_000} années {temps % 31_104_000//2_592_000} mois"
                        else:
                            temps = f"{temps //2_592_000} mois {temps%2_592_000//86400} jours"
                    else:
                        temps = f"{temps//86400} jours {temps%86400//3600} heures"
                else:
                    temps = f"{temps//3600} heures {temps%3600//60} minutes"
            else:
                temps = f" {temps//60} minutes {temps%60} secondes"
        else:
            temps = f"{temps} secondes "
    else:
        temps = "moins de 1 seconde"
    return(temps)
