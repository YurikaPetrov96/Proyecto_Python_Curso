import customtkinter
from gui.logreg import Login_register
from gui.registro import Registro


pages = {
    "Start_page": Login_register,
    "Registry_page": Registro
}

class App(customtkinter.CTk):
    """Ventana principal"""
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #definimos el tamaño y configuración
        self.title("Music Tour")
        self.iconbitmap("music.ico")
        self._set_appearance_mode("System")
        window_width = 800
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight() 
        x_coordinate = (screen_width - window_width)
        y_coordinate = (screen_height - window_height)
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        
        self._frame = None
        self.switch_frame("Start_page")
    
    def switch_frame(self, page_name):
        """Destroys current frame and replaces it with a new one."""
        cls = pages[page_name]
        new_frame = cls(parent=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()