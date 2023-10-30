
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        for row in self.data:
            week = row[1:]
            cleaned_week = [float(price) for price in week if price.strip()]
            # list comprehension that converts each 'price' in 'week' to a float 
            # and only includes a 'price' element in 'cleaned_week'
            # if 'price.strip()' is NOT an empty string
            averages.append(round(stats.mean(cleaned_week), 3))
        return averages

    def median02(self):
        """pt2
        """
        median = []
        for row in self.data:
            week = row[1:]
            cleaned_week = [float(price) for price in week if price.strip()]
            median.append(stats.median(cleaned_week))
        return median
    
    def stddev03(self):
        """pt3
        """
        stddev = []
        for row in self.data:
            week = row[1:]
            cleaned_week = [float(price) for price in week if price.strip()]
            stddev.append(round(stats.stdev(cleaned_week), 3))
        return stddev