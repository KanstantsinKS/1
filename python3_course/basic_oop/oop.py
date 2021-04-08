class MyFirstClass:
    pass
object_of_my_class = MyFirstClass()
print(type(object_of_my_class))

class Car:

    wheels_number = 4

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

mazda_car = Car(model='Mazda SX7', color="Black", year=2017)
print(mazda_car.model)

bmw_car = Car(model="BMW", color="White", year=2020)
print(bmw_car.model)
print(bmw_car.color)
print(bmw_car.year)

number_of_wheels_of_3_cars = Car.wheels_number * 3
print(number_of_wheels_of_3_cars)

class BlogPost():
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes

blog_post_1 = BlogPost("Jake", "It's a Jake post", "20 likes")
blog_post_2 = BlogPost("Jane", "It's a Jane post", "20 likes")

blog_post_2.number_of_likes = "50 likes"

print(blog_post_1.number_of_likes)
print(blog_post_2.number_of_likes)


class BlogPost():
    number_of_likes = 0
    def __init__(self,user_name, text):
        self.user_name = 'name'
        self.text = 'text'


blog_post1 = BlogPost(user_name='Nataly', text='Привет Букет')
blog_post2 = BlogPost(user_name= 'Василий', text='как дела сегодня')
blog_post1.number_of_likes = 5

print(blog_post1.number_of_likes)
print(blog_post2.number_of_likes)