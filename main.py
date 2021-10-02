from fastapi import FastAPI
import uvicorn
import datetime
import calendar
import string

app = FastAPI()

@app.get("/")
async def root():
    return {"Welcome, this API finds the the day of the week of any date in the format - DD MM YYYY"}

@app.get("/findday/{date}")
async def findday(date):
    '''Function that returns day of week of any date in the past 
    or the future'''
    
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    day = calendar.day_name[born]
    return {date:day}

  
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
