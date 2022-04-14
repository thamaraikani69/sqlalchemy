from main import Session,engine,datas

local_session=Session(bind=engine)

group_data=local_session.query(datas).filter(datas.group=='4').first()
local_session.delete(group_data)
local_session.commit()