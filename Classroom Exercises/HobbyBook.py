#Your name
#Your age
#A list of a few of your hobbies
#A dictionary of a few times you wake up during the week
my_info={"name":"Justin",
            "age":36,
            "gender":"male",
            "hobbies":["golf", "running", "home improvement"],
            "wake_up":{"Mon-Fri":"5:00", "Sat":"7:00", "Sun":"8.00"}}

print(my_info[name], len(my_info[hobbies]), my_info[wake_up][Sun])
