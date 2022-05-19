import requests
import glob
import config as cfg
from zipfile import ZipFile


def download_latest_data(state):
    url = cfg.WETLANDS_DOWNLOAD_URL.format(state)
    print(f"Download data from {url}...")
    requests.get(url)


def extract_shapefile(zip_filename, shp_filename):
    print("Unzipping main file")
    with ZipFile(f"{zip_filename}.zip", "r") as zip_obj:
        zip_obj.extractall()
    shapefile = glob.glob(f'./{zip_filename}/{shp_filename}.*')
    print(f"Creating new zip with {shp_filename}")
    with ZipFile(f"{shp_filename}.zip", "w") as zip_obj:
        [zip_obj.write(file) for file in shapefile]



def main():
    state = "FL"
    download_latest_data(state)
    zip_filename = cfg.WETLANDS_ZIP_FILENAME.format(state)
    shp_filename = cfg.WETLANDS_SHP_FILENAME.format(state)
    extract_shapefile(zip_filename, shp_filename)

main()


