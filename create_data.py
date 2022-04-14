from main import datas,Session,engine

data_dict=[
		{
			'group':'2',
			'year':'2025',
			'inflation':'2025'
		},
		{
			'group':'3',
			'year':'2026',
			'inflation':'2052'
		}
]

local_session=Session(bind=engine)
# new_data=datas(group='2',year='2025',inflation='205')
# local_session.add(new_data)
# local_session.commit()

for i in data_dict:
	new_data=datas(group=i['group'],year=i['year'],inflation=i['inflation'])
	local_session.add(new_data)
	local_session.commit()
	# print(new_data)
