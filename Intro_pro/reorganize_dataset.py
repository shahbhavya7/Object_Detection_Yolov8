"""
Script to reorganize dataset into YOLO format
Moves images and labels to correct directory structure
"""
import os
import shutil
from pathlib import Path

def reorganize_dataset():
    base_path = Path(r"C:\Users\bhavy\OneDrive\Desktop\Languages\Computer_Vision\Object_Detection_Yolo_V8\data")
    
    # Define source and destination paths
    splits = ['train', 'validation', 'test']
    
    for split in splits:
        print(f"\nProcessing {split} split...")
        
        # Source paths
        images_src = base_path / 'images' / split / 'imgs'
        labels_src = base_path / 'images' / split / 'anns'
        
        # Destination paths
        images_dst = base_path / 'images' / split
        labels_dst = base_path / 'labels' / split
        
        # Skip if source doesn't exist
        if not images_src.exists():
            print(f"  Skipping {split} - source path doesn't exist")
            continue
            
        # Create labels directory if it doesn't exist
        labels_dst.mkdir(parents=True, exist_ok=True)
        
        # Move images from imgs/ to train/
        if images_src.exists() and images_src != images_dst:
            print(f"  Moving images from imgs/ to {split}/")
            for img_file in images_src.glob('*.jpg'):
                dest_file = images_dst / img_file.name
                if not dest_file.exists():
                    shutil.move(str(img_file), str(dest_file))
            
            # Remove empty imgs directory
            try:
                images_src.rmdir()
                print(f"  Removed empty imgs/ directory")
            except:
                print(f"  Could not remove imgs/ directory (may not be empty)")
        
        # Copy labels from anns/ to labels/train/
        if labels_src.exists():
            print(f"  Copying labels from anns/ to labels/{split}/")
            copied = 0
            for label_file in labels_src.glob('*.txt'):
                dest_file = labels_dst / label_file.name
                if not dest_file.exists():
                    shutil.copy2(str(label_file), str(dest_file))
                    copied += 1
            print(f"  Copied {copied} label files")
    
    print("\n✅ Dataset reorganization complete!")
    print("\nNew structure:")
    print("data/")
    print("  ├── images/")
    print("  │   ├── train/")
    print("  │   │   ├── [images].jpg")
    print("  │   ├── validation/")
    print("  │   │   ├── [images].jpg")
    print("  │   └── test/")
    print("  │       ├── [images].jpg")
    print("  └── labels/")
    print("      ├── train/")
    print("      │   ├── [labels].txt")
    print("      ├── validation/")
    print("      │   ├── [labels].txt")
    print("      └── test/")
    print("          ├── [labels].txt")

if __name__ == '__main__':
    reorganize_dataset()
