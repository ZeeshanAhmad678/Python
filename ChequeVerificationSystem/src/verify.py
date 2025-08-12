import cv2
import numpy as np

def load_and_prepare(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Image not found: {img_path}")
    resized = cv2.resize(img, (220, 155))
    

    # Reject nearly blank images
    if np.mean(resized) > 245:  
        print(f" Image at {img_path} appears blank or too white.")
        return None

    return resized

def compare_signatures(img1_path, img2_path, match_threshold=0.11):
    img1 = load_and_prepare(img1_path)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

   

    if img1 is None or img2 is None:
        print(" Cannot compare: one of the images is invalid.")
        return False, 0.0

    sift = cv2.SIFT_create()

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    if des1 is None or des2 is None:
        print("Not enough features detected.")
        return False, 0.0

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    match_count = len(good_matches)
    print(" Matches (SIFT):", match_count)

    match_score = match_count / max(len(kp1), len(kp2))  # Normalize
    is_match = match_score >= match_threshold

    return is_match, match_score
