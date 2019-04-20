import requests
import json
from bs4 import BeautifulSoup
import telebot
# from datetime
import datetime
import winsound

# Пустая нода = 999
# Ссылка на стату
URL = 'https://www.marathonbet.ru/su/live/animation/statistic.htm?treeId='
# Ссылка на историю
HISTORY_URL = 'https://www.marathonbet.ru/su/react/eventStatistics/get?treeId='
LIVE_URL = 'https://www.marathonbet.ru/su/live/'
# tg token
token: str = '721830181:AAHSX-_tXmZpDnWfBPoR6IvMWy3O5jU6QMI'
bot = telebot.TeleBot(token)
# channelId = -1001417609698
channelId = 253013981
teamsInList = ['START']
teamsInStatistic = ['START']


# midnightStatistic = ''

def getInfoMatch(id, time):
    statLink = URL + id
    response = requests.get(statLink, auth=('user', 'passwd'))

    # sysdate = datetime.now()

    temp = response.content
    soup = BeautifulSoup(temp, features="html.parser")
    lst = soup.find_all('script')

    null = 0
    true = 1
    false = -1

    # History
    historyLink = HISTORY_URL + id

    try:
        response = requests.get(historyLink, auth=('user', 'passwd'))
        temp = response.content
        dic = str(temp)
        dic = eval(dic)

        homeHistoryGoals = []
        homeHistoryMissedGoals = []
        homeHistoryResults = []
        for i in range(1, (
        eval(dic.decode('utf-8')).get('membersStatistics').get('members')[0].get('matches').get('rows').__len__())):
            matchResult = (
                eval(dic.decode('utf-8')).get('membersStatistics').get('members')[0].get('matches').get('rows')[i].get(
                    'cells'))[4].get('matchResult')
            mainScore = (
                eval(dic.decode('utf-8')).get('membersStatistics').get('members')[0].get('matches').get('rows')[i].get(
                    'cells'))[4].get('mainScore')
            if matchResult == 'WIN':
                if int(mainScore[0:mainScore.index(':')]) > int(mainScore[mainScore.index(':') + 1:]):
                    goalCount = int(mainScore[0:mainScore.index(':')])
                    goalMissedCount = int(mainScore[mainScore.index(':') + 1:])
                else:
                    goalCount = int(mainScore[mainScore.index(':') + 1:])
                    goalMissedCount = int(mainScore[0:mainScore.index(':')])
            elif matchResult == 'LOSE':
                if int(mainScore[0:mainScore.index(':')]) < int(mainScore[mainScore.index(':') + 1:]):
                    goalCount = int(mainScore[0:mainScore.index(':')])
                    goalMissedCount = int(mainScore[mainScore.index(':') + 1:])
                else:
                    goalCount = int(mainScore[mainScore.index(':') + 1:])
                    goalMissedCount = int(mainScore[0:mainScore.index(':')])
            elif matchResult == 'DRAW':
                goalCount = int(mainScore[0:mainScore.index(':')])
                goalMissedCount = int(mainScore[0:mainScore.index(':')])

            homeHistoryGoals.append(goalCount)
            homeHistoryMissedGoals.append(goalMissedCount)
            homeHistoryResults.append(matchResult)

        awayHistoryGoals = []
        awayHistoryMissedGoals = []
        awayHistoryResults = []
        for i in range(1, (
        eval(dic.decode('utf-8')).get('membersStatistics').get('members')[1].get('matches').get('rows').__len__())):
            matchResult = (
                eval(dic.decode('utf-8')).get('membersStatistics').get('members')[1].get('matches').get('rows')[i].get(
                    'cells'))[4].get('matchResult')
            mainScore = (
                eval(dic.decode('utf-8')).get('membersStatistics').get('members')[1].get('matches').get('rows')[i].get(
                    'cells'))[4].get('mainScore')
            if matchResult == 'WIN':
                if int(mainScore[0:mainScore.index(':')]) > int(mainScore[mainScore.index(':') + 1:]):
                    goalCount = int(mainScore[0:mainScore.index(':')])
                    goalMissedCount = int(mainScore[mainScore.index(':') + 1:])
                else:
                    goalCount = int(mainScore[mainScore.index(':') + 1:])
                    goalMissedCount = int(mainScore[0:mainScore.index(':')])
            elif matchResult == 'LOSE':
                if int(mainScore[0:mainScore.index(':')]) < int(mainScore[mainScore.index(':') + 1:]):
                    goalCount = int(mainScore[0:mainScore.index(':')])
                    goalMissedCount = int(mainScore[mainScore.index(':') + 1:])
                else:
                    goalCount = int(mainScore[mainScore.index(':') + 1:])
                    goalMissedCount = int(mainScore[0:mainScore.index(':')])
            elif matchResult == 'DRAW':
                goalCount = int(mainScore[0:mainScore.index(':')])
                goalMissedCount = int(mainScore[mainScore.index(':') + 1:])

            awayHistoryGoals.append(goalCount)
            awayHistoryMissedGoals.append(goalMissedCount)
            awayHistoryResults.append(matchResult)

        '''
        Хед-ту-хед
        headToHeadGames = []
        headToHeadResults = []
        for i in range (1, eval(dic.decode('utf-8')).get('headToHeadMatches').get('rows').__len__()):
            mainScore = (eval(dic.decode('utf-8')).get('headToHeadMatches').get('rows')[i].get('cells'))[4].get('mainScore')
            homeT = (eval(dic.decode('utf-8')).get('headToHeadMatches').get('rows')[i].get('cells'))[1].get('value')
            awayT = (eval(dic.decode('utf-8')).get('headToHeadMatches').get('rows')[i].get('cells'))[3].get('value')
            headToHeadGames.append(homeT + ' - ' + awayT)
            headToHeadResults.append(mainScore)
        '''

        homePlaceInTable = (eval(dic.decode('utf-8')).get('overviewTable')).get('rows')[2].get('cells')[0].get('value')
        awayPlaceInTable = (eval(dic.decode('utf-8')).get('overviewTable')).get('rows')[4].get('cells')[0].get('value')

        homeMatchesPlayed = (eval(dic.decode('utf-8')).get('overviewTable')).get('rows')[2].get('cells')[2].get('value')
        awayMatchesPlayed = (eval(dic.decode('utf-8')).get('overviewTable')).get('rows')[4].get('cells')[2].get('value')

        homeGoalsAtOwnLeague = (eval(dic.decode('utf-8')).get('overviewTable')).get('rows')[2].get('cells')[6].get(
            'value')
        awayGoalsAtOwnLeague = (eval(dic.decode('utf-8')).get('overviewTable')).get('rows')[4].get('cells')[6].get(
            'value')

    except Exception as e:
        pass

    # score_time
    scoreTimeLink = LIVE_URL + id
    response = requests.get(scoreTimeLink, auth=('user', 'passwd'))
    temp = response.content
    soup = BeautifulSoup(temp, features="html.parser")

    eventTime = soup.find("div", class_="green bold nobr")
    eventScore = soup.find("div", class_="cl-left red")
    eventLeague = soup.find("h2", class_="category-label")
    eventLeague = eventLeague.find_all("span", class_="nowrap")
    eventLeagueV = ''
    for i in range(len(eventLeague)):
        eventLeagueV = eventLeagueV + ' ' + eventLeague[i].contents[0]

    # TODO
    # Тег 'cl-left red' меняется на 'cl-left grey' когда матч заканчивается и все идет по пизде. Добавить обработку
    # мб обернуть в try catch

    if eventScore is None or eventTime is None: return

    vMin = str(eventTime.contents[0])[3:5]
    if vMin[1] == ':':
        vMin = vMin[0]
    elif str(eventTime.contents[0])[3:6] == 'Пер':
        vMin = 450
    else:
        vMin = vMin[0:2]

    statistic = str(lst[2])[str(lst[2]).index('reactData') + 12: str(lst[2]).index(']]>>') - 5]
    statistic_json = json.loads(statistic)
    try:
        all_events = statistic_json['liveStatistic']

        # home variables
        homeTeam = all_events['homeTeam']
        homeTimeMinutes = int(vMin)

        strWithoutGap = str(eventScore.contents[0]).strip()
        homeGoals = int(strWithoutGap[:strWithoutGap.index(':')])

        if homeTimeMinutes == 0: return
        try:
            homeSubstitution = all_events['statistic']['items']['SUBSTITUTION']['t1']
        except Exception as e:
            homeSubstitution = 999
            pass
        try:
            homeFoul = all_events['statistic']['items']['FOUL']['t1']
        except Exception as e:
            homeFoul = 999
            pass
        try:
            homeCorner = all_events['statistic']['items']['CORNER']['t1']
        except Exception as e:
            homeCorner = 999
            pass
        try:
            homeGoalPenalty = all_events['statistic']['items']['GOAL_PENALTY']['t1']
        except Exception as e:
            homeGoalPenalty = 999
            pass
        try:
            homeOffside = all_events['statistic']['items']['OFFSIDE']['t1']
        except Exception as e:
            homeOffside = 999
            pass
        try:
            homeYellowCard = all_events['statistic']['items']['YELLOW_CARD']['t1']
        except Exception as e:
            homeYellowCard = 999
            pass
        try:
            homeRedCard = all_events['statistic']['items']['RED_CARD']['t1']
        except Exception as e:
            homeRedCard = 999
            pass
        try:
            homePossession = all_events['statistic']['items']['POSSESSION']['t1']
        except Exception as e:
            homePossession = 999
            pass
        try:
            homeDangerousAttack = all_events['statistic']['items']['DANGEROUS_ATTACK']['t1']
        except Exception as e:
            homeDangerousAttack = 999
            pass
        try:
            homeShotOnTarget = all_events['statistic']['items']['SHOT_ON_TARGET']['t1']
        except Exception as e:
            homeShotOnTarget = 999
            pass
        try:
            homeFreeKick = all_events['statistic']['items']['FREE_KICK']['t1']
        except Exception as e:
            homeFreeKick = 999
            pass
        try:
            homeAttack = all_events['statistic']['items']['ATTACK']['t1']
        except Exception as e:
            homeAttack = 999
            pass
        try:
            homeShot = all_events['statistic']['items']['SHOT']['t1']
        except Exception as e:
            homeShot = 999
            pass

        # away variables
        awayTeam = all_events['awayTeam']
        awayTimeMinutes = int(vMin)
        awayGoals = int(strWithoutGap[strWithoutGap.index(':') + 1:strWithoutGap.index(':') + 3].strip())

        try:
            awaySubstitution = all_events['statistic']['items']['SUBSTITUTION']['t2']
        except Exception as e:
            awaySubstitution = 999
            pass
        try:
            awayFoul = all_events['statistic']['items']['FOUL']['t2']
        except Exception as e:
            awayFoul = 999
            pass
        try:
            awayCorner = all_events['statistic']['items']['CORNER']['t2']
        except Exception as e:
            awayCorner = 999
            pass
        try:
            awayGoalPenalty = all_events['statistic']['items']['GOAL_PENALTY']['t2']
        except Exception as e:
            awayGoalPenalty = 999
            pass
        try:
            awayOffside = all_events['statistic']['items']['OFFSIDE']['t2']
        except Exception as e:
            awayOffside = 999
            pass
        try:
            awayYellowCard = all_events['statistic']['items']['YELLOW_CARD']['t2']
        except Exception as e:
            awayYellowCard = 999
            pass
        try:
            awayRedCard = all_events['statistic']['items']['RED_CARD']['t2']
        except Exception as e:
            awayRedCard = 999
            pass
        try:
            awayPossession = all_events['statistic']['items']['POSSESSION']['t2']
        except Exception as e:
            awayPossession = 999
            pass
        try:
            awayDangerousAttack = all_events['statistic']['items']['DANGEROUS_ATTACK']['t2']
        except Exception as e:
            awayDangerousAttack = 999
            pass
        try:
            awayShotOnTarget = all_events['statistic']['items']['SHOT_ON_TARGET']['t2']
        except Exception as e:
            awayShotOnTarget = 999
            pass
        try:
            awayFreeKick = all_events['statistic']['items']['FREE_KICK']['t2']
        except Exception as e:
            awayFreeKick = 999
            pass
        try:
            awayAttack = all_events['statistic']['items']['ATTACK']['t2']
        except Exception as e:
            awayAttack = 999
            pass
        try:
            awayShot = all_events['statistic']['items']['SHOT']['t2']
        except Exception as e:
            awayShot = 999
            pass

        '''
        Стратегию пишем тут. 

        eventLeagueV                Название лиги
        headToHeadGames             Массив хед-ту-хед игр
        headToHeadResults           Массив хед-ту-хед результатов
        goalsOnBreak                Сумма голов в первом тайме

        homeTeam                    Домашняя команда
        homeTimeMinutes             Время
        homeGoals                   Голы домашней команды
        homeSubstitution            Замены домашней команды
        homeFoul                    Фолы домашней команды
        homeCorner                  Угловые домашней команды
        homeGoalPenalty             Пенальти домашней команды
        homeOffside                 Офсайды домашней команды
        homeYellowCard              Желтые карточки домашней команды
        homeRedCard                 Красные карточки домашней команды
        homePossession              Владение мячем домашней команды в процентах
        homeDangerousAttack         Опасные атаки домашней команды
        homeShotOnTarget            Удары в створ домашней команды
        homeFreeKick                Штрафные удары домашней команды
        homeAttack                  Атаки домашней команды
        homeShot                    Удары в сторону ворот домашней команды
        homeHistoryGoals            Массив забитых голов в последних 5 матчах
        homeHistoryMissedGoals      Массив пропущенных голов в последних 5 матчах
        homeHistoryResults          Результаты поледних 5 матчей
        homePlaceInTable            Место в турнирной таблице домашней команды
        homeMatchesPlayed           Матчей сыграно в лиге
        homeGoalsAtOwnLeague        Забито мячей в лиге

        awayTeam
        awayTimeMinutes
        awayGoals
        awaySubstitution
        awayFoul
        awayCorner
        awayGoalPenalty
        awayOffside
        awayYellowCard
        awayRedCard
        awayPossession
        awayDangerousAttack
        awayShotOnTarget
        awayFreeKick
        awayAttack
        awayShot
        awayHistoryGoals
        awayHistoryMissedGoals
        awayHistoryResults
        awayPlaceInTable
        awayMatchesPlayed
        awayGoalsAtOwnLeague

        '''
        try:
            posBracket = str(eventScore.contents[0]).index('(')
        except Exception as e:
            posBracket = 0
            pass

        # Результат в лайве в первом тайме
        '''
        if homeTimeMinutes <= 45 and id in teamsInList and id not in teamsInStatistic:
            goalsOnBreak = str(eventScore.contents[0])[str(eventScore.contents[0]).index(':') - 1 : str(eventScore.contents[0]).index(':') + 2]
            goalsUnderBreak = int (goalsOnBreak[:goalsOnBreak.index(':')]) + int (goalsOnBreak[goalsOnBreak.index(':') + 1 : ])

            teamsInStatistic.append(id)

            if goalsUnderBreak > 0 :
                msg = eventLeagueV + '\n' +\
                homeTeam + ' - ' + awayTeam + '\n' + 'Гол на ' + str(homeTimeMinutes) + ' минуте\n' + '\u2705\u2705\u2705'
                print (msg + '\n')
                bot.send_message(channelId, msg)
                #midnightStatistic = midnightStatistic + ('\u2705\u2705\u2705' + homeTeam + ' - ' + awayTeam + '\n')
        '''

        if homeTimeMinutes == 450 and id in teamsInList and id not in teamsInStatistic and posBracket != 0:
            goalsOnBreak = str(eventScore.contents[0])[
                           str(eventScore.contents[0]).index('(') + 1: str(eventScore.contents[0]).index(')')]
            goalsOnBreak = int(goalsOnBreak[:goalsOnBreak.index(':')]) + int(goalsOnBreak[goalsOnBreak.index(':') + 1:])

            teamsInStatistic.append(id)

            if goalsOnBreak > 0:
                msg = eventLeagueV + '\n' + \
                      homeTeam + ' - ' + awayTeam + '\n' + 'Голов в первом тайме : ' + str(
                    goalsOnBreak) + '\n' + '\u2705\u2705\u2705'
                print(msg + '\n')
                # bot.send_message(channelId, msg)
                # midnightStatistic = midnightStatistic + ('\u2705\u2705\u2705' + homeTeam + ' - ' + awayTeam + '\n')
            elif goalsOnBreak == 0:
                msg = eventLeagueV + '\n' + \
                      homeTeam + ' - ' + awayTeam + '\n' + 'Голов в первом тайме : ' + str(
                    goalsOnBreak) + '\n' + '\u274c\u274c\u274c'
                print(msg + '\n')
                # bot.send_message(channelId, msg)
                # midnightStatistic = midnightStatistic + ('\u274c\u274c\u274c' + homeTeam + ' - ' + awayTeam + '\n')
            else:
                print('Error : goalsOnBreak')

        # Стратегия №1
        # ТБ 0.5 в первом тайме
        try:
            if homeTimeMinutes <= 27 and (homeGoals + awayGoals) == 0 and (homeShotOnTarget + awayShotOnTarget) >= 4 and \
                    (homeShot + awayShot) >= 4 and (homeCorner + awayCorner) >= 2 and (
                    homeFreeKick + awayFreeKick) >= 4 and \
                    homeShotOnTarget != 999 and awayShotOnTarget != 999 and homeShot != 999 and awayShot != 999:

                if id not in teamsInList:
                    if homeTimeMinutes == 450:
                        homeTimeMinutes = 'Пер.'
                    elif homeTimeMinutes == 0:
                        homeTimeMinutes = 'Матч еще не начался'
                    else:
                        homeTimeMinutes = str(homeTimeMinutes) + '-я минута'

                    msg = '=====================================================================\n' + eventLeagueV + '\n' + \
                          homeTeam + ' - ' + awayTeam + '\n' + \
                          homeTimeMinutes + '\n' + \
                          str(homeGoals) + ' : ' + str(awayGoals) + '\n' + \
                          'Прогноз : ТБ 0.5 В ПЕРВОМ ТАЙМЕ'
                    print(msg)
                    winsound.Beep(2200, 100)
                    winsound.Beep(2400, 100)
                    winsound.Beep(2200, 100)
                    winsound.Beep(2400, 100)
                    winsound.Beep(2200, 100)
                    winsound.Beep(2400, 100)
                    teamsInList.append(id)

                # bot.send_message(253013981, msg)
                # bot.send_message(channelId, msg)
        except Exception as e:
            pass

            # Стратегия №2
        # ИТМ 1.5 или 1
        '''
        try:
            if homeTimeMinutes <= 27 and (homeGoals + awayGoals) == 0 and (homeShotOnTarget + awayShotOnTarget) >= 4 and \
            (homeShot + awayShot) >= 4 and (homeCorner + awayCorner) >= 2 and (homeFreeKick + awayFreeKick) >= 2 and\
             homeShotOnTarget != 999 and awayShotOnTarget != 999 and homeShot != 999 and awayShot != 999:


                if id not in teamsInList:
                    if homeTimeMinutes == 450:
                        homeTimeMinutes = 'Пер.'
                    elif homeTimeMinutes == 0:
                        homeTimeMinutes = 'Матч еще не начался'
                    else:
                        homeTimeMinutes = str(homeTimeMinutes) + '-я минута'


                    msg = eventLeagueV + '\n' +\
                    homeTeam + ' - ' + awayTeam + '\n' +\
                    homeTimeMinutes + '\n' +\
                    str(homeGoals) + ' : ' + str(awayGoals) + '\n' +\
                    'Прогноз : ТБ 0.5 В ПЕРВОМ ТАЙМЕ' 
                    print (msg)
                    teamsInList.append(id)

                #bot.send_message(253013981, msg)
                bot.send_message(channelId, msg)
        except Exception as e:
            pass
        '''

        return [time, homeTeam, awayTeam]

    except KeyError:
        # Нужна нормальная реализация
        pass


def getStatDataFootball():
    response = requests.get('https://www.marathonbet.ru/su/live/26418')
    soup = BeautifulSoup(response.content, features="html.parser")

    lst = soup.find_all('script')
    open_bracket_pos = str(lst[2]).index('liveMenuEvents')
    close_bracket_pos = str(lst[2]).rindex('animationWidgetUrl')
    data = "{" + str(lst[2])[open_bracket_pos - 1: close_bracket_pos - 2] + "}"

    json_data = json.loads(data)
    all_events = json_data['liveMenuEvents']
    sport = all_events['childs'][0]['label']

    if sport != 'Футбол':
        return

    football_events = all_events['childs'][0]
    events_count = str(football_events).count(''"event"'')

    event_pos = 0
    fstr = str(football_events)

    statData = []

    print(datetime.datetime.now())
    preMi = int(datetime.datetime.today().strftime("%M"))
    preSs = int(datetime.datetime.today().strftime("%S"))

    for i in range(events_count):
        event_pos = fstr.index('event', event_pos + 1)
        uid_pos = fstr.index('uid', event_pos - 30) + 7
        uid_end_pos = fstr.index(',', uid_pos) - 1
        uid = fstr[uid_pos:uid_end_pos]
        statData.append(getInfoMatch(str(uid), i))

    postMi = int(datetime.datetime.today().strftime("%M"))
    postSs = int(datetime.datetime.today().strftime("%S"))
    if postMi < preMi:
        postMi = postMi + 60
    if postSs < preSs:
        postSs = postSs + 60
    totalTimeInSec = (postMi - preMi) * 60 + (postSs - preSs)

    print('Время обработки: ' + str(round(totalTimeInSec / 60, 1)) + ' мин.')
    print('Матчей в лайве: ' + str(events_count))
    print(str(round(totalTimeInSec / events_count, 2)) + ' секунд на матч\n\n')

    return statData


if __name__ == "__main__":
    while True:
        footballStata = getStatDataFootball()
