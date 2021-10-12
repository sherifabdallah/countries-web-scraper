import os
import requests
from bs4 import BeautifulSoup
from csv import writer
from csv import reader
import ast
import fiona


with open("url_text/cape town_south africia.txt") as file:
    lines = [line.strip() for line in file]

for x in lines:
    try:
        path = 'main.csv'
        isFile = os.path.isfile(path)
        if isFile == False:
            os.startfile('csv_maker.py')  # Start csv maker
        elif os.stat('main.csv').st_size == 0:
            os.startfile('csv_maker.py')  # Start csv maker


        result = requests.get(x)
        # result = requests.get('https://sdinet.org/settlement/1847/1025754')

        # result = requests.get('')
        src = result.content
        # print(src)
        # print(type(src))
        # print(result)

        country_name = []
        city_name = []
        settlement_name = []
        established = []
        lastupdated = []


        soup = BeautifulSoup(src, "lxml")


        country_names = soup.find_all( "h4", { "class" : "black-bar-heading" } )
        city_names = soup.find_all( "h4", { "class" : "black-bar-heading" } )
        settlement_names = soup.find_all( "h2", { "class" : "section-heading" } )
        established2 = soup.find_all( "h3", { "class" : "section-sub-heading" } )
        lastupdated2 = soup.find_all( "h3", { "class" : "section-sub-heading" } )
        estimated_population = soup.find_all( "div", id="population")
        # estimated_number_of_structures = str(soup.find_all( "div", id="structures"))
        try:
            javascrpit = str(soup)
            gps1 = javascrpit.find('shape') + 9
            gps2 = javascrpit.find('function getObjectProperty') - 16
            javascrpit =  javascrpit[gps1:gps2].replace('shape = ', '')
            javascrpit = javascrpit.replace(';', '')
            javascrpit = javascrpit.replace('[', '(')
            javascrpit = javascrpit.replace(']', ')')
            javascrpit = javascrpit.replace('"', '')
            javascrpit = '[' + javascrpit + ']'
            javascrpit = ast.literal_eval(javascrpit)
            javascrpit = [(element[1],element[0]) for element in javascrpit]
        except:
            javascrpit = str(javascrpit)
            javascrpit = 'NA'
        # Variabels
        for i in range(len(country_names)):
            country_name.append(country_names[i].text)
            city_name.append(city_names[i].text)
            settlement_name.append(settlement_names[i].text)
            lastupdated.append(lastupdated2[i].text)
            established.append(established2[i].text)


        # If javascript == Na




        # Country Name
        country_name = country_name[0]
        country_name = country_name[9:]
        # print(country_name)
        # City Name
        city_name = city_name[1]
        city_name = city_name[6:]
        # print(city_name)
        # settlement_name
        settlement_name = settlement_name[0]
        settlement_name = settlement_name[12:]
        # print(settlement_name)
        # established
        established = established[0]
        established = established[13:]
        # print(established)
        # lastupdated
        lastupdated = lastupdated[1]
        lastupdated = lastupdated[14:]
        lastupdated = lastupdated.replace(".", "-")
        # print(lastupdated)
        # estimated population
        estimated_population = str(estimated_population)
        estimated_population = estimated_population[38:]
        estimated_population = estimated_population.replace("</div>]", "")
        # print(estimated_population)
        # Estimated number of structures
        # print(estimated_number_of_structures)
        # coardanits





        # CSV





        def append_list_as_row(file_name, list_of_elem):
            # Open file in append mode
            with open(file_name, 'a+', newline='') as write_obj:
                # wr = writer(file_name)
                # wr.writerow(["Country", "City", "Settlement", "Established", " Last Updated", "Estimated population","Estimated number of structures", "Coordinates "])

                # Create a writer object from csv module
                csv_writer = writer(write_obj)
                # Add contents of list as last row in the csv file
                csv_writer.writerow(list_of_elem)
        def main():
            # List of strings
            row_contents = [country_name, city_name, settlement_name, established, lastupdated, estimated_population ,javascrpit]

            # Append a list as new line to an old csv file
            append_list_as_row('main.csv', row_contents)
        if __name__ == '__main__':
            main()









        # fileName = settlement_name + '.shp'
        # os.write(fileName)







        if javascrpit != 'NA':
            # define schema
            schema = {
                'geometry':'Polygon',
                'properties':[('Country', 'str'),('City', 'str'), ('Settlement','str'), ('Established', 'str'), ('Last Updated', 'str'), ('Estimated population', 'str')]
            }
            # Make a shp file
            # shape_filwname =
            # make_cpg_file = open(, 'w+')
            #open a fiona object


            # Make a diractory
            shape_dirctory_path = 'shapefile\\' + country_name + '_' + city_name + '_' + settlement_name
            shape_dirctory_path = shape_dirctory_path.lower()
            shape_dirctory_path = shape_dirctory_path.replace(' ', '-')

            isdir = os.path.isdir(shape_dirctory_path)

            if isdir == False:
                os.mkdir(shape_dirctory_path)
            else:
                print()

            # Make a cgp file
            shp_filename =  shape_dirctory_path + '\\' + settlement_name + '.shp'
            shp_filename = shp_filename.lower()
            shp_filename = shp_filename.replace(' ', '-')







            polyShp = fiona.open(shp_filename , mode='w', driver='ESRI Shapefile', schema = schema, crs = "EPSG:4326")
            #get list of points
            xyList = []
            rowName = settlement_name


            xyList = javascrpit


            #save record and close shapefile
            rowDict = {
            'geometry' : {'type':'Polygon',
                             'coordinates': [xyList]}, #Here the xyList is in brackets


            'properties': { 'Country' : country_name,
                            'City' : city_name,
                            'Settlement' : settlement_name,
                            'Established' : established,
                            'Last Updated' : lastupdated,
                            'Estimated population' : estimated_population
                            },
            }
            #country_name, city_name, settlement_name, established, lastupdated, estimated_population, '',javascrpit]
            print(rowDict)
            # print(type(xyList))


            polyShp.write(rowDict)
            # close fiona object
            polyShp.close()
        else:
            print('No Coardanits')
    except:
        print('Please Try Again')




