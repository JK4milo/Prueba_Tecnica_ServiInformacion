import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import Utils

class FileExplorer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("File Explorer")
        self.geometry("800x600")

        # Create the Treeview widget
        self.tree = ttk.Treeview(self)
        self.tree.heading("#0", text="SEARCH FOR AN IMAGE AN TRY THE MODEL", anchor='w')
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create a Scrollbar for the Treeview
        self.tree_scroll = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.tree_scroll.set)
        self.tree_scroll.pack(side=tk.LEFT, fill=tk.Y)

        # Create a Frame for displaying images
        self.image_frame = ttk.Frame(self)
        self.image_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.image_label = ttk.Label(self.image_frame)
        self.image_label.pack(fill=tk.BOTH, expand=True)

        self.title_label = ttk.Label(self.image_frame, text="", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.title_predict = ttk.Label(self.image_frame, text="", font=("Helvetica", 16))
        self.title_predict.pack(pady=20)
        # Add a button to the image frame
        self.button = ttk.Button(self.image_frame, text="Click to Predict!", command=self.on_button_click)
        self.button.pack(pady=10)
        self.button.pack_forget()  # Hide button initially

        self.populate_tree()
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def populate_tree(self):
        path = os.getcwd()
        self.path = os.path.join(path,'image_test')
        node = self.tree.insert('', 'end', text=self.path, open=True)
        self.process_directory(node, self.path)

    def process_directory(self, parent, path):
        for item in os.listdir(path):
            abs_path = os.path.join(path, item)
            is_dir = os.path.isdir(abs_path)

            node = self.tree.insert(parent, 'end', text=item, open=False)
            if is_dir:
                self.process_directory(node, abs_path)

    def on_tree_select(self, event):
        selected_item = self.tree.selection()[0]
        file_path = self.get_full_path(selected_item)
        
        if os.path.isfile(file_path) and self.is_image_file(file_path):
            self.display_image(file_path)

            raw_text = os.path.basename(file_path)
            file_path_splitted=file_path.split('\\')[::-1][2]
            file_path_splitted = f'y_true: {file_path_splitted}'
            self.title_label.config(text=file_path_splitted)
            self.button.pack(pady=10)  # Show button when an image is displayed
        else:
            self.title_label.config(text="")
            self.button.pack_forget()  # Hide button if no image is selected

    def get_full_path(self, item):
        path = self.tree.item(item, 'text')
        parent = self.tree.parent(item)
        while parent:
            path = os.path.join(self.tree.item(parent, 'text'),path)
            self.path_final = path
            parent = self.tree.parent(parent)
        return path

    def is_image_file(self, file_path):
        valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
        return file_path.lower().endswith(valid_extensions)

    def display_image(self, file_path):
        image = Image.open(file_path)
        image = image.resize((400, 400), Image.LANCZOS)  # Resize for display purposes
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def on_button_click(self):
        label_dict = {0: 'Avulsion fracture', 1: 'Comminuted fracture', 2: 'Fracture Dislocation', 3: 'Greenstick fracture', 4: 'Hairline Fracture', 5: 'Impacted fracture', 6: 'Longitudinal fracture', 7: 'Oblique fracture', 8: 'Pathological fracture', 9: 'Spiral Fracture'}
        IMG_PATH = self.path_final
        MODEL_PATH = r'D:\Users\user\Desktop\prueba-tecnica-Servinformacion\model\BestCNNModel.keras'

        ut = Utils(MODEL_PATH,IMG_PATH,label_dict)
        prediction = ut.predict()
        if prediction:
            text = f'y_pred: {prediction}'
            self.title_predict.config(text= text)
if __name__ == "__main__":
    app = FileExplorer()
    app.mainloop()
