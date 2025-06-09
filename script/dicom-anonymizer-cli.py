
# dicom-anonymizer-cli-py
# Version: 1.0.0 2025.06.09
# Author: Alejandro Ferrari - aleferrari.uy@gmail.com

import os
import argparse
import logging
from pydicom import dcmread, dcmwrite
from pydicom.uid import generate_uid

# Lista de etiquetas que deben ser anónimizaradas o eliminadas según normativa / List of tags that must be anonymized or removed according to regulations
TAG_BLACKLIST = [
    'PatientName', 'PatientID', 'PatientBirthDate', 'PatientSex',
    'InstitutionName', 'InstitutionAddress', 'ReferringPhysicianName',
    'StudyID', 'AccessionNumber', 'StudyDate', 'StudyTime',
    'SeriesDate', 'SeriesTime', 'PerformingPhysicianName',
    'OperatorsName', 'OtherPatientIDs', 'OtherPatientNames',
    # ... agregar más etiquetas sensibles según requerimientos / add more sensitive labels as required
]

# Etiquetas de UIDs que deben ser regeneradas / UID labels that need to be regenerated
UID_TAGS = [
    'StudyInstanceUID', 'SeriesInstanceUID', 'SOPInstanceUID',
    'MediaStorageSOPInstanceUID'
]


def anonymize_dicom(src_path: str, dst_path: str, overwrite: bool = False) -> None:
    ds = dcmread(src_path)
    # Eliminar etiquetas privadas / Remove private labels
    ds.remove_private_tags()

    # Anonimizar campos de identidad / Anonymize identity fields
    for tag in TAG_BLACKLIST:
        if hasattr(ds, tag):
            setattr(ds, tag, '')

    # Regenerar UIDs / Regenerate UIDs
    for tag in UID_TAGS:
        if hasattr(ds, tag):
            setattr(ds, tag, generate_uid())

    # Escribir archivo anónimo / Write anonymous file
    out_path = dst_path
n    if os.path.isdir(dst_path):
        basename = os.path.basename(src_path)
        out_path = os.path.join(dst_path, basename)

    if os.path.exists(out_path) and not overwrite:
        logging.warning(f"El archivo {out_path} ya existe. Use -w para sobreescribir.")
        return

    dcmwrite(out_path, ds)
    logging.info(f"Archivo anonimizado: {out_path}")


def walk_and_anonymize(input_dir: str, output_dir: str, overwrite: bool = False) -> None:
    for root, _, files in os.walk(input_dir):
        rel = os.path.relpath(root, input_dir)
        target_root = os.path.join(output_dir, rel)
        os.makedirs(target_root, exist_ok=True)
        for f in files:
            if f.lower().endswith('.dcm'):
                src = os.path.join(root, f)
                anonymize_dicom(src, target_root, overwrite)


def main():
    parser = argparse.ArgumentParser(
        description='Anonimizador de estudios DICOM para uso académico'
    )
    parser.add_argument('input', help='Directorio o archivo DICOM de entrada')
    parser.add_argument('output', help='Directorio de salida para archivos anonimizados')
    parser.add_argument('-w', '--overwrite', action='store_true', help='Sobrescribir archivos existentes')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    if os.path.isfile(args.input) and args.input.lower().endswith('.dcm'):
        os.makedirs(args.output, exist_ok=True)
        anonymize_dicom(args.input, args.output, args.overwrite)
    elif os.path.isdir(args.input):
        walk_and_anonymize(args.input, args.output, args.overwrite)
    else:
        parser.error('Entrada debe ser un archivo .dcm o un directorio')

if __name__ == '__main__':
    main()
