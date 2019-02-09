from generate_images import generate_images
from connect_sql import connect_sql

path = r"C:\Users\Administrator\PycharmProjects\docx_project\files\results"
turbine_list = ['GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'En2.5-141']
generate_images(path, turbine_list)
