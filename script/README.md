## Releases

| Version | Date | Type | Release-notes | Functionality |
|:-------:|:----:|:----:|:--------------|:-------------:|
|1.0.0|2025.06.09| Enhancement |- Recursively traverses directories and processes .dcm files. - Removes private tags and sensitive fields (name, ID, dates, etc.). - Regenerates key UIDs to maintain study consistency without exposing the originals. - Writes anonymized files to the output path, with the -w/--overwrite option.|Parcial|
||||||
