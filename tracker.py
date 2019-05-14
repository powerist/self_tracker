# TODO: only the life_cumu_efforts needs to be materialized.
import sys
import datetime
import pickle

start_year = 2019
start_day = 100

lstatus_file = "./dataset/life_status.pickle"
lceffort_file = "./dataset/life_efforts.pickle"


def save_data(life_status, life_cumu_efforts):
    with open(lstatus_file, "wb") as sfile:
        pickle.dump(life_status, sfile)

    with open(lceffort_file, "wb") as cfile:
        pickle.dump(life_cumu_efforts, cfile)

        
def load_data():
    with open(lstatus_file, "rb") as sfile:
        life_status = pickle.load(sfile)

    with open(lceffort_file, "rb") as cfile:
        life_cumu_efforts = pickle.load(cfile)

    return life_status, life_cumu_efforts


def init_data():
    life_status = {}
    life_status["Work-out"] = 50
    life_status["Research"] = 50
    life_status["Reading"] = 50
    life_status["Meditation"] = 50
    life_status["English learning"] = 50
    life_status["Social"] = 50

    life_cumu_efforts = {}
    life_cumu_efforts["Work-out"] = 5
    life_cumu_efforts["Research"] = 5
    life_cumu_efforts["Reading"] = 5
    life_cumu_efforts["Meditation"] = 5
    life_cumu_efforts["English learning"] = 5
    life_cumu_efforts["Social"] = 5

    return life_status, life_cumu_efforts


def add_meditation(life_cumu_efforts, life_add_rate):
    print("Increase the level of Meditation...")
    life_cumu_efforts["Meditation"] += life_add_rate["Meditation"]


if __name__ == "__main__":
    life_status, life_cumu_efforts = load_data()
    # print("life_status: {}".format(life_status))
    # print("life_cumu_efforts: {}".format(life_cumu_efforts))    

    aspects = ["Work-out",
               "Research",
               "Reading",
               "Meditation",
               "English learning",
               "Social"]

    life_consume_rate = {}
    life_consume_rate["Work-out"] = 5
    life_consume_rate["Research"] = 5
    life_consume_rate["Reading"] = 5
    life_consume_rate["Meditation"] = 5
    life_consume_rate["English learning"] = 5
    life_consume_rate["Social"] = 5

    life_add_rate = {}
    life_add_rate["Work-out"] = 5
    life_add_rate["Research"] = 5
    life_add_rate["Reading"] = 5
    life_add_rate["Meditation"] = 5
    life_add_rate["English learning"] = 5
    life_add_rate["Social"] = 5    

    cur_time = datetime.datetime.now()    
    cur_day = int(cur_time.strftime("%j"))
    cur_year = cur_time.strftime("%Y")
    print("Today is {}th day of {}".format(cur_day, cur_year))

    for asp in aspects:
        life_status[asp] -= life_consume_rate[asp] * (cur_day - start_day)
        life_status[asp] += life_cumu_efforts[asp]

    for asp, health in life_status.items():
        health_sig = None
        display_health = abs(health)
        if health > 0:
            health_sig = '*'
        else:
            health_sig = '-'
        print("{}: {}".format(asp, health_sig * display_health))

    add_meditation(life_cumu_efforts, life_add_rate)
