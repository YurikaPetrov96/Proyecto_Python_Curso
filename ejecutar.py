
import customtkinter
import os
from gui.logreg import Login_register
from gui.registro import Registro
from gui.home import Home

pages = {
    "Start_page": Login_register,
    "Registry_page": Registro,
    "Home_page": Home
}

class App(customtkinter.CTk):
    """Ventana principal"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Definimos el tamaño y configuración
        customtkinter.set_default_color_theme("data/cimne_theme.json")
        self.title("Music Tour")
        self.iconbitmap("src/music.ico")
        window_width = 800
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight() 
        x_coordinate = ((screen_width - window_width) // 2)
        y_coordinate = ((screen_height - window_height) // 2)
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        self.current_frame = None
        self.stored_frames = {}
        self.user_id = None
        self.switch_frame("Start_page")
        
        
    def user_id_callback(self):
        self.usuario_id = self.user_id
    
    

    def switch_frame(self, page_name):
        new_frame = self.stored_frames.get(page_name)

        if new_frame is None:
            cls = pages[page_name]
            new_frame = cls(parent=self, switch_frame_callback=self.switch_frame)
            self.stored_frames[page_name] = new_frame
        else:
            new_frame.update()  # hacemos una llamada a un metodo Update para poder refrescar los frames.

        if self.current_frame is not None:
            self.current_frame.pack_forget()

        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)
        
        
        # hacemos un llamado al user_id ingresado al momento de ingresar el usuario.
        if hasattr(self.current_frame, "set_user_id"):
            self.current_frame.set_user_id(self.user_id)
        
        # for debugging process:
        # print(f"Switching to {page_name} frame")
        # print(f"Current frame: {new_frame}")
        # print(f"Current frame attributes: {vars(new_frame)}")
        # print(f"Stored frames: {self.stored_frames}")
        # print("-" * 30)

if __name__ == "__main__":
    app = App()
    app.mainloop()
    