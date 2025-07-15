import os
from zipfile import ZipFile
from urllib.request import urlretrieve


DATA_ROW_PATH = os.path.abspath(os.path.join(
    os.getcwd(), "../data/raw"))
SCRIPTS_PATH = os.path.abspath(os.path.join(os.getcwd(), "../scripts"))

ZIP_PATH = os.path.abspath(os.path.join(
    DATA_ROW_PATH, "opencv_bootcamp_assets_NB1.zip"))
URL = r"https://www.dropbox.com/s/0o5yqql1ynx31bi/opencv_bootcamp_assets_NB9.zip?dl=1"


def download_unzip(url, save_path):
    print(f"Downloading and extracting assests....", end="")

    # Downloading zip file using urllib package.
    urlretrieve(url, save_path)

    try:
        # Extracting zip file using the zipfile package.
        with ZipFile(save_path) as z:
            for file in z.namelist():
                if file.endswith(".py"):
                    z.extract(file, SCRIPTS_PATH)
                else:
                    z.extract(file, os.path.split(save_path)[0])

        print("\nExtraction completed.")

    except Exception as e:
        print("\nInvalid file.", e)


# Download if assest ZIP does not exists.
if not os.path.exists(ZIP_PATH):
    download_unzip(URL, ZIP_PATH)
else:
    print("\nZip folder already exists")
