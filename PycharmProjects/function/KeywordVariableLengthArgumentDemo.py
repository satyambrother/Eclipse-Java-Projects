def display(**kwargs):
    print("record information")
    for k,v in kwargs.items():
        print(k,"....",v)
display(name='satyam',marks=100,age=18,gf='sad')
display(name='deepak',wife1='sadhavi',wife2='pragya')
display(name="beer",brand1="kf",brand2="rc")