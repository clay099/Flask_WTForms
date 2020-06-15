from app import db
from models import Pet

db.drop_all()
db.create_all()

p1 = Pet(name="Doug", species="Dog", photo_url="https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12234558/Chinook-On-White-03.jpg",
         age="4", notes="loves to run", available=True)
p2 = Pet(name="Fin", species="Dog", photo_url="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg",
         age="0", notes="", available=True)
p3 = Pet(name="Jane", species="Cat", photo_url="",
         age="8", notes="", available=False)
p4 = Pet(name="Silver", species="Cat", photo_url="https://i0.wp.com/www.web24.news/u/wp-content/uploads/2020/05/Baby-cat-should-die-in-garbage-press-and-meowed-for.img.jpeg?fit=1200%2C630&ssl=1", age="0", notes="", available=True)
p5 = Pet(name="Kitty", species="Cat", photo_url="https://theme.visualmodo.com/petshop/wp-content/uploads/sites/53/2018/07/Gallery-Cats-Petshop-WordPress-Theme.jpg1", age="0", notes="", available=True)
p6 = Pet(name="Spiky", species="Porcupine",
         photo_url="https://www.nationalgeographic.com/content/dam/yourshot/2014/08/4254384.jpg", age="18", notes="", available=True)
p7 = Pet(name="Pizza", species="Dog",
         photo_url="https://thestacker.com/sites/default/files/styles/properly_sized_image/public/2020-03/English%20Lab%20Puppy%20%281%29_0.png", age="0", notes="", available=False)


db.session.add_all([p1, p2, p3, p4, p5, p6, p7])
db.session.commit()
