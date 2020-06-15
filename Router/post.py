from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..Controller.PostController import PostController

post = Blueprint('post', __name__)
CORS(post, resources={r"/*": {"origins": "*"}})


@post.route('/get-posts', methods=['GET'])
def get_posts():
    return PostController().get_posts()


@post.route('/create-post', methods=['POST'])
def create_post():
    PostController().create_post(request.get_json())
    return jsonify({'response': 'Ok'})


@post.route('/update-post', methods=['POST'])
def update_post():
    PostController().update_post(request.get_json())
    return jsonify({'response': 'Ok'})


@post.route('/delete-post', methods=['POST'])
def delete_post():
    PostController().delete_post(request.get_json())
    return jsonify({'response': 'Ok'})


@post.route('/update-post-position', methods=['POST'])
def update_post_position():
    return PostController().update_post_position(request.get_json())


@post.route('/bulk-activate-posts', methods=['POST'])
def bulk_activate_posts():
    PostController().bulk_activate_posts(request.get_json())
    return jsonify({'response': 'Ok'})


@post.route('/bulk-deactivate-posts', methods=['POST'])
def bulk_deactivate_posts():
    PostController().bulk_deactivate_posts(request.get_json())
    return jsonify({'response': 'Ok'})


@post.route('/bulk-delete-posts', methods=['POST'])
def bulk_delete_posts():
    PostController().bulk_delete_posts(request.get_json())
    return jsonify({'response': 'Ok'})
