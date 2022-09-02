from app import db
from devtools import debug
class ImageModel(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    likes = db.Column(db.Integer,nullable=False)
    views = db.Column(db.Integer,nullable=False)
    
    def __init__(self,id: int,name: str,likes: int,views: int) ->None:
        self.id = id
        self.likes = likes
        self.name = name
        self.views = views
    
    def __repr__(self):
        return self.name
    
    @classmethod
    def get_image_by_id(cls,image_id):
        return cls.query.filter_by(id = image_id)
    
    @classmethod
    def add_image(cls,id,name,likes,views):
        image = cls(id,name,likes,views)
        db.session.add(image)
        db.session.commit()
        return image
    
    @classmethod 
    def update_image(cls,id,name,likes,views):
        image = cls.get_image_by_id(image_id=id).update(values=dict({"name":name,"likes":likes,"views":views}))
        db.session.commit()
        return cls(id,name,likes,views)
    
    @classmethod
    def delete_image(cls,id):
        cls.get_image_by_id(image_id=id).delete()
        db.session.commit()
    
    @classmethod
    def get_all_images(cls):
        return cls.query.all()
        
        