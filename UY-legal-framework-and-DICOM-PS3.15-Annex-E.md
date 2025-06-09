To ensure that a DICOM image can be used for educational or research purposes in Uruguay without violating personal and sensitive data legislation, it is necessary to address both the national **legal framework** and the **de-identification techniques** defined in the DICOM standard. The key aspects are described below.

---

### 1. Uruguayan Legal Framework

* **Law No. 18,331 (August 11, 2008)** on Personal Data Protection and Habeas Data Actions.

* Defines “personal data” as any information that identifies or makes a natural person identifiable.
* Classifies as **sensitive data** those that reveal racial origin, religious beliefs, union membership, and **information about health** or sexual life. The processing of sensitive data requires **express written consent** from the data subject, except for legal exceptions such as academic or research studies authorized by an ethics committee ([pdelc.com.uy][1]).
* **Regulatory Decree 414/009 (08/31/2009)** sets forth the obligations of database controllers, including:

* Implement **technical security measures** to safeguard the integrity and confidentiality of the data (Art. 7) ([biblioteca.protecdatacolombia.com][2]).
* Register all processing activities involving sensitive data in the Personal Database Registry, and keep the technical description and adopted security measures up to date (Art. 16) ([biblioteca.protecdatacolombia.com][2]).
* **Ethics Committee and IRB**: For research projects, approval must be obtained from an institutional ethics committee, which will evaluate the anonymization and data management plan.

---

### 2. Principles of Anonymization and Pseudonymization

* **Complete Anonymization**: Irreversible elimination of all data that allows re-identification, both direct (name, ID) and indirect (exact dates, internal codes).
* **Pseudonymization**: Replacement of direct identifiers with random codes, maintaining an encrypted and protected "master record" that allows internal traceability without exposing identity ([pdelc.com.uy][1]).
* **Data Minimization**: Retaining only the attributes strictly necessary for the educational or research purpose (e.g., study modality, protocol type), discarding all superfluous elements.

---

### 3. DICOM Confidentiality Profile (PS3.15 Annex E)

The DICOM standard defines de-identification profiles in Part 15, Annex E:

* **Basic Application Level Confidentiality Profile**: Removes or clears (action codes X/Z/D) attributes containing PHI (Patient Name, ID, Birth Date, UIDs, dates, institution, requesting physician, etc.) ([dicom.nema.org][3], [wiki.cancerimagingarchive.net][4]).
* **Options**:

* *Clean Pixel Data Option* (E.3.1): Erases any burned-in text on pixels.
* *Clean Recognizable Visual Features Option* (E.3.2): If the image shows facial features (head CT), apply blurring or blackout.

* *Retain Longitudinal Temporal Information Options* (E.3.6):

* **Full Dates**: Retains original dates if essential, marking LongitudinalTemporalInformationModified = UNMODIFIED.
* **Modified Dates**: Shifts dates by a consistent offset (e.g., +365 days), preserving the temporal relationship, and marking MODIFIED ([dicom.innolitics.com][5]).

---

### 4. Practical De-Identification Steps

1. **Attribute Inventory**: Create a list of DICOM tags to process, typically:

* **Patient**: (0010,0010) Name, (0010,0020) ID, (0010,0030) Date of Birth, (0010,0040) Sex
* **Study/Series**: (0008,0020) Study Date, (0008,0030) Study Time, (0008,0050) Accession Number
* **Team/Institution**: (0008,0080) Institution Name, (0008,0090) Referring Physician
* **Identifiers**: (0008,0018) SOP Instance UID, (0020,000D) Study Instance UID
2. **Removal or Replacement**: Apply action codes 'X' (remove), 'Z' (zero-length), or 'D' (dummy value) according to DICOM PS3.15, Annex E, Table E.1-1 ([aliza-dicom-viewer.com][6]).
3. **Pixel Treatment**: If there is burn-in of text or identifiable facial features, use image editing tools to darken or blur them before saving.
4. **Dates and Times**: If exact dates are not required, replace them with dummy values ​​or shift them consistently.
5. **Pseudonymization**: If internal tracking is required, generate a random identifier (UUID) and save correspondence in a protected file with restricted access.
6. **Process Log**: Document each step of the anonymization process, with an audit trail of changes and a checksum of the resulting files.

---

### 5. Tools and Validation

* **Open-source libraries**:

* **pydicom + pynetdicom**: Configurable anonymization script with DICOM profiles.
* **DCMTK**: `dcmodify`, `dcmdel`, `dcmanon` utilities to remove tags and apply profiles.
* **Validation**:

* Verify with a DICOM viewer that sensitive attributes do not appear.
* Run an automatic scan with utilities such as `dicom-anonymizer-validator`.
* **Compliance**:

* Submit the anonymization protocol to the Personal Data Regulatory and Control Unit (URCDP) to ensure compliance with Decree 414/009.
* Obtain a report from the ethics committee accrediting the measures and exceptions (research/teaching).

---

**Summary:** Proper anonymization of DICOM images in Uruguay requires (1) adherence to Law 18.331 and Decree 414/009, (2) application of the DICOM PS3.15 Basic Application Level Confidentiality Profile and its options, (3) removal of metadata and pixels containing PHI, (4) documentation and validation of the process, and (5) ethical approval and, if necessary, notification or registration with the URCDP. This ensures both the protection of patient privacy and the viability of using the images in educational and research contexts.

[1]: https://www.pdelc.com.uy/es/novedades/corporativo/nueva-guia-de-proteccion-de-datos-personales/?utm_source=chatgpt.com "Nueva Guía de Protección de Datos Personales"
[2]: https://biblioteca.protecdatacolombia.com/wp-content/uploads/2024/06/Decreto-Numero-414-del-2009-Uruguay.pdf?utm_source=chatgpt.com "[PDF] REGLAMENTACION DE LA LEY 18.331, RELATIVO A LA ..."
[3]: https://dicom.nema.org/medical/dicom/current/output/chtml/part15/ps3.15.html?utm_source=chatgpt.com "PS3.15 - DICOM - NEMA"
[4]: https://wiki.cancerimagingarchive.net/display/TSKB?utm_source=chatgpt.com "DICOM Basic Attribute Confidentiality Profile"
[5]: https://dicom.innolitics.com/ciods/rt-plan/sop-common/00280303?utm_source=chatgpt.com "Longitudinal Temporal Information Modified Attribute"
[6]: https://www.aliza-dicom-viewer.com/manual/dicom-specification/application-level-confidentiality-profile-attributes?utm_source=chatgpt.com "DICOM Application Level Confidentiality Profile Attributes"

---
---

# Spanish translate

Para garantizar que una imagen DICOM pueda utilizarse con fines educativos o de investigación en Uruguay sin vulnerar la legislación sobre datos personales y datos sensibles, es necesario abordar tanto el **marco legal** nacional como las **técnicas de de‐identificación** definidas en el estándar DICOM. A continuación, se describen los aspectos clave.

---

### 1. Marco legal uruguayo

* **Ley N° 18.331 (11/08/2008)** de Protección de Datos Personales y Acción de Habeas Data.

  * Define “datos personales” como toda información que identifica o hace identificable a una persona física.
  * Clasifica como **datos sensibles** aquellos que revelan origen racial, convicciones religiosas, afiliación sindical, e **informaciones sobre salud** o vida sexual. El tratamiento de datos sensibles requiere **consentimiento expreso y escrito** del titular, salvo excepciones legales como estudios académicos o de investigación con autorización de un comité de ética ([pdelc.com.uy][1]).
* **Decreto Reglamentario 414/009 (31/08/2009)** enuncia las obligaciones de los responsables de bases de datos, entre ellas:

  * Implementar **medidas de seguridad técnicas** para resguardar la integridad y confidencialidad de los datos (Art. 7) ([biblioteca.protecdatacolombia.com][2]).
  * Inscribir en el Registro de Bases de Datos Personales toda actividad de tratamiento que incluya datos sensibles, y mantener actualizada la descripción técnica y las medidas de seguridad adoptadas (Art. 16) ([biblioteca.protecdatacolombia.com][2]).
* **Comité de Ética e IRB**: para proyectos de investigación, se debe contar con la aprobación de un comité de ética institucional, que evaluará el plan de anonimización y manejo de datos.

---

### 2. Principios de anonimización y seudonimización

* **Anonimización completa**: eliminación irreversible de todo dato que permita la reidentificación, tanto directo (nombre, cédula) como indirecto (fechas exactas, códigos internos).
* **Seudonimización**: sustitución de identificadores directos por códigos aleatorios, manteniendo un “registro maestro” cifrado y protegido que permita trazabilidad interna sin exponer la identidad ([pdelc.com.uy][1]).
* **Minimización de datos**: conservar únicamente los atributos estrictamente necesarios para el propósito educativo o investigativo (p. ej., modalidad de estudio, tipo de protocolo), descartando todo elemento superfluo.

---

### 3. Perfil de confidencialidad DICOM (PS3.15 Annex E)

El estándar DICOM define perfiles de des-identificación en su parte 15, Annex E:

* **Basic Application Level Confidentiality Profile**: elimina o vacía (action codes X/Z/D) los atributos que contengan PHI (Patient Name, ID, Birth Date, UIDs, fechas, institución, médico solicitante, etc.) ([dicom.nema.org][3], [wiki.cancerimagingarchive.net][4]).
* **Opciones**:

  * *Clean Pixel Data Option* (E.3.1): borra cualquier texto “quemado” (burned-in) en los píxeles.
  * *Clean Recognizable Visual Features Option* (E.3.2): si la imagen muestra rasgos faciales (TC craneal), aplica desenfoque o blackout.
  * *Retain Longitudinal Temporal Information Options* (E.3.6):

    * **Full Dates**: conserva fechas originales si son esenciales, marcando LongitudinalTemporalInformationModified = UNMODIFIED.
    * **Modified Dates**: desplaza fechas por un offset consistente (p. ej., +365 días), preservando la relación temporal, y marca MODIFIED ([dicom.innolitics.com][5]).

---

### 4. Pasos prácticos de des-identificación

1. **Inventario de atributos**: elaborar una lista de tags DICOM a procesar, típicamente:

   * **Paciente**: (0010,0010) Nombre, (0010,0020) ID, (0010,0030) Fecha de nacimiento, (0010,0040) Sexo
   * **Estudio/Serie**: (0008,0020) Study Date, (0008,0030) Study Time, (0008,0050) Accession Number
   * **Equipo/Institución**: (0008,0080) Institution Name, (0008,0090) Referring Physician
   * **Identificadores**: (0008,0018) SOP Instance UID, (0020,000D) Study Instance UID
2. **Eliminación o reemplazo**: aplicar action codes ‘X’ (remove), ‘Z’ (zero-length), o ‘D’ (dummy value) según DICOM PS3.15, Annex E, Table E.1-1 ([aliza-dicom-viewer.com][6]).
3. **Tratamiento de píxeles**: si hay burn-in de texto o rasgos faciales identificables, usar herramientas de edición de imágenes para oscurecer o difuminar antes de guardar.
4. **Fechas y tiempos**: si no se requiere mantener las fechas exactas, reemplazarlas por valores dummy o desplazarlos de forma consistente.
5. **Pseudonimización**: en caso de necesitar mantener rastreo interno, generar un identificador aleatorio (UUID) y guardar la correspondencia en un archivo protegido con acceso restringido.
6. **Registro de proceso**: documentar cada paso de la anonimización, con auditoría de cambios y checksum de los archivos resultantes.

---

### 5. Herramientas y validación

* **Bibliotecas open-source**:

  * **pydicom + pynetdicom**: script de anonimización configurable con perfiles DICOM.
  * **DCMTK**: utilidades `dcmodify`, `dcmdel`, `dcmanon` para remover tags y aplicar perfiles.
* **Validación**:

  * Verificar con un visualizador de DICOM que los atributos sensibles no aparezcan.
  * Ejecutar un escaneo automático con utilidades como `dicom-anonymizer-validator`.
* **Cumplimiento**:

  * Someter el protocolo de anonimización a la Unidad Reguladora y de Control de Datos Personales (URCDP) para asegurar adecuación al Decreto 414/009.
  * Obtener informe de comité de ética donde se acrediten las medidas y excepciones (investigación/enseñanza).

---

**Resumen:** la anonimización correcta de imágenes DICOM en Uruguay exige (1) adherir a la Ley 18.331 y Decreto 414/009, (2) aplicar el Basic Application Level Confidentiality Profile de DICOM PS3.15 y sus opciones, (3) eliminar metadatos y píxeles con PHI, (4) documentar y validar el proceso, y (5) contar con la aprobación ética y, de ser preciso, la notificación o registro ante la URCDP. Esto asegura tanto la protección de la privacidad de los pacientes como la viabilidad de uso de las imágenes en contextos educativos y de investigación.

[1]: https://www.pdelc.com.uy/es/novedades/corporativo/nueva-guia-de-proteccion-de-datos-personales/?utm_source=chatgpt.com "Nueva Guía de Protección de Datos Personales"
[2]: https://biblioteca.protecdatacolombia.com/wp-content/uploads/2024/06/Decreto-Numero-414-del-2009-Uruguay.pdf?utm_source=chatgpt.com "[PDF] REGLAMENTACION DE LA LEY 18.331, RELATIVO A LA ..."
[3]: https://dicom.nema.org/medical/dicom/current/output/chtml/part15/ps3.15.html?utm_source=chatgpt.com "PS3.15 - DICOM - NEMA"
[4]: https://wiki.cancerimagingarchive.net/display/TSKB?utm_source=chatgpt.com "DICOM Basic Attribute Confidentiality Profile"
[5]: https://dicom.innolitics.com/ciods/rt-plan/sop-common/00280303?utm_source=chatgpt.com "Longitudinal Temporal Information Modified Attribute"
[6]: https://www.aliza-dicom-viewer.com/manual/dicom-specification/application-level-confidentiality-profile-attributes?utm_source=chatgpt.com "DICOM Application Level Confidentiality Profile Attributes"
