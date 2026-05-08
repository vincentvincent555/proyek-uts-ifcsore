"""
bg_setter_gui_new.py
=====================
Author: Your Team
License: MIT License
Version: 2.0

GUI Application for Background Color Setter
Features: Real-time preview, side-by-side image display, and output save
"""

import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser
import tkinter.font as tkfont
from pathlib import Path
import threading
from PIL import Image, ImageTk
import subprocess

# Import the background setter module
from bg_setter import BackgroundColorSetter


class BGSetterGUI(tk.Tk):
    """
    GUI application for setting background colors on transparent images.
    """
    
    def __init__(self):
        super().__init__()
        self.title("Background Color Setter - Image Preview")
        self.geometry("1600x950")
        self.resizable(True, True)
        self.minsize(1400, 850)
        
        # Initialize variables
        self.setter = BackgroundColorSetter()
        self.current_color = (255, 255, 255)  # Default white
        self.input_image_path = None
        self.output_image_path = None
        self.is_processing = False
        self.input_pil_image = None
        self.input_photo_image = None
        self.output_photo_image = None
        
        # Font configuration
        default_font = tkfont.nametofont("TkDefaultFont")
        self.font_family = default_font.actual()["family"]
        
        # Dark theme colors
        self.colors = {
            'bg_primary': '#1e1e1e',
            'bg_secondary': '#2d2d2d',
            'bg_tertiary': '#404040',
            'text_primary': '#e0e0e0',
            'text_secondary': '#a0a0a0',
            'accent': '#00d9ff',
            'accent_hover': '#00b8d4',
            'success': '#4caf50',
            'error': '#f44336',
        }
        
        # Configure theme
        self.configure(bg=self.colors['bg_primary'])
        self.style = ttk.Style()
        self._configure_styles()
        
        # Build UI
        self._create_widgets()
    
    def _configure_styles(self):
        """Configure ttk styles."""
        self.style.theme_use('clam')
        
        self.style.configure(
            'TButton',
            font=(self.font_family, 9),
            background=self.colors['bg_secondary'],
            foreground=self.colors['text_primary'],
            borderwidth=1,
            padding=6
        )
        
        self.style.configure(
            'TLabel',
            background=self.colors['bg_primary'],
            foreground=self.colors['text_primary'],
            font=(self.font_family, 9)
        )
        
        self.style.configure(
            'TFrame',
            background=self.colors['bg_primary']
        )
        
        self.style.configure(
            'TLabelframe',
            background=self.colors['bg_primary'],
            foreground=self.colors['text_primary'],
            font=(self.font_family, 10, 'bold')
        )
    
    def _create_widgets(self):
        """Create all GUI widgets."""
        # Main container
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(
            main_frame,
            text="🎨 Background Color Setter - Real-time Image Preview",
            font=(self.font_family, 13, 'bold')
        )
        title_label.pack(pady=(0, 10))
        
        # Create PanedWindow for left controls and right image preview
        paned = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Controls
        left_panel = ttk.Frame(paned)
        paned.add(left_panel, weight=1)
        
        # Right panel - Image Preview
        right_panel = ttk.Frame(paned)
        paned.add(right_panel, weight=2)
        
        # Create control widgets
        self._create_control_widgets(left_panel)
        
        # Create image preview widgets
        self._create_image_preview_widgets(right_panel)
    
    def _create_control_widgets(self, parent):
        """Create control panel widgets."""
        # File Selection Frame
        file_frame = ttk.LabelFrame(parent, text="📁 File Selection", padding=10)
        file_frame.pack(fill=tk.X, pady=10)
        
        # Input file
        input_frame = ttk.Frame(file_frame)
        input_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(input_frame, text="Input PNG:", width=12).pack(side=tk.LEFT, padx=3)
        self.input_label = ttk.Label(
            input_frame,
            text="No file",
            foreground=self.colors['text_secondary']
        )
        self.input_label.pack(side=tk.LEFT, padx=3, fill=tk.X, expand=True)
        
        ttk.Button(
            input_frame,
            text="Browse",
            command=self._select_input_file,
            width=12
        ).pack(side=tk.RIGHT, padx=2)
        
        # Output file
        output_frame = ttk.Frame(file_frame)
        output_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(output_frame, text="Output PNG:", width=12).pack(side=tk.LEFT, padx=3)
        self.output_label = ttk.Label(
            output_frame,
            text="No file",
            foreground=self.colors['text_secondary']
        )
        self.output_label.pack(side=tk.LEFT, padx=3, fill=tk.X, expand=True)
        
        ttk.Button(
            output_frame,
            text="Browse",
            command=self._select_output_file,
            width=12
        ).pack(side=tk.RIGHT, padx=2)
        
        # Color Selection Frame
        color_frame = ttk.LabelFrame(parent, text="🎯 Color Selection", padding=10)
        color_frame.pack(fill=tk.X, pady=10)
        
        # Color picker button
        color_btn_frame = ttk.Frame(color_frame)
        color_btn_frame.pack(fill=tk.X, pady=8)
        
        ttk.Button(
            color_btn_frame,
            text="Pick Color",
            command=self._pick_color,
            width=15
        ).pack(side=tk.LEFT, padx=3)
        
        # Color preview canvas
        self.color_preview = tk.Canvas(
            color_btn_frame,
            width=80,
            height=40,
            bg=self._rgb_to_hex(self.current_color),
            highlightthickness=2,
            highlightbackground=self.colors['accent']
        )
        self.color_preview.pack(side=tk.LEFT, padx=10)
        
        # RGB Sliders Frame
        slider_frame = ttk.LabelFrame(color_frame, text="RGB Values", padding=8)
        slider_frame.pack(fill=tk.X, pady=8)
        
        self._create_color_slider(slider_frame, "R:", 0, self._on_red_change)
        self._create_color_slider(slider_frame, "G:", 1, self._on_green_change)
        self._create_color_slider(slider_frame, "B:", 2, self._on_blue_change)
        
        # RGB Display
        display_frame = ttk.Frame(color_frame)
        display_frame.pack(fill=tk.X, pady=8)
        
        ttk.Label(display_frame, text="RGB:").pack(side=tk.LEFT, padx=3)
        self.rgb_display = ttk.Label(
            display_frame,
            text="(255, 255, 255)",
            font=(self.font_family, 9, 'bold'),
            foreground=self.colors['accent']
        )
        self.rgb_display.pack(side=tk.LEFT, padx=3)
        
        ttk.Label(display_frame, text=" | Hex:").pack(side=tk.LEFT, padx=3)
        self.hex_display = ttk.Label(
            display_frame,
            text="#ffffff",
            font=(self.font_family, 9, 'bold'),
            foreground=self.colors['accent']
        )
        self.hex_display.pack(side=tk.LEFT, padx=3)
        
        # Preset Colors
        preset_frame = ttk.LabelFrame(color_frame, text="Presets", padding=5)
        preset_frame.pack(fill=tk.X, pady=8)
        
        presets = [
            ("White", (255, 255, 255)),
            ("Black", (0, 0, 0)),
            ("Red", (255, 0, 0)),
            ("Green", (0, 255, 0)),
            ("Blue", (0, 0, 255)),
            ("Yellow", (255, 255, 0)),
        ]
        
        row1_frame = ttk.Frame(preset_frame)
        row1_frame.pack(fill=tk.X, pady=2)
        row2_frame = ttk.Frame(preset_frame)
        row2_frame.pack(fill=tk.X, pady=2)
        
        for idx, (name, rgb) in enumerate(presets):
            btn_frame = row1_frame if idx < 3 else row2_frame
            btn = tk.Button(
                btn_frame,
                text=name,
                bg=self._rgb_to_hex(rgb),
                fg=self._get_text_color(rgb),
                command=lambda r=rgb: self._set_color(r),
                relief=tk.FLAT,
                padx=8,
                pady=3,
                font=(self.font_family, 8),
                activebackground=self._rgb_to_hex(rgb)
            )
            btn.pack(side=tk.LEFT, padx=2, fill=tk.X, expand=True)
        
        # Action Buttons
        action_frame = ttk.Frame(parent)
        action_frame.pack(fill=tk.X, pady=15)
        
        self.process_button = ttk.Button(
            action_frame,
            text="🚀 Apply & Preview",
            command=self._process_image,
            width=20
        )
        self.process_button.pack(side=tk.LEFT, padx=3, fill=tk.X, expand=True)
        
        ttk.Button(
            action_frame,
            text="Save Output",
            command=self._save_output,
            width=15
        ).pack(side=tk.LEFT, padx=3)
        
        ttk.Button(
            action_frame,
            text="Clear",
            command=self._clear_fields,
            width=10
        ).pack(side=tk.LEFT, padx=3)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            action_frame,
            length=100,
            mode='indeterminate'
        )
        self.progress.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Status Frame
        status_frame = ttk.LabelFrame(parent, text="📝 Status", padding=8)
        status_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        scrollbar = ttk.Scrollbar(status_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.status_text = tk.Text(
            status_frame,
            height=8,
            bg=self.colors['bg_secondary'],
            fg=self.colors['text_primary'],
            yscrollcommand=scrollbar.set,
            font=(self.font_family, 8),
            wrap=tk.WORD
        )
        self.status_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.status_text.yview)
    
    def _create_image_preview_widgets(self, parent):
        """Create image preview panel."""
        # Create two columns for original and processed images
        images_frame = ttk.Frame(parent)
        images_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        # Left - Original Image
        left_frame = ttk.LabelFrame(images_frame, text="📷 Original Image (Input)", padding=8)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.input_canvas = tk.Canvas(
            left_frame,
            bg=self.colors['bg_secondary'],
            highlightthickness=2,
            highlightbackground=self.colors['accent']
        )
        self.input_canvas.pack(fill=tk.BOTH, expand=True)
        
        input_label_info = ttk.Label(
            left_frame,
            text="No image loaded",
            foreground=self.colors['text_secondary']
        )
        input_label_info.pack(pady=5)
        
        # Right - Processed Image
        right_frame = ttk.LabelFrame(images_frame, text="🖼️ Processed Image (Output Preview)", padding=8)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.output_canvas = tk.Canvas(
            right_frame,
            bg=self.colors['bg_secondary'],
            highlightthickness=2,
            highlightbackground=self.colors['accent']
        )
        self.output_canvas.pack(fill=tk.BOTH, expand=True)
        
        output_label_info = ttk.Label(
            right_frame,
            text="Preview will appear here",
            foreground=self.colors['text_secondary']
        )
        output_label_info.pack(pady=5)
        
        # Store references for info labels
        self.input_info_label = input_label_info
        self.output_info_label = output_label_info
    
    def _create_color_slider(self, parent, label_text, color_index, on_change):
        """Create a color slider with label and value display."""
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, pady=4)
        
        ttk.Label(frame, text=label_text, width=3).pack(side=tk.LEFT)
        
        slider = ttk.Scale(
            frame,
            from_=0,
            to=255,
            orient=tk.HORIZONTAL,
            command=on_change
        )
        slider.set(self.current_color[color_index])
        slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)
        
        value_label = ttk.Label(frame, text=str(self.current_color[color_index]), width=5)
        value_label.pack(side=tk.RIGHT, padx=3)
        
        # Store slider references
        setattr(self, f'slider_{color_index}', slider)
        setattr(self, f'value_label_{color_index}', value_label)
    
    def _on_red_change(self, value):
        """Handle red slider change."""
        r = int(float(value))
        self.current_color = (r, self.current_color[1], self.current_color[2])
        self._update_color_display()
        if self.input_pil_image:
            self._update_preview()
    
    def _on_green_change(self, value):
        """Handle green slider change."""
        g = int(float(value))
        self.current_color = (self.current_color[0], g, self.current_color[2])
        self._update_color_display()
        if self.input_pil_image:
            self._update_preview()
    
    def _on_blue_change(self, value):
        """Handle blue slider change."""
        b = int(float(value))
        self.current_color = (self.current_color[0], self.current_color[1], b)
        self._update_color_display()
        if self.input_pil_image:
            self._update_preview()
    
    def _update_color_display(self):
        """Update color display elements."""
        hex_color = self._rgb_to_hex(self.current_color)
        
        self.color_preview.config(bg=hex_color)
        self.rgb_display.config(
            text=f"({self.current_color[0]}, {self.current_color[1]}, {self.current_color[2]})"
        )
        self.hex_display.config(text=hex_color)
        
        # Update value labels
        self.value_label_0.config(text=str(self.current_color[0]))
        self.value_label_1.config(text=str(self.current_color[1]))
        self.value_label_2.config(text=str(self.current_color[2]))
    
    def _set_color(self, rgb):
        """Set color from preset."""
        self.current_color = rgb
        self.slider_0.set(rgb[0])
        self.slider_1.set(rgb[1])
        self.slider_2.set(rgb[2])
        self._update_color_display()
        if self.input_pil_image:
            self._update_preview()
    
    def _pick_color(self):
        """Open color picker dialog."""
        color = colorchooser.askcolor(
            color=self._rgb_to_hex(self.current_color),
            title="Choose background color"
        )
        
        if color[0]:
            rgb = tuple(int(round(c)) for c in color[0])
            self._set_color(rgb)
    
    def _select_input_file(self):
        """Select input image file."""
        file_path = filedialog.askopenfilename(
            title="Select input PNG image",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        
        if file_path:
            self.input_image_path = file_path
            filename = os.path.basename(file_path)
            self.input_label.config(text=filename[:20] + "..." if len(filename) > 20 else filename)
            
            # Load and display original image
            try:
                self.input_pil_image = Image.open(file_path)
                self._add_status(f"✅ Image loaded: {self.input_pil_image.size}")
                self._display_input_image()
                self._update_preview()
            except Exception as e:
                self._add_status(f"❌ Error loading image: {str(e)}")
                messagebox.showerror("Error", f"Cannot load image:\n{str(e)}")
    
    def _select_output_file(self):
        """Select output file location."""
        file_path = filedialog.asksaveasfilename(
            title="Save processed image as",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        
        if file_path:
            self.output_image_path = file_path
            filename = os.path.basename(file_path)
            self.output_label.config(text=filename[:20] + "..." if len(filename) > 20 else filename)
            self._add_status(f"📁 Output path set: {filename}")
    
    def _display_input_image(self):
        """Display input image on canvas."""
        if not self.input_pil_image:
            return
        
        canvas_width = self.input_canvas.winfo_width()
        canvas_height = self.input_canvas.winfo_height()
        
        if canvas_width <= 1 or canvas_height <= 1:
            self.after(100, self._display_input_image)
            return
        
        # Resize image to fit canvas
        img = self.input_pil_image.copy()
        img.thumbnail((canvas_width - 10, canvas_height - 10), Image.Resampling.LANCZOS)
        
        self.input_photo_image = ImageTk.PhotoImage(img)
        self.input_canvas.delete("all")
        self.input_canvas.create_image(
            canvas_width // 2,
            canvas_height // 2,
            image=self.input_photo_image
        )
        
        size_text = f"{self.input_pil_image.size[0]}x{self.input_pil_image.size[1]} px"
        self.input_info_label.config(text=size_text)
    
    def _update_preview(self):
        """Update output preview with current color."""
        if not self.input_pil_image:
            return
        
        try:
            # Create preview by applying color to input image
            img = self.input_pil_image.copy()
            
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Create background with current color
            background = Image.new('RGB', img.size, self.current_color)
            background.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
            
            # Resize for display
            canvas_width = self.output_canvas.winfo_width()
            canvas_height = self.output_canvas.winfo_height()
            
            if canvas_width <= 1 or canvas_height <= 1:
                self.after(100, self._update_preview)
                return
            
            display_img = background.copy()
            display_img.thumbnail((canvas_width - 10, canvas_height - 10), Image.Resampling.LANCZOS)
            
            self.output_photo_image = ImageTk.PhotoImage(display_img)
            self.output_canvas.delete("all")
            self.output_canvas.create_image(
                canvas_width // 2,
                canvas_height // 2,
                image=self.output_photo_image
            )
            
            size_text = f"{self.input_pil_image.size[0]}x{self.input_pil_image.size[1]} px - RGB{self.current_color}"
            self.output_info_label.config(text=size_text)
            
        except Exception as e:
            self._add_status(f"❌ Preview error: {str(e)}")
    
    def _process_image(self):
        """Process and save the image."""
        if not self.input_image_path:
            messagebox.showerror("Error", "Please select an input image!")
            return
        
        if not self.output_image_path:
            messagebox.showerror("Error", "Please select an output location!")
            return
        
        self.process_button.config(state=tk.DISABLED)
        self.progress.start()
        self._add_status("⏳ Processing image...")
        
        thread = threading.Thread(
            target=self._process_thread,
            args=(self.input_image_path, self.output_image_path, self.current_color)
        )
        thread.start()
    
    def _process_thread(self, input_path, output_path, rgb_color):
        """Process image in background thread."""
        try:
            success = self.setter.set_background_color(input_path, output_path, rgb_color)
            
            if success:
                self._add_status("✅ Image processed and saved successfully!")
                self.after(0, lambda: messagebox.showinfo(
                    "Success",
                    f"Image saved to:\n{output_path}\n\nDo you want to open it?"
                ))
            else:
                self._add_status("❌ Processing failed!")
                self.after(0, lambda: messagebox.showerror("Error", "Failed to process image."))
        except Exception as e:
            self._add_status(f"❌ Error: {str(e)}")
            self.after(0, lambda: messagebox.showerror("Error", f"Error: {str(e)}"))
        finally:
            self.after(0, lambda: [
                self.process_button.config(state=tk.NORMAL),
                self.progress.stop()
            ])
    
    def _save_output(self):
        """Save the current preview as output."""
        if not self.input_pil_image:
            messagebox.showerror("Error", "No image loaded!")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Save preview image as",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                img = self.input_pil_image.copy()
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
                
                background = Image.new('RGB', img.size, self.current_color)
                background.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
                
                background.save(file_path, 'PNG')
                self._add_status(f"✅ Saved to: {os.path.basename(file_path)}")
                messagebox.showinfo("Success", f"Image saved to:\n{file_path}")
            except Exception as e:
                self._add_status(f"❌ Save error: {str(e)}")
                messagebox.showerror("Error", f"Failed to save:\n{str(e)}")
    
    def _clear_fields(self):
        """Clear all fields."""
        self.input_image_path = None
        self.output_image_path = None
        self.input_pil_image = None
        self.current_color = (255, 255, 255)
        
        self.input_label.config(text="No file")
        self.output_label.config(text="No file")
        
        self.slider_0.set(255)
        self.slider_1.set(255)
        self.slider_2.set(255)
        
        self._update_color_display()
        
        self.input_canvas.delete("all")
        self.output_canvas.delete("all")
        self.input_info_label.config(text="No image loaded")
        self.output_info_label.config(text="Preview will appear here")
        
        self.status_text.delete(1.0, tk.END)
        self._add_status("Ready for new operation.")
    
    def _add_status(self, message):
        """Add message to status text."""
        def update():
            self.status_text.insert(tk.END, message + "\n")
            self.status_text.see(tk.END)
            self.status_text.update()
        
        self.after(0, update)
    
    @staticmethod
    def _rgb_to_hex(rgb):
        """Convert RGB tuple to hex color string."""
        return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
    
    @staticmethod
    def _get_text_color(rgb):
        """Determine if text should be black or white based on brightness."""
        r, g, b = rgb
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        return "black" if luminance > 0.5 else "white"


def main():
    """Main entry point for the application."""
    app = BGSetterGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
