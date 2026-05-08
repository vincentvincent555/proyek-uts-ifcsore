"""
bg_setter.py
=================
Author: Your Team
License: MIT License
Version: 1.0

Background Color Setter Script
This script sets the background of transparent images to a specified RGB color.
It works with PNG images that have transparent backgrounds.
"""

import sys
import os
import time
from PIL import Image
import numpy as np

# Set UTF-8 encoding for better compatibility
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass


class BackgroundColorSetter:
    """
    Class to handle background color setting for images with transparent backgrounds.
    """
    
    def __init__(self):
        """Initialize the background color setter"""
        self.log("="*50)
        self.log("Background Color Setter Initialized!")
        self.log("="*50)
    
    def log(self, message):
        """Print log message with timestamp and flush immediately."""
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        try:
            print(f"[{timestamp}] {message}")
            sys.stdout.flush()
        except UnicodeEncodeError:
            # Fallback for encoding issues
            print(f"[{timestamp}] {message.encode('ascii', 'ignore').decode('ascii')}")
            sys.stdout.flush()
    
    def set_background_color(self, input_path, output_path, rgb_color=(255, 255, 255)):
        """
        Set the background color of an image with transparency.
        
        Args:
            input_path (str): Path to the input PNG image with transparency
            output_path (str): Path to save the output image
            rgb_color (tuple): RGB color tuple (R, G, B) values 0-255
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Validate RGB values
            if not all(0 <= val <= 255 for val in rgb_color):
                self.log(f"[ERROR] Invalid RGB values: {rgb_color}. Values must be 0-255")
                return False
            
            self.log("-"*50)
            self.log(f"[INPUT] Input path: {input_path}")
            self.log(f"[OUTPUT] Output path: {output_path}")
            self.log(f"[COLOR] RGB Color: R={rgb_color[0]}, G={rgb_color[1]}, B={rgb_color[2]}")
            
            # Check if input file exists
            if not os.path.exists(input_path):
                self.log(f"[ERROR] Input file does not exist: {input_path}")
                return False
            
            # Load image
            self.log("[STEP 1/4] Loading image...")
            image = Image.open(input_path)
            self.log(f"[INFO] Image loaded: {image.size[0]}x{image.size[1]} pixels, mode: {image.mode}")
            
            # Check if image has alpha channel (transparency)
            if image.mode != 'RGBA':
                self.log(f"[STEP 2/4] Converting {image.mode} to RGBA...")
                image = image.convert('RGBA')
            else:
                self.log("[STEP 2/4] Image already in RGBA mode")
            
            # Create a new image with the background color
            self.log("[STEP 3/4] Applying background color...")
            start_time = time.time()
            
            # Create background image with specified RGB color
            background = Image.new('RGB', image.size, rgb_color)
            
            # Paste the image with alpha channel onto the background
            # The alpha channel is used as the mask
            background.paste(image, mask=image.split()[3])
            
            processing_time = time.time() - start_time
            self.log(f"[SUCCESS] Background color applied in {processing_time:.2f} seconds")
            
            # Save the result
            self.log("[STEP 4/4] Saving output image...")
            background.save(output_path, 'PNG')
            
            # Verify output file was created
            if not os.path.exists(output_path):
                self.log("[ERROR] Output file generation failed!")
                return False
            
            file_size = os.path.getsize(output_path)
            self.log(f"[SUCCESS] Image saved successfully!")
            self.log(f"[INFO] Output file size: {file_size / 1024:.2f} KB")
            self.log("-"*50)
            return True
        
        except Exception as e:
            self.log(f"[ERROR] Error processing image: {str(e)}")
            return False
    
    def batch_set_background(self, input_dir, output_dir, rgb_color=(255, 255, 255)):
        """
        Process multiple images in a directory.
        
        Args:
            input_dir (str): Directory containing input images
            output_dir (str): Directory to save output images
            rgb_color (tuple): RGB color tuple (R, G, B)
        
        Returns:
            dict: Dictionary with processing statistics
        """
        stats = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'errors': []
        }
        
        try:
            # Create output directory if it doesn't exist
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                self.log(f"[INFO] Created output directory: {output_dir}")
            
            # Get all PNG files in the input directory
            png_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.png')]
            
            if not png_files:
                self.log("[WARNING] No PNG files found in input directory")
                return stats
            
            self.log(f"[INFO] Found {len(png_files)} PNG files to process")
            
            for png_file in png_files:
                stats['total'] += 1
                input_path = os.path.join(input_dir, png_file)
                output_filename = f"bg_colored_{os.path.splitext(png_file)[0]}.png"
                output_path = os.path.join(output_dir, output_filename)
                
                self.log(f"\n[PROCESSING] File {stats['total']}/{len(png_files)}: {png_file}")
                
                if self.set_background_color(input_path, output_path, rgb_color):
                    stats['success'] += 1
                else:
                    stats['failed'] += 1
                    stats['errors'].append(png_file)
            
            self.log(f"\n{'='*50}")
            self.log(f"[SUMMARY] Batch processing completed!")
            self.log(f"[SUMMARY] Total: {stats['total']}, Success: {stats['success']}, Failed: {stats['failed']}")
            self.log(f"{'='*50}")
            
            return stats
        
        except Exception as e:
            self.log(f"[ERROR] Error in batch processing: {str(e)}")
            return stats


# Command line interface
if __name__ == "__main__":
    setter = BackgroundColorSetter()
    
    if len(sys.argv) < 3:
        print("\nUsage:")
        print("  python bg_setter.py <input_image> <output_image> [R] [G] [B]")
        print("\nExample:")
        print("  python bg_setter.py input.png output.png 255 0 0      # Red background")
        print("  python bg_setter.py input.png output.png 0 255 0      # Green background")
        print("  python bg_setter.py input.png output.png 0 0 255      # Blue background")
        print("  python bg_setter.py input.png output.png 255 255 255  # White background (default)")
        print("\nIf RGB values are not provided, default is white (255, 255, 255)")
    else:
        input_image = sys.argv[1]
        output_image = sys.argv[2]
        
        # Default to white if RGB not provided
        rgb = (255, 255, 255)
        
        if len(sys.argv) >= 5:
            try:
                r = int(sys.argv[3])
                g = int(sys.argv[4])
                b = int(sys.argv[5])
                rgb = (r, g, b)
            except ValueError:
                setter.log("[ERROR] RGB values must be integers (0-255)")
                sys.exit(1)
        
        success = setter.set_background_color(input_image, output_image, rgb)
        sys.exit(0 if success else 1)
