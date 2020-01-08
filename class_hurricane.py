class Hurricane:
    '''
    Fields: _title is a string containing the storm name
            _start is a string containing the date the storm formed in MMDD
            _end is a string containing the date the storm dissipated in MMDD
            _windspd is a non-negative integer containing the storm's maximum
                sustained winds for approximately 1 minute
            _mb is a non-negative integer containing the storm's lowest central
                pressure
            _cost is a non-negative integer containing the storm's damages
            _death is a non-negative integer containing the storm's casualties
    '''    
    def __init__(self, title, start, end, windspd, mb, cost, death):
        self._title = title
        self._start = start
        self._end = end
        self._windspd = int(windspd)
        self._pressure = int(mb)
        self._cost = int(cost)
        self._death = int(death)
        
    ## print(self) prints the storm name and it's classification
    ## Effects: prints information
    ## __str__: Hurricane -> Str
    def __str__(self):
        if self._windspd <= 38:
            cat_str = 'Tropical Depression '
            
        elif self._windspd >= 39 and self._windspd <= 73:
            cat_str = 'Tropical Storm '
         
        elif self._windspd >= 74 and self._windspd <= 95:
            cat_str = 'Category 1 Hurricane '
            
        elif self._windspd >= 96 and self._windspd <= 110:
            cat_str = 'Category 2 Hurricane '
            
        elif self._windspd >= 111 and self._windspd <= 129:
            cat_str = 'Category 3 Major Hurricane '
            
        elif self._windspd >= 130 and self._windspd <= 156:
            cat_str = 'Category 4 Major Hurricane '
            
        else:
            cat_str = 'Category 5 Major Hurricane '
            
        return cat_str + self._title.capitalize()
        
    ## self.date(when) translates either self._start or self._end to a string 
    ##   containing the date and returns said string
    ## Requires: when.capitalize() = 'Start' or 'End'
    ## date: Hurricane Str -> Str
    def date(self, when):
        if when.capitalize() == 'Start':
            date = self._start
            y = 'Formed'
            
        elif when.capitalize() == 'End':
            date = self._end
            y = 'Dissipated'
        
        if date[:2] == '01':
            month = 'January'
            
        elif date[:2] == '02':
            month = 'February'
            
        elif date[:2] == '03':
            month = 'March'
            
        elif date[:2] == '02':
            month = 'April'
            
        elif date[:2] == '05':
            month = 'May'
            
        elif date[:2] == '06':
            month = 'June'
            
        elif date[:2] == '07':
            month = 'July'
            
        elif date[:2] == '08':
            month = 'August'
            
        elif date[:2] == '09':
            month = 'September'
            
        elif date[:2] == '10':
            month = 'October'
            
        elif date[:2] == '11':
            month = 'November'
            
        elif date[:2] == '12':
            month = 'December'
            
        x = '{0} on {1} {2}'.format(y, month, date[2:])
        return x
        
    ## self.max_wind_speed() returns a sentence stating the maximum
    ##   wind speed of a storm
    ## max_wind_speed: Hurricane -> Str
    def max_wind_speed(self):
        x = 'Maximum wind speed was {0} mph.'.format(self._windspd)
        return x
        
    ## self.category() returns a sentence stating the storm's category
    ## category: Hurricane -> Str
    def category(self):
        if self._windspd <= 38:
            return 'Tropical Depression'
            
        elif self._windspd >= 39 and self._windspd <= 73:
            return 'Tropical Storm'
         
        elif self._windspd >= 74 and self._windspd <= 95:
            return 'Category 1'
            
        elif self._windspd >= 96 and self._windspd <= 110:
            return 'Category 2'
            
        elif self._windspd >= 111 and self._windspd <= 129:
            return 'Category 3'
            
        elif self._windspd >= 130 and self._windspd <= 156:
            return 'Category 4'
            
        else:
            return 'Category 5'
            
    ## self.pressure() returns a sentence stating
    ##   the lowest central pressure of a storm
    ## pressure: Hurricane -> Str
    def pressure(self):
        x = 'Minimum pressure was {0} mb (millibar).'.format(self._pressure)
        return x
        
    ## self.cost() returns a sentence stating the storm's damages
    ## cost: Hurricane -> Str    
    def cost(self):
        money_figure = ''
        x = str(self._cost)
        for y in range (1, len(x) + 1):
            money_figure = x[-y] + money_figure
            if y%3 == 0 and len(x) - y != 0:
                money_figure = ',' + money_figure
                
            elif len(x) - y == 0:
                money_figure = '$' + money_figure
                
        if self._windspd <= 38:
            cat_str = 'Tropical Depression {0}'.format(self._title.capitalize())
            
        elif self._windspd >= 39 and self._windspd <= 73:
            cat_str = 'Tropical Storm {0}'.format(self._title.capitalize())
            
        elif self._windspd >= 74:
            cat_str = 'Hurricane {0}'.format(self._title.capitalize())
            
        z = '{0} caused {1} in damages.'.format(cat_str, money_figure)
        return z
        
    ## self.deaths() returns a sentence stating the storm's casualties
    ## deaths: Hurricane -> Str    
    def deaths(self):
        cat_str = ''
        
        if self._windspd <= 38:
            cat_str = 'Tropical Depression {0}'.format(self._title.capitalize())
            
        elif self._windspd >= 39 and self._windspd <= 73:
            cat_str = 'Tropical Storm {0}'.format(self._title.capitalize())
         
        elif self._windspd >= 74:
            cat_str = 'Hurricane {0}'.format(self._title.capitalize())
            
        if self._death == 0:
            x = cat_str + ' caused no deaths.'
            
        elif self._death == 1:
            x = cat_str + ' caused 1 death.'
            
        else:
            x = cat_str + ' caused {0} deaths.'.format(self._death)
            
        return x