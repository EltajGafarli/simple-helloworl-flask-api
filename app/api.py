from app import app
from flask_restful import Api
from flask_restful import Resource
from flask_restful import abort
from flask_restful import reqparse
from flask_restful import fields
from flask_restful import marshal_with

from app.model import ImageModel

img_put_args = reqparse.RequestParser()

img_put_args.add_argument('name',type=str,help='The name of Image is required',required=True)
img_put_args.add_argument('likes',type=int,help='The Likes of Image is required',required=True)
img_put_args.add_argument('views',type=int,help='The Views of Image is required',required=True)


api = Api(app=app)

resources_fields = {
    "id":fields.Integer,
    "name":fields.String,
    "likes":fields.Integer,
    "views":fields.Integer,
}

class HelloWorld(Resource):
    @marshal_with(resources_fields)
    def get(self,image_id = None):
        if image_id == None:
            result = ImageModel.get_all_images()
            return result
        result = ImageModel.get_image_by_id(image_id=image_id)
        result = result.first()
        return result
    
    @marshal_with(resources_fields)
    def put(self,image_id):
        args = img_put_args.parse_args()

        if ImageModel.get_image_by_id(image_id=image_id).first() != None:
            result = ImageModel.update_image(id=image_id,name=args['name'],likes=args['likes'],views=args['views'])
            return result
        
        result = ImageModel.add_image(id=image_id,name=args['name'],likes=args['likes'],views=args['views'])
        return result
        
    
    def delete(self,image_id):
        if ImageModel.get_image_by_id(image_id=image_id).first() == None:
            abort(404,message="404 Image Not Found")
        ImageModel.delete_image(image_id)
        return '',204
    
class MainPage(Resource):
    @marshal_with(resources_fields)
    def get(self):
        result = ImageModel.get_all_images()
        return result
    
api.add_resource(MainPage,"/api/hello")           
api.add_resource(HelloWorld,"/api/hello/<int:image_id>")
