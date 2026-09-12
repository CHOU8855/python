class India():
    def capital(self):
        print('New Dehli is the capital of india')


    def language(self):
        print('Hindi is the most prominent language in india')

    def type(self):
        print('india is a nee which means newling emerging economy as theyre gdp per capita is in the rnages between 12,485 and 25,783 cite by the un national page in 2022')


class USA():
    def capital(self):
        print('washington dc is the capital of united states of america')

    def language(self):
        print('The priamry language spoken in the usa is american english however the un have denie this is actual language and is just pronouced differently from standard british english.')

    def type(self):
        print('The usa is a hic standing for a high income country as its gdp per capita is of the around 25k threshold')

class UK():
    def capital(self):
        print('The capital of the Uk is London')

    def language(self):
        print('The priamry language spoken in the Uk is English.')

    def type(self):
        print('The uk is a hic standing for a high income country as its gdp per capita is of the around 25k threshold')

obj_ind = India()
obj_usa = USA()
obj_uk = UK()

for country in (obj_ind, obj_usa, obj_uk):
    country.capital()
    country.language()
    country.type()



    