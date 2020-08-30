

import time,os,re,csv,sys,uuid
from datetime import date


def update_predict_log(country,y_pred,y_proba,query,runtime, MODEL_VERSION, test=False):
    """
    update predict log file
    """

    ## name the logfile using something that cycles with date (day, month, year)
    today = date.today()
    logfile = "predict-{}-{}.log".format(today.year, today.month)

    ## write the data to a csv file
    header = ['unique_id','timestamp','y_pred','y_proba','x_shape','model_version','runtime']
    write_header = False
    if not os.path.exists(logfile):
        write_header = True
    with open(logfile,'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')
        if write_header:
            writer.writerow(header)

        to_write = map(str,[uuid.uuid4(),time.time(),y_pred,y_proba,query,MODEL_VERSION,runtime])
        writer.writerow(to_write)

def update_train_log(tag,dates,metrics,runtime,MODEL_VERSION,MODEL_VERSION_NOTE,test=False):
    """
    update train log file
    """

    ## name the logfile using something that cycles with date (day, month, year)
    today = date.today()
    logfile = "train-{}-{}.log".format(today.year, today.month)

    ## write the data to a csv file
    header = ['unique_id','timestamp','tag','dates','metrics','model_version',"model_version_note",'runtime']
    write_header = False
    if not os.path.exists(logfile):
        write_header = True
    with open(logfile,'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')
        if write_header:
            writer.writerow(header)

        to_write = map(str,[uuid.uuid4(),time.time(),tag,dates,metrics,MODEL_VERSION,MODEL_VERSION_NOTE,runtime])
        writer.writerow(to_write)
