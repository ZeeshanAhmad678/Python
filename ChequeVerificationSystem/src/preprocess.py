import cv2
import numpy as np
import os

def extract_signature(image_path="original.jpg", output_path=None):
    if not os.path.exists(image_path):
        print(f" Image not found: {image_path}")
        return None

    # Load original image
    image = cv2.imread(image_path)
    original_height, original_width = image.shape[:2]
    
    # Create visualization image
    vis_image = image.copy()
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate contrast
    contrast = np.std(gray)
    print(f"Contrast Level: {contrast:.1f}")

    # Apply enhancement
    if contrast < 30:
        gray = cv2.filter2D(gray, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))
    elif contrast < 60:
        gray = cv2.bilateralFilter(gray, 9, 75, 75)

    
    roi_width = 400 
    roi_height = 170   
    
   
    base_x = int(original_width * 0.71)  
    base_y = int(original_height * 0.59)  
    
    
    roi_x = base_x - 20 
    roi_y = base_y - 50  
    
    
    roi_x = max(0, roi_x)
    roi_y = max(0, roi_y)
    
    
    if roi_x + roi_width > original_width or roi_y + roi_height > original_height:
        print(" Requested ROI would extend beyond image boundaries")
        return None

    
    signature_roi = gray[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
    
    
    edges = cv2.Canny(signature_roi, 50, 150)
    

    cv2.rectangle(vis_image, (roi_x, roi_y), (roi_x+roi_width, roi_y+roi_height), 
                  (0, 255, 0), 2)
   
    cv2.putText(vis_image, f"ROI: {roi_width}x{roi_height}", (roi_x, roi_y-10), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    
    resized_vis = cv2.resize(vis_image, (800, int(800*original_height/original_width)))
    cv2.imshow("Cheque with Precise Signature ROI", resized_vis)
    cv2.waitKey(500)
    
   
    cv2.imshow(" Signature ROI", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if output_path:
        cv2.imwrite(output_path, edges)
        print(f"  Signature saved at: {output_path}")
        return output_path
    else:
        return edges

