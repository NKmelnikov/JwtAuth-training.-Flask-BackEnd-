from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Service.PostService import PostService
from ..Model.PostModel import PostModel
import json

post = Blueprint('post', __name__)
CORS(post, resources={r"/*": {"origins": "*"}})


@post.route('/get-posts', methods=['GET'])
def get_posts():
    return PostService(PostModel).get_all()


@post.route('/create-post', methods=['POST'])
def create_post():
    PostService(PostModel).create_post(request.get_json())
    PostService(PostModel).update_position(json.loads(PostService(PostModel).get_all()))
    return jsonify({'response': 'Ok'})


@post.route('/update-post', methods=['POST'])
def update_post():
    PostService(PostModel).update_post(request.get_json())
    return jsonify({'response': 'Ok'})


@post.route('/delete-post', methods=['POST'])
def delete_post():
    PostService(PostModel).delete(request.get_json())
    PostService(PostModel).update_position(json.loads(PostService(PostModel).get_all()))
    return jsonify({'response': 'Ok'})


@post.route('/update-post-position', methods=['POST'])
def update_post_position():
    return PostService(PostModel).update_position(request.get_json())


@post.route('/bulk-activate-posts', methods=['POST'])
def bulk_activate_posts():
    PostService(PostModel).bulk_activate(request.get_json())
    return jsonify({'response': 'Ok'})


@post.route('/bulk-deactivate-posts', methods=['POST'])
def bulk_deactivate_posts():
    PostService(PostModel).bulk_deactivate(request.get_json())
    return jsonify({'response': 'Ok'})


@post.route('/bulk-delete-posts', methods=['POST'])
def bulk_delete_posts():
    PostService(PostModel).bulk_delete(request.get_json())
    PostService(PostModel).update_position(json.loads(PostService(PostModel).get_all()))
    return jsonify({'response': 'Ok'})
