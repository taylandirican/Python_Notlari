mlist=[1,2,3]
# print(len(mlist))




class Movie:
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("movie obje oldu")
    def __str__(self) -> str:
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print("movie objesi silindi")
m = Movie("film adi","yönetmen adi",120)
# print(type(m))
# print(len(m))



# print(mlist)
# print(m)
# print(len(mlist))
# print(len(m))


print(m)
# https://www.informit.com/articles/article.aspx?p=453682&seqNum=6#:~:text=The%20names%20of%20special%20methods,%5D%2C%20is%20mapped%20to%20x.
# ^^^^^^^^^^^^^^
# diğer metodlar
