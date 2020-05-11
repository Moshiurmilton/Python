class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    @classmethod #( ক্লাস মেথোডকে ডাকা হচ্ছে ক্ষমতা দেওয়া হচ্ছে।)
    def new_square(cls, side_length): # এই নিউ স্কয়ার মেথোড! আসো। উপরের ক্লাসকে সাইড লেনথ নামক আর্গুমেন্ট দ্বারা মোডিফাই করবে।)
        return cls(side_length, side_length) #(শোন কীভাবে করতে হবে। উপরের ক্লাসের আর্গুমেন্টদ্বয়কে দুইটি একই সাইড লেনথ আর্গুমেন্ট দ্বারা প্রতিস্থাপিত করবে।
    # ওকে ঠিক আছে বস। আদেশ দিন।
square = Rectangle.new_square(5)
print(square.calculate_area())
