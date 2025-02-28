import io
import requests
from PIL import Image
import fitz  # PyMuPDF

def extract_images_from_pdf(pdf_url, max_images=3):
    """
    Extract images from a PDF file given its URL.
    
    Args:
    pdf_url (str): URL of the PDF file
    max_images (int): Maximum number of images to extract
    
    Returns:
    list: List of PIL Image objects
    """
    try:
        # Download the PDF file
        response = requests.get(pdf_url)
        pdf_content = io.BytesIO(response.content)
        
        # Open the PDF file
        doc = fitz.open(stream=pdf_content, filetype="pdf")
        
        images = []
        for page in doc:
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                if len(images) >= max_images:
                    break
                
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                
                # Convert to PIL Image
                image = Image.open(io.BytesIO(image_bytes))
                images.append(image)
            
            if len(images) >= max_images:
                break
        
        return images
    
    except Exception as e:
        print(f"Error extracting images from PDF: {e}")
        return []

