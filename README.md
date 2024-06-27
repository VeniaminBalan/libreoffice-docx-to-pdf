## Docker compose
services: \
  &emsp;converter:  
    &emsp;&emsp;image: ghcr.io/veniaminbalan/docx2pdf:latest \
   &emsp; &emsp;container_name: converter \
    &emsp;&emsp;&emsp;ports: \
     &emsp;&emsp;&emsp;&emsp; - "5000:5000"

## Request curl
curl -X POST http://127.0.0.1:5000/convert \
  -F "file=@/path/to/your/document.docx" \
  -F "method=file"


## Lisence
This project is licensed under the MIT License - see the LICENSE file for details.
