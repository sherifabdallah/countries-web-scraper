import requests
from bs4 import BeautifulSoup
import csv
import ast
# import fiona
import re


# To Get urls file write in terminal
# wget --output-file=malawi.txt --recursive --spider --include-directories="/settlement/,/explore-our-data/country/" http://sdinet.org/explore-our-data/country/?country=malawi


txt_filename = str(input('Enter file Name : '))
csv_filename = str(input('Enter csv Name : '))
with open("urls/" + txt_filename +".txt") as file:
    lines = [line.strip() for line in file]

for link in lines:
    url = link
    result = requests.get(link)
    src = result.content
    # Soup
    soup = BeautifulSoup(src, "lxml")
    # ===========================================================================
    # Country Name
    # ===========================================================================
    country_name = []
    country_names = soup.find_all( "h4", { "class" : "black-bar-heading" } )
    # ===========================================================================
    # City Names
    # ===========================================================================
    city_name = []
    city_names = soup.find_all( "h4", { "class" : "black-bar-heading" } )
    # ===========================================================================
    # Settlement Name
    # ===========================================================================
    settlement_name= []
    settlement_names = soup.find_all( "h2", { "class" : "section-heading" } )
    # ===========================================================================
    # Established Name
    # ===========================================================================
    established = []
    established2 = soup.find_all( "h3", { "class" : "section-sub-heading" } )
    # ===========================================================================
    # Lastupdated Name
    # ===========================================================================
    lastupdated = []
    lastupdated2 = soup.find_all( "h3", { "class" : "section-sub-heading" } )
    # ===========================================================================
    # Population Name
    # ===========================================================================
    population = soup.find_all( "div", id="population")
    # ===========================================================================
    # Structures Name
    # ===========================================================================
    try:
        structures = str(soup)
        structures_frist_bracket = structures.find('C5_Structures_Total":"')
        structures = structures[structures_frist_bracket:structures_frist_bracket + 100]
        structures = structures.replace('C5_Structures_Total":"', '')
        structures = structures[0: structures.index('","')]
    except:
        structures = 'N/A'
    # ===========================================================================
    # For Loop
    # ===========================================================================
    for i in range(len(country_names)):
        country_name.append(country_names[i].text)
        city_name.append(city_names[i].text)
        settlement_name.append(settlement_names[i].text)
        lastupdated.append(lastupdated2[i].text)
        established.append(established2[i].text)


    # ===========================================================================
    country_name = country_name[0]
    country_name = country_name[9:]
    # ===========================================================================
    city_name = city_name[1]
    city_name = city_name[6:]
    # ===========================================================================
    settlement_name = settlement_name[0]
    settlement_name = settlement_name[12:]
    # ===========================================================================
    established = established[0]
    established = established[13:]
    # ===========================================================================
    lastupdated = lastupdated[1]
    lastupdated = lastupdated[14:]
    lastupdated = lastupdated.replace(".", "-")
    # ===========================================================================
    population = str(population)
    population = population[38:]
    population = population.replace("</div>]", "")
    # ===========================================================================

    # ===========================================================================
    # Ciordanits
    # ===========================================================================
    try:
        javascrpit = str(soup)
        gps1 = javascrpit.find('shape') + 9
        gps2 = javascrpit.find('function getObjectProperty') - 16
        javascrpit = javascrpit[gps1:gps2].replace('shape = ', '')
        javascrpit = javascrpit.replace(';', '')
        javascrpit = javascrpit.replace('[', '(')
        javascrpit = javascrpit.replace(']', ')')
        javascrpit = javascrpit.replace('"', '')
        javascrpit = '[' + javascrpit + ']'
        javascrpit = ast.literal_eval(javascrpit)
        javascrpit = [(element[1], element[0]) for element in javascrpit]
        javascrpit_chek = ''
    except:
        javascrpit = str(javascrpit)
        javascrpit_chek='NA'
        javascrpit = ''
    # ===========================================================================




    # Status
    # ===========================================================================
    status = str(soup)
    status_frist = status.find('"section_B\/B14_Status":"')
    status = status[status_frist:status_frist + 100]
    status = status.replace('"section_B\/B14_Status":"', '')
    status = status.replace('_', ' ')
    status = ''.join([i for i in status if not i.isdigit()]).replace(' ', ', ')

    if len(status) == 0 or len(status) > 150:
        status = 'N/A'
    else:
        status = status[0: status.index('"')]

    # ===========================================================================


    # Eviction
    # ===========================================================================
    eviction = str(soup)
    eviction_frist = eviction.find('"section_E\/E2B_Current_Eviction_Seriousness":"')
    eviction = eviction[eviction_frist:eviction_frist+100]
    eviction = eviction.replace('"section_E\/E2B_Current_Eviction_Seriousness":"', '')
    try:
        eviction = eviction[0: eviction.index('","')]
    except:
        'NA'
    if len(eviction) > 10:
        eviction = 'None'
    elif len(eviction) == 0:
        eviction = 'None'
    # ===========================================================================

    # City relate
    # ===========================================================================
    city_relat = str(soup)
    city_relat_1 = city_relat.find('section_P\/P7_City_Relationship":"')
    city_relat = city_relat[city_relat_1: city_relat_1 + 100]
    city_relat = city_relat.replace('section_P\/P7_City_Relationship":"', '').replace('"', '')

    if len(city_relat) == 0 or len(city_relat) > 100:
        city_relat = 'N/A'
    else:
        city_relat = city_relat[0: city_relat.index(',')]

    # ===========================================================================


    # City relate
    # ===========================================================================
    electric = str(soup)
    electric_1 = electric.find('J1_Electricity_Available":"')
    electric = electric[electric_1: electric_1 + 100]
    electric = electric.replace('J1_Electricity_Available":"', '').replace('"', '')
    if len(electric) == 0 or len(electric) > 100:
        electric = 'N/A'
    else:
        electric = electric[0: electric.index(',')]
    # ===========================================================================


    # Working taps to people
    # ===========================================================================
    water_pp = str(soup)
    water_pp_1 = water_pp.find('<h4>Working taps to people:</h4>')
    water_pp = water_pp[water_pp_1:water_pp_1 + 100]
    water_pp = water_pp.replace('<h4>Working taps to people:</h4>', '').replace('<div class="bold-it">', '').replace('</div>', '').replace('<div class="indicator">', '').replace('<h4>A', '').replace('<', '').replace('h4', '').replace('>', '').strip()



    if len(water_pp) == 0 or len(water_pp) > 100:
        water_pp = 'N/A'
    else:
        water_pp = water_pp.strip()

    # ===========================================================================


    # Total number of toilets seats
    # ===========================================================================
    total_number_of_toilets_seats = str(soup)
    total_number_of_toilets_seats_frist = total_number_of_toilets_seats.find('Total number of toilets seats:</h4>')
    total_number_of_toilets_seats = total_number_of_toilets_seats[total_number_of_toilets_seats_frist:total_number_of_toilets_seats_frist + 100]
    total_number_of_toilets_seats = total_number_of_toilets_seats.replace('</div>', '').replace('<div class="bold-it">', '').replace('Total number of toilets seats:</h4>', '').replace('Status :declared_legal_protected', '').replace(' ', '').replace('<divclass="col-lg-4col-md-4col-sm-4indicator">', '').strip()


    if len(total_number_of_toilets_seats) == 0 or len(total_number_of_toilets_seats) > 100:
        total_number_of_toilets_seats = 'N/A'
    else:
        total_number_of_toilets_seats = total_number_of_toilets_seats[0: total_number_of_toilets_seats.index('<')]
        total_number_of_toilets_seats = total_number_of_toilets_seats.strip()
    # ===========================================================================



    # Working_toilet_seats_to_people
    # ===========================================================================
    Working_toilet_seats_to_people = str(soup)
    Working_toilet_seats_to_people_frist = Working_toilet_seats_to_people.find('<h4>Working toilet seats to people:</h4>')
    Working_toilet_seats_to_people = Working_toilet_seats_to_people[Working_toilet_seats_to_people_frist:Working_toilet_seats_to_people_frist + 200]
    Working_toilet_seats_to_people = Working_toilet_seats_to_people.replace('</div>', '').replace('<div class="bold-it">', '').replace('<h4>Working toilet seats to people:</h4>', '').replace('Status :declared_legal_protected', '').replace(' ', '').replace('<h4>Total number of toilets seats:</h4>', '').replace('<divclass="indicator">', '').strip()

    if len(Working_toilet_seats_to_people) == 0 or len(Working_toilet_seats_to_people) > 200:
        Working_toilet_seats_to_people = 'N/A'
    else:
        Working_toilet_seats_to_people = Working_toilet_seats_to_people[0: Working_toilet_seats_to_people.index('<')].strip()

    # ===========================================================================


    # Types of toilets in use
    # ===========================================================================
    types_of_toilets = soup.find('li', class_='active')
    types_of_toilets = str(types_of_toilets)
    types_of_toilets_1 = types_of_toilets.find('</noscript></span>')
    types_of_toilets = types_of_toilets[types_of_toilets_1:]
    types_of_toilets = types_of_toilets.replace('</noscript></span>', '').replace('</li>', '')
    if len(types_of_toilets) == 0 or len(types_of_toilets) > 100 or len(types_of_toilets) == 1:
        types_of_toilets = 'N/A'
    # ===========================================================================


    # Main means of transportation
    # ===========================================================================
    trans_type = []
    trans_types = soup.find_all( "li", { "class" : "col-lg-3 col-md-3 col-sm-6 col-xs-6 active" } )

    for i in range(len(trans_types)):
        trans_type.append(trans_types[i].text)

    trans_type = str(trans_type)
    trans_type = trans_type.replace('\\t', '').replace('\\n', '').replace('[', '').replace(']', '').replace(' ', '').replace("'", '').replace(',', ', ')

    if len(trans_type) == 0 or len(trans_type) > 100:
        trans_type = 'N/A'
    # ===========================================================================


    # Commercial Establishments & Facilities
    # ===========================================================================
    facilities = []
    facilitiess = soup.find_all( "li", { "class" : "col-lg-3 col-md-3 col-sm-3 col-xs-6 active" } )

    for i in range(len(facilitiess)):
        facilities.append(facilitiess[i].text)

    facilities = str(facilities)
    facilities = facilities.replace('\\t', '').replace('\\n', '').replace('[', '').replace(']', '').replace(' ', '').replace("'", '').replace(',', ', ')

    if len(facilities) == 0 or len(facilities) > 100:
        facilities = 'N/A'
    # ===========================================================================

    # history
    # ===========================================================================
    history = str(soup)
    history_frist = history.find('History:')
    history = history[history_frist:]
    history = history.replace('</div>', '').replace('</h4>', '').strip()
    history = history[: history.index('<')]
    history = history.strip()


    # ===========================================================================


    # Priorities
    # ===========================================================================
    try:
        priorities = []
        priorities_2 = soup.find('ul', attrs = {'class': 'numbered-list'})
        priorities_2 = priorities_2.find_all('li')

        for i in range(len(priorities_2)):
            priorities_2.append(priorities_2[i].text)

        priorities = str(priorities_2)
        priorities = priorities.replace('[', '').replace(']', '').replace('<li>', '').replace('</li>', '').replace('<span>', '').replace('</span>', '')
        priorities = re.sub('\d', '', priorities)
        priorities = priorities.replace(' ', '').replace("'", '').replace(',', ', ')
    except:
        priorities = str('N/A')
    # ===========================================================================


    # Average cost of access per month
    # ===========================================================================
    water_cost = str(soup)
    water_cost_1 = water_cost.find('F\/F11_Water_MonthlyCost":')
    water_cost = water_cost[water_cost_1:int(water_cost_1 + 35)]
    water_cost = water_cost.replace('F\/F11_Water_MonthlyCost":', '')
    water_cost = my_string=''.join((ch if ch in '0123456789' else '') for ch in water_cost)

    if len(water_cost) == 0 or len(water_cost) > 35:
        water_cost = 'N/A'

    # ===========================================================================

    # Number of savings groups
    # ===========================================================================
    saving_tot = str(soup)
    saving_tot_1 = saving_tot.find('P10_Savings_Groups_Count":')
    saving_tot = saving_tot[saving_tot_1:int(saving_tot_1 + 35)]
    saving_tot = saving_tot.replace('P10_Savings_Groups_Count":', '')
    # saving_tot = saving_tot[ 0 : saving_tot.index(',')]
    if len(saving_tot) == 0 or len(saving_tot) > 35:
        saving_tot = 'N/A'
    else:
        saving_tot = saving_tot[0: saving_tot.index(',')]
    # ===========================================================================

    # Number of working toilets seats
    # ===========================================================================
    toilet_wrk = str(soup)
    toilet_wrk_frist = toilet_wrk.find('{"Working toilets":')
    toilet_wrk = toilet_wrk[toilet_wrk_frist:toilet_wrk_frist + 100]
    toilet_wrk = toilet_wrk.replace('{"Working toilets":', '').replace('colors = {};', '').replace('};', '').replace('"', '').strip()
    if len(toilet_wrk) == 0:
        toilet_wrk = 'NA'
    else:
        toilet_wrk = toilet_wrk[0: toilet_wrk.index('colors')].strip()
    # ===========================================================================


    # Number of taps
    # ===========================================================================
    water_tot = soup.find('div', id ='sharedTaps').text

    try:
        water_wrk = str(soup)
        water_wrk_1 = water_wrk.find('{"Working taps":')
        water_wrk = water_wrk[water_wrk_1:water_wrk_1 + 100]
        water_wrk = water_wrk.replace('{"Working taps":', '').strip()
        if len(water_wrk) == 0 or len(water_wrk) > 100:
            water_wrk = 'N/A'
        else:
            water_wrk = water_wrk[0: water_wrk.index('"')]
        # water_wrk = 'N/A'
    except:
        water_wrk = 'N/A'
    # ===========================================================================


    # Community leadership
    # ===========================================================================
    lead = str(soup)
    lead_1 = lead.find('"section_P\/P1_CommunityLeadership":"')

    lead = lead[lead_1:]
    lead = lead.replace('"section_P\/P1_CommunityLeadership":"', '')
    if lead[0:3] == 'yes':
        lead = 'Yes'
    else:
        lead = 'N/A'
    # ===========================================================================



    # How often does the community meet?
    # ===========================================================================
    lead_freq = str(soup)
    lead_freq_1 = lead_freq.find('"section_P\/P4_CommunityMeetings_Frequency":"')

    lead_freq = lead_freq[lead_freq_1: lead_freq_1 + 100]
    lead_freq = lead_freq.replace('"section_P\/P4_CommunityMeetings_Frequency":"', '')


    if len(lead_freq) == 0 or len(lead_freq) > 100:
        lead_freq = 'N/A'
    else:
        lead_freq = lead_freq[0: lead_freq.index(',"')]
        lead_freq = lead_freq.replace('"', '')

    # ===========================================================================

    # How often does the community meet with the city?
    # ===========================================================================
    city_freq = str(soup)
    city_freq_1 = city_freq.find('P\/P5_CityMeetings_Frequency":"')

    city_freq = city_freq[city_freq_1: city_freq_1 + 100]
    city_freq = city_freq.replace('P\/P5_CityMeetings_Frequency":"', '')
    if len(city_freq) == 0 or len(city_freq) > 100:
        city_freq = 'N/A'
    else:
        city_freq = city_freq[0: city_freq.index('"')]
    # ===========================================================================


    # Diseases
    # ===========================================================================
    try:
        diseases = []
        diseases_2 = soup.find('ul', attrs = {'class': 'bullet-list'})
        diseases_2 = diseases_2.find_all('li')

        for i in range(len(diseases_2)):
            diseases.append(diseases_2[i].text)

        diseases = str(diseases)
        diseases = diseases.replace('[', '').replace(']', '').replace("'", '').replace('"', '')
    except:
        diseases = str('N/A')
    # ===========================================================================


    # acc_clin
    # ===========================================================================
    acc_clin = str(soup)
    acc_clin_1 = acc_clin.find('"section_I\/I1_HealthClinic":"')

    acc_clin = acc_clin[acc_clin_1: acc_clin_1 + 100]
    acc_clin = acc_clin.replace('"section_I\/I1_HealthClinic":"', '')

    if len(acc_clin) == 0 or len(acc_clin) > 100:
        acc_clin = 'N/A'
    else:
        acc_clin = acc_clin[0: acc_clin.index('","')]
    # ===========================================================================

    # Road types
    # ===========================================================================
    road_type = str(soup)
    road_type_1 = road_type.find('"section_L\/L5_Road_Type":"')

    road_type = road_type[road_type_1: road_type_1 + 100]
    road_type = road_type.replace('"section_L\/L5_Road_Type":"', '')

    if len(road_type) == 0 or len(road_type) > 100:
        road_type = 'N/A'
    else:
        road_type = road_type[0: road_type.index('","')].replace('_', ' ')
    # ===========================================================================

    # Road types
    # ===========================================================================
    time_clin = str(soup)
    time_clin_1 = time_clin.find('"section_I\/I1_HealthClinic_Distance_min":"')

    time_clin = time_clin[time_clin_1: time_clin_1 + 100]
    time_clin = time_clin.replace('"section_I\/I1_HealthClinic_Distance_min":"', '')
    if len(time_clin) == 0 or len(time_clin) > 100:
        time_clin = 'Unknown'
    else:
        time_clin = time_clin[0: time_clin.index('","')]
        time_clin = time_clin.replace('_', ' ')
    # ===========================================================================

    # Garbage collections per week
    # ===========================================================================
    trash_pw = str(soup)
    trash_pw_1 = trash_pw.find('"section_H\/H6_Garbage_WeeklyCollections":')

    trash_pw = trash_pw[trash_pw_1: trash_pw_1 + 100]
    trash_pw = trash_pw.replace('"section_H\/H6_Garbage_WeeklyCollections":', '')

    if len(trash_pw) == 0 or len(trash_pw) > 100:
        trash_pw = 'N/A'
    else:
        trash_pw = trash_pw[0: trash_pw.index(',')]
    # ===========================================================================

    # Access to AIDS clinics
    # ===========================================================================
    acc_aids = str(soup)
    acc_aids_1 = acc_aids.find('"section_I\/I2_AidsClinic":"')

    acc_aids = acc_aids[acc_aids_1: acc_aids_1 + 100]
    acc_aids = acc_aids.replace('"section_I\/I2_AidsClinic":"', '')
    if len(acc_aids) == 0 or len(acc_aids) > 100:
        acc_aids = 'N/A'
    else:
        acc_aids = acc_aids[0: acc_aids.index('","')]
    # ===========================================================================

    # Average walking time to nearest Aids clinic (minutes)
    # ===========================================================================
    time_aids = str(soup)
    time_aids_1 = time_aids.find('"section_I\/I2_AidsClinic_Distance_min":"')

    time_aids = time_aids[time_aids_1: time_aids_1 + 100]
    time_aids = time_aids.replace('"section_I\/I2_AidsClinic_Distance_min":"', '')
    if len(time_aids) == 0 or len(time_aids) > 100:
        time_aids = 'Unknown'
    else:
        time_aids = time_aids[0: time_aids.index('","')]
        time_aids = time_aids.replace('_', ' ')
    # ===========================================================================

    # Access to hospitals
    # ===========================================================================
    acc_hosp = str(soup)
    acc_hosp_1 = acc_hosp.find('section_I\/I3_Hospital":"')

    acc_hosp = acc_hosp[acc_hosp_1: acc_hosp_1 + 100]
    acc_hosp = acc_hosp.replace('section_I\/I3_Hospital":"', '')
    if len(acc_hosp) == 0 or len(acc_hosp) > 100:
        acc_hosp = 'N/A'
    else:
        acc_hosp = acc_hosp[0: acc_hosp.index('","')]
        acc_hosp = acc_hosp.replace('_', ' ')
    # ===========================================================================

    # Average walking time to nearest hospital (minutes)
    # ===========================================================================
    time_hosp = str(soup)
    time_hosp_1 = time_hosp.find('"section_I\/I3_Hospital_Distance_min":"')

    time_hosp = time_hosp[time_hosp_1: time_hosp_1 + 100]
    time_hosp = time_hosp.replace('"section_I\/I3_Hospital_Distance_min":"', '')

    if len(time_hosp) == 0 or len(time_hosp) > 100:
        time_hosp = 'Unknown'
    else:
        time_hosp = time_hosp[0: time_hosp.index('","')]
        time_hosp = time_hosp.replace('_', ' ')
    # ===========================================================================

    # Garbage location
    # ===========================================================================
    trash_loc = str(soup)
    trash_loc_1 = trash_loc.find('"section_H\/H1_Garbage_Location":"')

    trash_loc = trash_loc[trash_loc_1: trash_loc_1 + 100]
    trash_loc = trash_loc.replace('"section_H\/H1_Garbage_Location":"', '')

    if len(trash_loc) == 0 or len(trash_loc) > 100:
        trash_loc = 'N/A'
    else:
        trash_loc = trash_loc[0: trash_loc.index('","')].replace('_', ' ').capitalize()

    # ===========================================================================

    def append_list_as_row(file_name, list_of_elem):
        # Open file in append mode
        with open(file_name, 'a+', newline='') as write_obj:

            csv_writer = csv.writer(write_obj)

            csv_writer.writerow(list_of_elem)
    def main():

        row_contents = [link ,country_name, city_name, settlement_name, established, lastupdated, history, priorities, population, structures, eviction, status, total_number_of_toilets_seats, toilet_wrk, Working_toilet_seats_to_people, types_of_toilets,water_tot, water_wrk, water_pp, electric, water_cost, trash_pw, trash_loc, road_type, trans_type, saving_tot,lead, lead_freq, city_relat, city_freq, diseases, acc_clin, time_clin, acc_aids, time_aids, acc_hosp, time_hosp,facilities]


        append_list_as_row('csv/ ' + csv_filename + ' .csv', row_contents)
    if __name__ == '__main__':
        main()


    # output

    output = {'country':country_name ,'City':city_name, 'settlement': settlement_name, 'established': established, 'last_updat': lastupdated, 'history': history, 'priorities':priorities, 'population': population, 'structures': structures, 'eviction': eviction, 'status': status, 'toilet_tot': total_number_of_toilets_seats, 'toilet_wrk': toilet_wrk, 'toilet seats to people': Working_toilet_seats_to_people, 'types_of_toilets': types_of_toilets, 'water_tot': water_tot, 'water_wrk': water_wrk, 'water_pp': water_pp, 'electric': electric  ,'water_cost':water_cost, 'trash_pw':trash_pw , 'trash_loc':trash_loc , 'road_type':road_type ,'trans_type':trans_type, 'saving_tot':saving_tot, 'lead':lead, 'lead_freq':lead_freq, 'city_relat':city_relat, 'city_freq':city_freq, 'diseases':diseases, 'acc_clin':acc_clin, 'time_clin':time_clin, 'acc_aids':acc_aids, 'time_aids':time_aids, 'acc_hosp':acc_hosp, 'time_hosp':time_hosp, 'facilities':facilities}
    for key in output:
        print(key, '->', output[key])
    print('-------------------------------------------------------------------------------------------------')