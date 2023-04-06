from rich import print
from os import system
from random import choice


def genEurope_Paper3(section) -> str:
    """This function generates the essay questions for the Paper 3 of the Europe section of the IB History course"""

    # These are the randomized terms that will be used to generate the command term in the questions
    command_terms = [
        "Analyze",
        "Discuss",
        "Evaluate",
        "Examine",
        "Explain",
    ]

    # These are the randomized terms that will be used to generate the questions
    section_terms = [
        ["the establishment of royal government in England and France", "the characteristics of royal government in England and France", "the changing nature of royal government in England and France",
            "the policies in England, Ireland and Gascony by Henry II (1154-1189) of the Angevin Commonwealth", "the extension of the royal demesne and power in France under the Capetians (1108-1223)", "the expansion of Capetian power under Louis VI, Louis VII and Phillip II"],
        ["the Reasons for hostility to Muslim", "Reasons for Christian opposition to the Muslim states in Spain", "Continuous conflict between the Christian-ruled and Muslim-ruled states in Spain",
            "The role and contribution of Jews in medieval Europe", "The reasons for persecution of Jews", "the impact of persecution of Jews", "the impact of Jewish persecution on society"],
        ["the Succession crises in England", "either the causes, course, or impact and significance of the Hundred Years War 1337-1360 and 1369-1389", "the reasons for the re-emergence of war, in the Hundred Years War 1415-1453", "the importance of Aquitaine in the Hundred Years War 1415-1453", "the reasons for the outcome in the Hundred Years War 1415-1453", "the impact in England and France from the Hundred Years War 1415-1453",
            "The rise and fall of ducal Burgundy", "the Crisis of monarchy and challenges to royal authority in 15th-century England and France", "the nature of kingship and challenges for either Henry VI (1422-1461), Edward IV (1461-1483), or Louis XI (1461-1483)", f'the {choice(["causes of","events in","impact on England including impact on government and royal authority from"])} The Wars of the Roses'],
        ["the Origins, causes and development of the Renaissance in Italy", "the Forms of government in Italian city states",
            f"the importance of patronage from {choice(['the papal states', 'Lorenzo de Medici and patronage from Ludovico Sforza'])} during the Renaissance", "Cultural and intellectual developments during the Renaissance", "The renaissance's spread to Burgundy and Germany", "the spread and impact of the Renaissance to one European country"],
        ["the Motives for exploration and reasons for its increase in the 15th century", f"the role of {choice(['patronage, including role and significance of Henry the Navigator', 'developments in shipbuilding, cartography and navigation'])} as 'enablers' of exploration", f"the {choice(['significance of', 'consequences of', 'impact on indigenous peoples from due to'])} Portuguese exploration of the west coast of Africa",
         f"the {choice(['significance of', 'consequences of', 'impact on indigenous peoples due to'])} the exploration of the New World", f"the {choice(['significance of', 'consequences of', 'impact on indigenous peoples due to'])} the exploration of the Indian Ocean", 'The significance and impact of the Treaty of Tordesillas (1494)', 'the impact on Europe from the "Columbian Exchange"'],
        ["The state of the Catholic church in Europe at the start of the 16th century, and reasons for criticism", "The religious ideas and impact of Luther and Calvin", "Reasons for the successful spread of Lutheran ideas in Germany to 1547, including the attitudes of the German princes",
            "Religion and conflict in Germany including the Peasants’ War; the Schmalkaldic League and the Peace of Ausburg (1555)", "The role of spread and impact of Protestant ideas in any one of England, Scotland, France or the Netherlands", f" {choice(['the role of spiritual movements in the', 'the role of the Jesuits and other Catholic orders in the', 'the role of clerical education and discipline in the', 'the role of the Council of Trent (1545-1563) in the'])} The Catholic Reformation"],
        ["The goals and development of Enlightenment ideas including the Scientific Revolution", "the Enlightenment ideas and their political impact in any two of Germany, England, Scotland, France, Spain, the Dutch Republic or Italy)",
            f"the {choice(['the nature of the rule of', 'the extent of the power of', 'foreign policy of'])} any two absolutist monarchs", f"the {choice(['policies and their impact from', 'extent of change of'])} any two enlightened despots", f"Social and economic change in the Enlightenment era including but not limited to {choice(['growth of cities', 'agricultural change'])}", "Monarchy, patronage and the arts in the Enlightenment"],
        [f"the role of the monarchy in the Crisis of the Ancien Régime with respect to the {choice(['intellectual', 'political', 'social', 'financial', 'economic'])} challenges", f"the transition from Monarchy to republic with respect to the {choice(['causes and significance of the Revolution', 'the 1791 Constitution', 'the fate of the monarchy', 'the Thermidorean reaction'])}",
         f"The political, social and economic impact of the{choice(['Revolution','French revolutionary wars (1792-1799)'])}", "Establishment of, nature of, and collapse of the Directory (1795-1799)", "impact of Napoleon’s domestic and foreign policies on France", "collapse of the Napoleonic Empire"],
        ["The Bourbon restoration, the Congress of Vienna and its impact on France", "The reigns of Louis XVIII and Charles X with respect to politics and society (1815-1830)", "the reasons for the collapse of the July monarchy", "the emergence of Louis-Napoleon and the Second Empire",
         f"{choice(['domestic policies', 'stability', 'opposition', 'periods of reform', 'foreign policies, including the ' + choice(['Crimean War', 'interventions in Italy and Mexico'])])} in the Second Empire under Napoleon III", "stability and crises in the Third Republic (1871-1914)"],
        ["Social protest (1815-1848)", "the reasons for, and consequences of, the Reform Act (1832, 1867 and 1884-1885) and impact on the political parties", "the condition of the working class during the Industrial Revolution with respect to urban poverty and social reforms", "Disraeli, Gladstone and Salisbury regarding either domestic policies or the Irish Question",
         "Early 20th-century Britain regarding either the emergence of the Labour Party, Lloyd George and social reforms or the “People's Budget” and the Parliament Act", f"Pre-war unrest and protest in Edwardian Britain with respect to {choice(['the women’s suffrage movement', 'Ireland', 'trade unions'])}"],
        ["the impact of the Congress of Vienna on Italy", "Austrian dominance in Italy", "the role of Metternich in Italy", " the role of nationalism and liberalism in Italy", "the attempted revolutions in Italy between 1820 and 1844", "the impact of the Congress of Vienna on Germany", "nationalism and liberalism in the Vormärz period", "economic and social change before 1848 in Germany", "1848-1849 Revolutions—causes, nature, defeat and consequences",
            "Cavour and Garibaldi in the Unification of Italy (1849-1871)", "the role of foreign influence in Italy", "The rise of Prussia and the decline of Austria (1815-1866)", f"the role of Bismarck in the unification of Prussia with respect to {choice(['diplomatic', 'economic', 'military'])} reorganization", " Bismarck's domestic policies in Germany including the Kulturkampf and the anti-socialist campaign (1871-1890)"],
        ["the extent of reform under Alexander II (1855-1881)", f"Policies of Alexander III (1881-1894) and Nicholas II (1894-1917) regarding {choice(['economic modernization', 'tsarist repression and the growth of opposition'])}", "Causes of the 1905 Revolution (including social and economic conditions and the significance of the Russo-Japanese War",
         "the consequences of the 1905 Revolution (including Stolypin and the Dumas)", "the impact of the First World War and the final crisis of autocracy in February/March 1917", "1917 Revolutions", f"Lenin’s Russia/Soviet Union with respect to {choice(['the consolidation of new Soviet state', 'Civil War', 'War Communism', 'New Economic Policy (NEP)', 'terror and coercion', 'foreign relation'])}"],
        ["Diplomacy in Europe and the changing balance of power after 1871", "the imperial expansion in Africa and Asia, and its impact on European diplomacy", " the Congress of Berlin and European Alliance system", "Domestic conditions that impacted on German foreign policy under Kaiser Wilhelm II", "the impact/influence off German foreign policy under Kaiser Wilhelm II on other countries, including Britain, France, Russia and Austria-Hungary", "the short-term and long-term causes of the First World War", "the Alliance system in refernce to the First World War",
            "the decline of the Ottoman Empirein reference to the First World War", "German foreign policyin reference to the First World War", f"nationalism in {choice(['Austria-Hungary','Russia', 'the Balkans'])} in reference to the First World War", "Impact of the First World War on civilian populations of two countries from the region European between 1914 and 1918", f"Factors leading to the defeat of Germany and the other Central Powers, and to the victory of the Entente Powers, include reference to {choice(['strategic errors',' economic factors','the  entry and role of the US', 'domestic instability in the Central Powers'])}"],
        ["the constitutional, political, economic/financial and social issues in Weimar Germany (1918-1933)", "the initial challenges (1918-1923) in Weimar Germany", "the “Golden Era” under Stresemann in Weimar Germany (1924-1929)", "the crisis years and the rise of Hitler in Weimar Germany (1929-1933)", "Hitler’s pre-war domestic policies, including economic, social and political policies", "nature of the Nazi state", " the extent of resistance to the Nazis",
         "Mussolini’s pre-war domestic policies, including economic, social and political policies", "the nature of the fascist state", "political, social and economic conditions in Spain (1918-1939)", "polarization and political parties under the Second Republic", "causes of the Civil War", "reasons for nationalist victory under Franco", "domestic political, economic and social developments in one European country (other than Germany, Italy or Spain) in the inter-war years."],
        ["issues and responses with two Peace settlements (1919-1923)", "The League of Nations and Europe: successes and failures", "developments in the successor states of central and eastern Europe", "Italian and German foreign policies (1919-1941): aims, issues and extent of success", "the aims, issues and extent of success of Collective security and appeasement (1919-1941)",
         "the role of British, French and Russian/Soviet foreign policies (1919-1941) in regards to collective security", "Causes of the Second World War and the development of European conflict (1939-1941)", "reasons for Axis defeat in 1945 and for Allied victory", "the role of economic, strategic and other factors during the Second World War", "Impact of the Second World War on civilian populations in any two countries between 1939-1945"],
        ["Stalin’s policies of collectivization and the Five-Year Plans", "government and propaganda under Stalin", "the purges and the Great Terror",
            "The impact of the Great Patriotic War (1941-1945)", "the political and economic developments in the post-war Soviet Union (1945-1953)", "Khrushchev's and Brezhnev's domestic policies and foreign relations", "either Gorbachev's aims, policies or extent of success regarding the political developments and change during the Transformation of the Soviet Union (1985-1991)", "the role and policies of Yeltsin"],
        ["the emergence of the Cold War and its impact on Germany",  "Post-war problems and political and economic recovery in western Europe", "the reconstruction of France and West Germany (1945-1963) and the impact of the Marshall Plan", "the role of Adenauer regarding the German “economic miracle” and the role of de Gaulle regarding the “Les Trente Glorieuses” in France", "domestic policies in West Germany (1963-1990)", "the challenge of Baader Meinhof Group/Red Army Faction in West Germany (1961-1990)",
         " social and cultural change in West Germany from 1949 to 1990", ": Franco’s regime and the transition to, and establishment of, democracy under Juan Carlos up to 1982", "political, economic and social developments in Spain (1982-2000)", "political, social and economic changes in one western or northern European country (other than France, the Federal Republic of Germany and Spain) between 1945-2000"],
        ["the motives, extent and nature of Soviet control in central and eastern Europe (1945-1955)", " politics, economies (COMECON) and the Warsaw Pact (1945-1955)", "Yugoslavia’s challenge to Soviet control under Tito", "Support and cooperation, repression and protest (1945-1968) in either East Germany, Poland, Hungary, or Czechoslovakia", "Acceptance of, and opposition to, Soviet control in central and eastern Europe (1968-1989) in two of the following states: East Germany, Poland, Hungary, Czechoslovakia, Romania or Bulgaria",
         "one of either the causes, developments and consequences regarding the collapse of Soviet control in central and eastern Europe", "the reasons for, and consequences of the Balkan Conflicts in the 1990s", "role and policies of Milosevic in the Balkan Conflicts in the 1990s", "the economic, social and political challenges of the post-communist era in any one central or eastern European country (1989-2000)"]
    ]

    term = choice(command_terms)
    text = choice(section_terms[section-1])
    return (f'[blue]{term}[/blue] [green]{text.lstrip()}.[/green]')


def genWorldHistoryQuestion(topic) -> str:
    """This function generates a question for the Paper 3 exam in the Europe region."""

    #These are the terms that will be used to generate the questions
    command_terms = [
        "Analyze",
        "Compare",
        "Compare and Contrast",
        "Contrast",
        "Discuss",
        "Evaluate",
        "Examine",
        "Explain",
    ]

    #These are the randomized terms that will be used to generate the questions
    section_terms = [
        ["changes in social structures and systems in two societies, each chosen from a different region", "the impact of population change in two societies, each chosen from a different region", "the role of women in two societies, each chosen from a different region", "the nature and development of trade in two societies, each chosen from a differnt region", "the changes in travel and transportation in two societies, each chosen from a differnt region", "the role and significance of key individuals in two societies, each chosen from a differnt region", "the factors affecting the transmission of ideas and cultures in two societies, each chosen from a differnt region",
            "the significance and impact of artistic and cultural developments in two societies, each chosen from a differnt region", "the developments in science and technologyin two societies, each chosen from a differnt region", f"{choice(['the religious leaders in government and administration', 'disputes between rulers and religious leaders'])} in two societies, each chosen from a differnt region", "the treatment of religious minorities in two societies, each chosen from a differnt region", "the spread of religion in two societies, each chosen from a differnt region"],
        [f"the affect of {choice(['dynastic disputes', 'territorial disputes', 'religious disputes'])} as a cause for two wars in the period 750-1500 each chosen from a different region.", f"{choice(['economic', 'ideological', 'political', 'religious', 'long-term', 'short-term', 'immediate'])} causes with respect to to two wars in the period 750-1500, each chosen from a different region.",
         f"{choice(['role and significance of leaders', 'methods for raising armies', 'how logistics, tactics and organization of warfare', 'the significance of women in war'])} with respect to two wars in the period 750-1500, each chosen from a different region", f"{choice(['conquest, boundary and dynastic changes', 'treaties and truces', 'political repercussions', 'economic, social, religious and cultural changes', 'demographic changes and population movements'])} as a result of two wars in the period 750-1500, each chosen from a different region"],
        [f"{choice(['methods used to legitimize, consolidate and maintain rule', 'nature of power and rule', 'aims and achievements', 'reasons for expansion', 'methods used to expand power', 'invasion and settlement'])} for two rulers, each chosen from a different region",
         f"{choice(['models and methods of government and administration', 'sources of religious and secular law', 'administration and interpretation of law', 'role and duties of officials', 'role of nobility and the elite'])} for two rulers, each chosen from a different region", f"{choice(['successes and failures', 'internal and external challenges to power', 'rebellion and/or political opposition as challenge', ' rivalries and issues of succession as challenge'])} for two rulers, each chosen from a different region"],
        [f"{choice(['the role of women','population expansion and movements', 'the treatment of minorities', 'development of, and changing patterns of, trade', 'role and impact of merchants and travellers'])} during the period 1400-1700",
         f"the {choice(['impact of artistic, cultural and intellectual movements', 'impact of cross-cultural exchanges', 'social and cultural impact of scientific and technological developments', 'role and significance of key intellectual/scientific figures'])} during the period 1400-1700", f"{choice(['the interactions and relationships between religion and the state', 'religious expansion and conversion', 'religious division, conflict, discrimination and persecution'])} during the period 1400-1700"],
        [f"{choice(['the ascendancy and decline of two states in two differnt regions', 'methods and models of government for two states in two differnt regions', 'reasons for changes in political structures/political organization for two states in two differnt regions', 'domestic policies by two states in two differnt regions', 'treatment of subjects by two states in two differnt regions', 'ideologies of two rulers in two differnt regions', 'the nature of rule of two rulers in two differnt regions', 'ambition and achievements of two rulers in two differnt regions', 'legitimacy of two rulers in two differnt regions', 'successes and failures of two rulers in two differnt regions'])}",
         f"{choice(['the political and economic reasons for expansion', 'structures of government and political structures', 'the models and methods of government', 'the relationship between religion and the state', 'the establishment and expansion of colonial empires', ' political and economic reasons for expansion and acquisition of territory', 'the structures of government and the political structure in the colonial world', 'the colonial race'])} with reference to two states each chosen from a differnt region", f"{choice(['the methods of maintaining power', 'treatment of opposition', ' challenges to power and how successfully those challenges were overcome,', 'colonial resistance, colonial rebellions and their impact', 'issues of succession'])} in two states each chosen from a differnt region"],
        [f"{choice(['ideological and political causes', 'economic causes', 'economic causes with referernce to competition for resources as a cause', 'the religious causes', 'the short-term causes', 'the long-term causes'])} of two wars in two differnt regions", f"impact of {choice(['and role of leaders', 'raising armies with respect to military service and mercenaries', 'raising armies with respect to taxes', 'raising armies', 'strategies in land and/or sea', 'technological developments', 'the influence and/or involvement of foreign powers'])} with respect to the outcome of two wars in two differnt regions",
         "the successes and/or failures of peacemaking in two wars in two differnt regions", f"the {choice(['economic','political', 'territorial', 'social', 'religious'])} impacts of war in two differnt regions", f"{choice(['demographic changes', 'population movements'])} as a result of two wars in two differnt regions"],
        [f"{choice(['the causes and enablers of industrialization', 'the causes and enablers of industrialization with reference to the availability of human and natural resources', 'the causes and enablers of industrialization with reference to political stability', 'the causes and enablers of industrialization with reference to infrastructure', 'role and significance of technological developments with respect to industrialization', 'role and significance of individuals with respect to industrialization'])} in two countries, each chosen from a different region",
         f"the significance of {choice(['developments in transportation with respect to industrialization', 'developments in energy and power with respect industrialization', 'industrial infrastructure such as iron and steel', 'mass production', 'developments in communications'])} in two countries, each chosen from a different region", f"the social and political impact of {choice(['urbanization and the growth of cities and factories', 'labour conditions', 'labour conditions with reference to organization of labour', 'opposition to industrialization', 'with respect to the impacts on standards of living'])} in two different countries, each chosen from a different region"],
        [f"{choice(['role and relative importance of nationalism and political ideology regarding the', 'role and relative importance of religion, race, social and economic factors regarding the'])} origins and rise of two independence movements, up to the point of independence in two different regions", "wars as a cause and/or catalyst for two independence movements in two different regions", "internal and external factors vis-à-vis fostering growth of independence movements in two independent states, each chosen from a different region", "the methods of achieving independence (including violent and non-violent methods) in two independent states, each chosen from a different region",
         "the role and importance of leaders of independence movements in two independent states, each chosen from a differernt region", "the role and relative importance of other factors in the success of two independence movements, each in a different region", f"the {choice(['challenges from political movements', 'challenges from ethnic movements', 'challenges from racial movements', 'separatist movements', 'social challenges', 'cultural challenges', 'economic challenges', 'responses to challenges faced'])} during the first ten years of independence in two independent states, each chosen from a different region"],
        ["the conditions that encouraged the demand for democratic reform in two democratic states, each chosen from a differernt region", f"the conditions that encouraged the demand for democratic reform in two democratic states, each chosen from a differernt region, include referernce to {choice(['the aftermath of war and/or political upheaval as a condition', 'social and economic conditions', 'external influences as a condition'])}", f"{choice(['the role and significance of leaders', 'the development of political parties', 'constitutions and electoral systems'])} as a factor in the emergence of two democratic states, each chosen from a different region", f"the factors influencing the evolution of democratic states with referernce to {choice(['immigration', 'ideology', 'economic forces', 'foreign influences'])} in two democratic states, each chosen from a differerent region",
         "the responses to, and impact of, domestic crises in two democratic states, each chosen from a differernt region", "suffrage movements and civil protests with referernce to the developement of two democratic states, each chosen from a differernt region", f"the impact of democracy on {choice(['education','social welfare', 'policies towards women and minorities', 'the distribution of wealth'])} in two democratic states, each chosen from a different region", "the extent to which citizens benefit from policies in two democratic states, each chosen from a differernt region", "the impact of democracy on freedom of expression in the arts and media in two democratic states, each chosen from a differernt region"],
        [f"{choice(['economic factors', 'social division', 'the impact of war', 'the weakness of political systems'])} as a condition in which two authoritarian states emerged, each from a differernt region", f"the methods used to establish two authoritarian states, each from a differernt region {choice(['','include reference to persuasion and coercion', 'include reference to the role of leaders', 'include reference to ideology', 'include reference to the use of force', 'include reference to the use of propoganda'])}", f"{choice(['the use of legal methods', 'the use of force', 'charismatic leadership', 'the dissemination of propaganda', 'nature, extent and treatment of opposition'])} in regard to the maintaining of power in two authoritarian states, each from a differernt region",
         "the impact of the success and/or failure of foreign policy in two authoritarian states each chosen from a different region", f"the {choice(['aims','impact'])} of domestic {choice(['economic', 'political', 'cultural', 'social'])} policies in two authoritarian states each chosen from a different region", "the impact of policies on women and minorities in two authoritarian states each chosen from a different region", "the extent in which authoritarian control was achived in two authoritarian states each chosen from a different region"],
        [f"{choice(['economic','ideological', 'political', 'territorial',])} causes alongside other causes for two {choice(['civil ',''])}wars in two different regions", f"{choice(['short-term', 'long-term'])} causes of two {choice(['civil ', ''])}wars in two differernt regions", f"the impact of {choice(['technological developments', 'the extent of the mobilization of human and economic resources', 'the influence and/or involvement of foreign powers'])} on the outcome of two {choice(['civil ', ''])}wars in two differernt regions",
         f"{choice(['the successes and failures of peacemaking', 'territorial changes', 'political repercussions', 'economic, social and demographic impacts', 'economic, social and demographic impacts with referernce to the changes in the role and status of women'])} in two {choice(['civil ', ''])}wars in two differernt regions"],
        [f"the role of {choice(['ideology', 'fear and aggression', 'economic interests'])} the breakdown of the grand alliance and the emergence of superpower rivalry in Europe and Asia (1943-1949)", f"{choice(['containment', 'the idea of peaceful co-existence', 'Sino-Soviet and Sino-US relations', 'detente'])} in superpower relations (1947-1979)",
         f"reasons for the end of the Cold War (1980-1991), include referernce to {choice(['ideological challenges and dissent', 'economic problems', 'the arms race'])}", "the impact of two leaders, each chosen from a different region, on the course and development of the Cold War", "the impact of Cold War tensions on two countries (excluding the USSR and the US)", "the impact and significance of two Cold War crises from two differernt regions"]
    ]
    


    term = choice(command_terms)
    text = choice(section_terms[topic-1])
    return (f'[blue]{term.lstrip()}[/blue] [green]{text.lstrip()}.[/green]')


def genPaper2() -> str:
    """This function generates and prints a question for Paper 2"""

    # 1) Loop Though all Topics (Paper 2 has 12 topics)
    # 2) Print the topic type
    # 3) Print two questions from the topic

    clear()

    output = ""
    output += ("[bold]Paper 2[/bold]\n")

    for topic in range(1, 13):
        output += (f"Topic {topic}: {world_history_section_names[topic-1]}\n")
        for question in range(2):
            output += (f"{(topic-1)*2 + question+1}. {genWorldHistoryQuestion(topic)}\n")
        output += ("\n")

    print(output)

    return output


def genPaper3() -> str:
    """This function generates and prints a question for Paper 3"""

    # 1) Loop Though all Topics (Paper 3 has 18 topics)
    # 2) Print the topic type
    # 3) Print two questions from the topic
    clear()

    output = "\n"
    output += ("[bold]Paper 3[/bold]\n")

    for topic in range(1, 19):
        output += (f"Topic: {europe_paper3_section_names[topic-1]}\n")
        for question in range(2):
            output += (f"{(topic-1)*2 + question+1}. {genEurope_Paper3(topic)}\n")
        output += ("\n")

    print(output)

    return output


def clear():
    """This helper function clears the terminal"""
    system('clear')


europe_paper3_section_names = [
    "1: Monarchies in England and France (1066-1223)",
    "2: Muslims and Jews in medieval Europe (1095-1492)",
    "3: Late medieval political crises (1300-1487)",
    "4: The Renaissance (c1400-1600)",
    "5: The Age of Exploration and its impact (1400-1550)",
    "6: The Reformation (1517-1572)",
    "7: Absolutism and Enlightenment (1650-1800)",
    "8: The French Revolution and Napoleon I (1774-1815)",
    "9: France (1815-1914)",
    "10: Society, politics and economy in Britain and Ireland (1815-1914)",
    "11: Italy (1815-1871) and Germany (1815-1890)",
    "12: Imperial Russia, revolution and the establishment of the Soviet Union (1855-1924)",
    "13: Europe and the First World War (1871-1918)",
    "14: European states in the inter-war years (1918-1939)",
    "15: Versailles to Berlin: Diplomacy in Europe (1919-1945)",
    "16: The Soviet Union and post-Soviet Russia (1924-2000)",
    "17: Post-war western and northern Europe (1945-2000)",
    "18: Post-war central and eastern Europe (1945-2000)"
]
"""These are the section names for the Paper 3 Exam in the Europe region."""


world_history_section_names = [
    "World history topic 1: Society and economy (750-1400)",
    "World history topic 2: Causes and effects of medieval wars (750-1500)",
    "World history topic 3: Dynasties and rulers (750-1500)",
    "World history topic 4: Societies in transition (1400-1700)",
    "World history topic 5: Early Modern states (1450-1789)",
    "World history topic 6: Causes and effects of Early Modern wars (1500-1750)",
    "World history topic 7: Origins, development and impact of industrialization (1750-2005)",
    "World history topic 8: Independence movements (1800-2000)",
    "World history topic 9: Evolution and development of democratic states (1848-2000)",
    "World history topic 10: Authoritarian states (20th century)",
    "World history topic 11: Causes and effects of 20th century wars",
    "World history topic 12: The Cold War: Superpower tensions and rivalries (20th century)",
]
"""These are the section names for the paper 2 exam"""

# Settings:
numberOfQuestions = 2
"""This is the number of questions per topic."""


while True:

    user_input = input("\nPress enter to continue.\nOr write 2 to Generate Some Paper 2 Questions For A Given Unit.\nOr write 3 Generate Some Paper 3 Questions For A Given Unit.\nOr write 4 to change the number of questions per topic.\nOr write genPaper2 to generate a paper 2.\nOr write genPaper3 to generate a paper 3.\nOr write x to exit.\nChoice: ")
    """This is the user input. It is used to determine what the user wants to do."""

    clear()

    if user_input == "2":
        try:
            topic = int(input("Create a question for which topic? (1-12): "))
        except:
            print("Invalid topic number, please try again.")
            input("Press enter to continue...")
            continue
        if topic < 1 or topic > 12:
            print("Invalid topic number, please try again.")
            input("Press enter to continue...")
            continue

        clear()
        print(f"\n[bold]Topic: {world_history_section_names[topic-1]}[/bold]\n\n")

        for i in range(numberOfQuestions):
            print(f"{i+1}. {genWorldHistoryQuestion(topic)}")
    elif user_input == "3":
        try:
            topic = int(input("Create a question for which topic? (1-18): "))
        except:
            print("Invalid topic number, please try again.")
            input("Press enter to continue...")
            continue
        if topic < 1 or topic > 18:
            print("Invalid topic number, please try again.")
            input("Press enter to continue...")
            continue
        clear()
        print(
            f"[bold]Topic: {europe_paper3_section_names[topic-1]}[/bold]\n\n")

        for i in range(numberOfQuestions):
            print(f"{i+1}. {genEurope_Paper3(topic)}")
    elif user_input == "4":
        try:
            numberOfQuestions = int(
                input("How many questions per topic? (1-10): "))
        except:
            print("Invalid number of questions, please try again.")
            input("Press enter to continue...")
            continue
        if numberOfQuestions < 1 or numberOfQuestions > 10:
            print("Invalid number of questions, please try again.")
            input("Press enter to continue...")
            continue
    elif user_input == "genPaper2":
        genPaper2()
    elif user_input == "genPaper3":
        genPaper3()
    elif user_input == "genPaper2PDF":
        genPaper2(True)
    elif user_input == "genPaper3PDF":
        genPaper3(True)
    elif user_input == "x":
        break
    else:
        print("Invalid input, please try again.")
        input("Press enter to continue...")
        continue

    print("[bold]Note:[/bold] [underline]not all questions are perfect[/underline] due to the random nature of the program, [underline]if you don't like the question, skip it[/underline].")


quit()
