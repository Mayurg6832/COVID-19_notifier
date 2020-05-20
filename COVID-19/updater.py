from covid import Covid
import os
from plyer import notification

covid=Covid()
base=os.getcwd()
print(base)
path=os.path.join(base,'virus.ico')


def noti(data1):
	notification.notify('COVID-19',message=data1,app_icon=path)


India=covid.get_status_by_country_name('India')
data={
	key: India[key]
	for key in India.keys() and {'confirmed',
								 'active',
								 'deaths',
								 'recovered'}
}

data1=("Confirmed Cases: {}\nDeaths: {}\nActive: {}\nRecovered: {}".format(data['confirmed'],data['deaths'],data['active'],data['recovered']))
noti(data1)