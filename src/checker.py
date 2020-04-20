import re
import requests


class Checker(object):

    def check_availability(self, level, sess, subject, cournum):
        raw_data = self.get_data(level, sess, subject, cournum)
        parsed_data = self.parsed_data(raw_data)
        return parsed_data

    def parsed_data(self, data):
        table_data = []
        headers = []
        for l in data.split('\n'):
            if '<TH>' in l:
                header = re.findall(r"<A.*>([\w\d ]*)</A>", l)
                if header:
                    headers.append(header[0])
            if '<TR>' in l:
                datum = {}
                values = re.findall(r"<TD.*?>(.*?)</TD>", l)
                for i, value in enumerate(values):
                    datum[headers[i]] = value
                table_data.append(datum)
        return table_data

    def get_data(self, level, sess, subject, cournum):
        url = "http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl"
        response = requests.post(url, data={
            'level': level,
            'sess': sess,
            'subject': subject,
            'cournum': cournum
        })
        return response.text






