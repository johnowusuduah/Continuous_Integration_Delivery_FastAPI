from fastapi import FastAPI
import uvicorn
import datetime
import calendar
import string

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome, this function finds the the day of the week of any date in the format - DD MM YYYY"}

@app.get("/finddayofweek/{date}")
async def finddayofweek(date):
    '''Function that returns day of week of any date in the past 
    or the future'''
    
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])

  
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
