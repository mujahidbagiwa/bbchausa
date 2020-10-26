FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


#copy requirements.txt file first to prevent invalidating cache of downloaded packages.
COPY requirements.txt /bbchausanews/


#change dir to app dir on container
WORKDIR /bbchausanews

#get required packages to run apps
RUN pip install -r requirements.txt

#copy app dir from computer to app dir on container
COPY .  ./bbchausanews


#always run uvicorn command on starting container
ENTRYPOINT [ "uvicorn" ]


CMD ["bbchausanews.main:app", "--host", "0.0.0.0", "--port", "8000"]