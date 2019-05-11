import datetime

start_year = 2019
start_day = 100


if __name__ == "__main__":
    aspects = ["Work-out",
               "Research",
               "Reading",
               "Meditation",
               "English learning",
               "Social"]

    life_status = {}
    life_status["Work-out"] = 50
    life_status["Research"] = 50
    life_status["Reading"] = 50
    life_status["Meditation"] = 50
    life_status["English learning"] = 50
    life_status["Social"] = 50

    life_consume_rate = {}
    life_consume_rate["Work-out"] = 5
    life_consume_rate["Research"] = 5
    life_consume_rate["Reading"] = 5
    life_consume_rate["Meditation"] = 5
    life_consume_rate["English learning"] = 5
    life_consume_rate["Social"] = 5

    life_cumu_efforts = {}
    life_cumu_efforts["Work-out"] = 5
    life_cumu_efforts["Research"] = 5
    life_cumu_efforts["Reading"] = 5
    life_cumu_efforts["Meditation"] = 5
    life_cumu_efforts["English learning"] = 5
    life_cumu_efforts["Social"] = 5

    cur_time = datetime.datetime.now()    
    cur_day = int(cur_time.strftime("%j"))
    print("Today is {}".format(cur_day))

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
