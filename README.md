## Docker compose
services:
  converter: 
    image: ghcr.io/veniaminbalan/docx2pdf:latest
    container_name: converter
    ports:
      - "5000:5000"

## Request curl
curl -X POST http://127.0.0.1:5000/convert \
  -F "file=@/path/to/your/document.docx" \
  -F "method=file"


## Lisence
This project is licensed under the MIT License - see the LICENSE file for details.
