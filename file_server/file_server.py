from app import Blueprint, render_template, redirect, url_for, flash

file_server = Blueprint('file_server', __name__,template_folder="templates")

@file_server.route('/')
def index():
    return "<h2>Files Server</h2>"