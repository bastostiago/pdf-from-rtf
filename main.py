import pandas as pd
import os
from log_config import logger

# CONFIG
data_origin_path = "./arquivos_csv"
pdf_file_path = "./pdf"
libre_office_path = "C:\Program Files\LibreOffice\program\soffice.exe"


if __name__ == "__main__":

    logger.info("Starting application")

    for filename in os.listdir(data_origin_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(data_origin_path, filename)
            df = pd.read_csv(filepath)

            # iterate DF lines
            for index, line in df.iterrows():
                rtf_code = line["DS_LAUDO"]
                rtf_name = line["NR_SEQUENCIA"]

                # write a temp rtf file
                rtf_file_path = f'{rtf_name}.rtf'
                with open(rtf_file_path, "w") as rtf_file:
                    rtf_file.write(rtf_code)

                # create pdf on destination
                if not os.path.isfile(os.path.join(pdf_file_path, f'{rtf_name}.pdf')):
                    os.system(f'"{libre_office_path}" --headless --convert-to pdf --outdir {pdf_file_path} {rtf_file_path}')
                    logger.info(f'Created file {rtf_name}')

                # delete temp rtf files
                os.remove(rtf_file_path)
