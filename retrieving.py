from main import datas,Session,engine
from sqlalchemy import desc

local_session=Session(bind=engine)

# datas=local_session.query(datas).all()

# for i in datas:
# 	print(i.added_on)


group=local_session.query(datas).filter(datas.group==3).first()

# acending order
group=local_session.query(datas).order_by(datas.group).all()
# decding_order
group=local_session.query(datas).order_by(dec(datas.group)).all()

print(group)