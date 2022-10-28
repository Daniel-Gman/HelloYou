from time import sleep
def printsleep(sleeptime, txt):
    sleep(sleeptime)
    print(txt)

print("Gemaakt door Daniel Vermeulen")

printsleep(1.5, "Je bent op een feestje met vrienden en er is veel drank aanwezig")
printsleep(1.5, "het er staat een hoop drank op tafel, je twijfelt of je meer wilt drinken")
printsleep(1.5, "wat doe je?")
print("A: je feest door")
print("B: Je gaat voor een drankje")
vraagje1 = input("wat ga je doen? ").upper()
if vraagje1 == 'A':
    print("\n\nJe feest door, de rest van de avond word saai")
    printsleep(1.5, "jij krijgt geen leuk verhaal zonder wilde keuzes")
    print("YOU DIED OF BOREDOM!")
    exit()
elif vraagje1 == 'B':
    print("\n\nje loopt naar de tafel en besluit elke fles leeg te zuipen todat je zicht ineens weg is.")




printsleep(1.5, "Het is een donkere nacht, je bent net wakker na een hefitge nacht feesten en weet niet waar je bent.")
printsleep(1.8, "Je kijkt goed om je heen en merkt dat je in een groot bos zit. ook merk je nog iets anders op. ")
printsleep(3.0, "je merkt een fel licht, maar het is riskant om er heen te gaan.")
printsleep(1.5, "wat doe je?")
printsleep(1.5, "A: je blijft waar je bent en wacht op hulp ")
printsleep(1.5, "B: je gaat richting het velle licht ")


sleep(2.0); keuze1 = input("wat ga je doen? ").upper()
if keuze1 == 'A':
    printsleep(1.5, "\n\n Je besluit te blijven waar je bent en wacht op hulp ")
    printsleep(1.5, "de nacht nacht gaat voorbij en je bevriest dood. wat is het leven toch hard! ")
    printsleep(2.0, "YOU DIED")
elif keuze1 == 'B':
    printsleep(2.0, "\n\nJe besloot naar het licht te lopen. ")
    printsleep(2.0, "Je loopt naar het licht, het is een lange wandeling maar met moeite kom je eindelijk aan.")
    printsleep(2.0, "je ziet een eng en verlaten huis.")
    printsleep(1.0, "wat doe je?")
    printsleep(1.5, "A: je loopt het huis in ")
    printsleep(1.5, "B: Je besluit buiten te blijven")

    keuze2 = input("Wat ga je doen? ").upper()
    if keuze2 == 'A':
        printsleep(1.5, "\n\nJe loopt het huis in")
        printsleep(1.5, "je doet de deur open en hoort een rare krijs")
        printsleep(1.5, "je hoort het gekrijs steeds luider worden en besluit te moeten kiezen")
        printsleep(1.5, "A: loop de gang in")
        printsleep(1.5, "B: je loopt weer naar buiten")

        keuze3 = input("Wat ga je doen? ").upper()
        if keuze3 == 'A':
            printsleep(1.5, "\n\nJe loopt verder de gang in om erachter te komen waar het geluid vandaan komt")
            printsleep(1.5, "elke stap die je zet hoor je een heleboel gekraak van de houte vloer komen ")
            printsleep(1.5, "je komt aan het eind van de gang en ziet ineens een pop")
            printsleep(1.5, "wat doe je? ")
            printsleep(1.5, "A: Je pakt de pop ")
            printsleep(1.5, "B: Je negeert de pop en zoekt een kamer geschikt om in te overnachten")

            keuze4 = input("Wat doe je? ").upper()
            if keuze4 == 'A':
                printsleep(1.5, "\n\nJe besluit de pop te pakken")
                printsleep(1.5, "Je houd de pop vast maar ineens zie je dat de pop zn hoofd begint te draaien")
                printsleep(1.5, "De pop staart je recht in je ziel aan en er kruipen spinnen uit der ogen ")
                printsleep(1.5, "al gouw realiseer je je dat deze plek vervloekt is en je moet snel handelen ")
                printsleep(1.5, "A: ren naar de uitgang ")
                printsleep(1.5, "B: gooi de pop snel tegen de muur en zoek een veilige kamer")
                
                keuze5 = input("wat doe je? ").upper()
                if keuze5 == 'A':
                    printsleep(1.5, "\n\nJe rent naar de uitgang in paniek")
                    printsleep(1.5, "Je rent sneller en sneller todat je struikelt over je eigen voet")
                    printsleep(1.5, "je valt op je nek en sterft hulpeloos op de grond")
                    printsleep(1.5, "YOU DIED!")
                elif keuze5 == 'B':
                    print("\n\nje gooit de pop tegen de muur ")
                    printsleep(1.5, "de porselijn splat alle kanten op en plots zie je iets glinsteren")
                    printsleep(1.5, "je ziet twee sleutels, een rode en blauwe ")
                    printsleep(1.5, "welk pak je?")
                    printsleep(1.5, "A: je pakt de rode sleutel ")
                    printsleep(1.5, "B: je pakt de blauwe sleutel ")
                    printsleep(1.5, "C: Je pakt geen sleutel ")

                    keuze6 = input("Wat is je keuze? ").upper()
                    if keuze6 == 'A':
                        print("\n\nje kiest de rode sleutel ")
                        printsleep(1.5, "Je pakt de sleutel en gaat slapen ")
                        printsleep(1.5, "het is de volgende ochtend en je wilt de deur om naar buiten te gaan open doen")
                        printsleep(1.5, "je merkt dat de deur op slot zit en kan niet weg")
                        printsleep(2.0, "todat ")
                        printsleep(1.5, "Je realliseerd dat je een rode sleutel hebt en probeerd hem te gebruiken. ")
                        printsleep(1.5, "de sleutel komt vast te zitten en hoort een demonishe stem")
                        printsleep(1.5, " DAT WAS DE VERKEERDE KEUZE....!")
                        printsleep(1.5, "Je vliegt in de fik en sterft")
                        printsleep(1.5, "YOU DIED!")

                    elif keuze6 == 'B':
                        print("\n\nJe kiest de blauwe sleutel ")
                        printsleep(1.5, "Je pakt de sleutel en gaat slapen")
                        printsleep(1.5, "het is de volgende ochtend en je wilt de deur om naar buiten te gaan open doen")
                        printsleep(1.5, "je merkt dat de deur op slot zit en kan niet weg")
                        printsleep(2.0, "Todat")
                        printsleep(1.5, "Je realliseerd dat je een blauwe sleitel hebt en probeerd hem te gebruiken")
                        printsleep(1.5, "de sleutel blijkt te passen ")
                        printsleep(1.5, "je trekt de deur open en ontsnapt naar buiten")
                        printsleep(1.5, "je word plots verblind door een vel licht")
                        printsleep(1.5, "")
                        printsleep(3.0, "je staat plotseling niet meer in een bos, maar in een drukke straat")
                        printsleep(3.0, "je bedenkt al snel dat het kan zijn dat je alles hebt gehallicuneerd")
                        printsleep(3.0, "het zal vast niet komen aan al de alcohol die je op had bij het feestje")
                        printsleep(3.0, "je merkt op dat de straat waar je in bent naast je huis is")
                        printsleep(3.0, "je loopt je huis in en besluit in bed te liggen omdat je slecht hebt geslapen in het vervloekte huis")
                        printsleep(3.0, "je ligt in bed, denkend dat alles voorbij is. todat je plots een bekend soort gekrijs hoort")
                        printsleep(3.0, "je word nieuwsgierig")
                        printsleep(1.5, "A: je blijft slapen")
                        printsleep(1.5, "B: je besluit het krijs geluid te checken")

                        keuze7 = input("wat doe je? ").upper()
                        if keuze7 == 'A':
                            print("\n\nje valt in slaap")
                            printsleep(1.5, "*YOU SURVIVED*")
                        elif keuze7 == 'B':
                            print("\n\nJe laat zien dat je dommer bent dat een aardappel en checkt het geluid")
                            printsleep(1.5, "het is de pop van je halicunatie")
                            printsleep(1.5, "je checkt de pop, maar er gebeurd niks")
                            printsleep(1.5, "je loopt naar je bed omdat je besluit te moe te zijn voor meer gekkigheid ")
                            printsleep(1.5, "Je loopt naar je bed maar sterft plots aan een hartaanval")
                            printsleep(1.5, "YOU DIED!")


                    elif keuze6 == 'C':
                        print("\n\nje kiest geen sleutel")
                        printsleep(1.5, "Je besluit niks meer aan te raken voor de rest van de avond en zoekt een veilige slaap plaats")
                        printsleep(1.5, "je slaapt de hele nacht veilig en doet een poging om het huis uit te gaan")
                        printsleep(1.5, "Je loopt door de gang en probeerd de deur te openen")
                        printsleep(2.0, "TODAT")
                        printsleep(1.5, "de deur zit op slot")
                        printsleep(1.5, "je hebt geen sleutel om de deur te openen")
                        printsleep(1.5, "je doet een poging om de deur te forceren maar het lukt je niet")
                        printsleep(1.5, "tijdens het forceren voel je een tik op je schouder")
                        printsleep(1.5, "Je draait je langzaam om")
                        printsleep(3.0, "Je ziet ineens een grote zwarte bloedende demoon")
                        printsleep(1.5, "het was niet handig om hier te blijven. zegt de demoon")
                        printsleep(1.5, "de demoon valt je aan")
                        printsleep(1.5, "YOU DIED!")

            elif keuze4 == 'B':
                print("\n\nJe besloot de pop te negeren en een kamer te zoeken die geschikt is voor de nacht ")
                printsleep(3.0, "je vind een veilige kamer en valt in slaap op de stoffige vloer")
                printsleep(3.0, "je word wakker de volgende ochtend en besluit naar buiten te willen gaan")
                printsleep(3.0, "terwijl je door de gang loopt opweg naar de deur merk je dat de huis er heel anders uit ziet dan je je kan herinneren")
                printsleep(3.0, "je loopt de deur uit en word verblind door een vel licht")
                printsleep(3.0, "je staat plotseling niet meer in een bos, maar in een drukke straat")
                printsleep(3.0, "je bedenkt al snel dat het kan zijn dat je alles hebt gehallicuneerd")
                printsleep(3.0, "het zal vast niet komen aan al de alcohol die je op had bij het feestje")
                printsleep(3.0, "je merkt op dat de straat waar je in bent naast je huis is")
                printsleep(3.0, "je loopt je huis in en besluit in bed te liggen omdat je slecht hebt geslapen in het vervloekte huis")
                printsleep(3.0, "je ligt in bed, denkend dat alles voorbij is. todat je plots een bekend soort gekrijs hoort")
                printsleep(3.0, "je word nieuwsgierig")
                printsleep(1.5, "A: je blijft slapen")
                printsleep(1.5, "B: je besluit het krijs geluid te checken")

                keuze6 = input("wat doe je? ").upper()
                if keuze6 == 'A':
                    print("\n\nje valt in slaap")
                    printsleep(1.5, "*YOU SURVIVED*")
                elif keuze6 == 'B':
                    print("\n\nJe laat zien dat je dommer bent dat een aardappel en checkt het geluid")
                    printsleep(1.5, "het is de pop van je halicunatie")
                    printsleep(1.5, "je checkt de pop, maar er gebeurd niks")
                    printsleep(1.5, "je loopt naar je bed omdat je besluit te moe te zijn voor meer gekkigheid ")
                    printsleep(1.5, "Je loopt naar je bed maar sterft plots aan een hartaanval")
                    printsleep(1.5, "YOU DIED!")
        elif keuze3 == 'B':
            printsleep(1.5, "\n\nje loopt in angst naar buiten waar je een erge verassing te wachten staat.")
            printsleep(2.0, "je ziet een groep wolfen buiten staan, je rent in angst terug naar de deur om het huis in te vluchten. maar plots hoor je een geluidje ")
            printsleep(3.0, "*click*")
            printsleep(2.0, "de deur is op slot. je hoort een vage lach terwijl een groep wolfen op het punt staat om je te verslinden.")
            printsleep(1.5, "wat doe je? ")
            print("A: je rent weg")
            print("B: Je probeerd ze te aaien")

            antwoordje1 = input("Wat is je keuze? ").upper()
            if antwoordje1 == 'A':
                print("\n\nJe besluit weg te rennen, alleen de wolfen waren sneller dan je dacht. je word opgegeten")
                printsleep(1.5, "YOU DIED!")
            elif antwoordje1 == 'B':
                print("\n\nJe probeert de wolfen te aaien, de wolfen vinden het aaien fijn. je overleeft ze")
                printsleep(1.5, "TODAT")
                printsleep(1.5, "Er valt ineens een piano op je hoofd en je gaat dood aan een hersenschudding")
                printsleep(1.5, "YOU DIED!")
    elif keuze2 == 'B':
        printsleep(1.5, "\n\nJe blijft buiten en het word ijskoud")
        printsleep(1.5, "je maakt het heel moeilijk voor jezelf, waarom ben je nou zo eigenwijs. ")
        printsleep(2.0, "Je bevriest bijna dood en moet warmte vinden ")
        printsleep(1.5, "wat doe je?")
        printsleep(1.5, "A je zoekt bladeren voor een simpel warm deken om te maken ")
        printsleep(1.5, "Je blijft waar je bent ")

        antwoordje2 = input("Wat is je keuze? ").upper()
        if antwoordje2 == 'A':
            print("\n\nJe besluit bladeren te zoeken ")
            printsleep(1.5, "Tijdens je zoektocht word je begroet door een hoop boze uilen")
            printsleep(1.5, "je raakt in paniek wat doe je?")
            printsleep(1.5, "A: Je gaat ze aaien")
            printsleep(1.5, "B: Je rent weg")
            
            antwoordje3 = input("Wat doe je? ").upper()
            if antwoordje3 == 'A':
                print("\n\nJe aait de uilen, ze respecteren het niet, je word dood gepikt.")
                printsleep(1.5, "YOU DIED!")
            elif antwoordje3 == 'B':
                print("\n\nJe rent weg, maar t heeft geen nut. de boze uilen halen je in en pikken je dood ")
                printsleep(1.5, "YOU DIED")

        elif antwoordje2 == 'B':
            print("\n\nJe bevriest dood")
            printsleep(1.5, "YOU DIED!")