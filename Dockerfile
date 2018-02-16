#EXAM #1 - initial docker container run and modification


FROM ubuntu
MAINTAINER Joe
ADD getweather.py ~/getweather.py
WORKDIR ~/
CMD python ~/getweather.py

# Notes:  Build me like:
#     docker build -t "weather_joe:initial" .
