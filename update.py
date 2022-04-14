from main import Session,engine,datas

local_session=Session(bind=engine)

group_data=local_session.query(datas).filter(datas.group=='2').first()
group_data.group='4'
local_session.commit()